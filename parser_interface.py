import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import font
from excel_parser import ExcelParser
import threading
import os
import sys
import time


class ParserInterface:
    def __init__(self):
        self.excel_parser = None
        self.stop_flag = False
        self.thread = None
        self.root = tk.Tk()

        self.selected_file_path = tk.StringVar()
        self.sheet_name = tk.StringVar()
        self.start_index_input = tk.IntVar()
        self.selected_file_path.set("C:/Users/aelmendo/Documents/CREE_LEDs.xlsx")
        self.start_index_input.set(5)
        self.sheet_name.set("Models")

        current_directory = os.getcwd()
        icon_path = os.path.join(current_directory, "resources", "icons8-folder-48.png")
        self.default_font = font.nametofont("TkDefaultFont")
        self.default_font.configure(size=14)

        self.fIcon = tk.PhotoImage(file=icon_path)
        self.notebook = ttk.Notebook(self.root)
        self.tab1 = ttk.Frame(self.notebook, padding=10)
        self.tab1.grid_columnconfigure(0, weight=1)
        self.notebook.add(self.tab1, text="Input")
        self.tab2 = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(self.tab2, text="Output")
        self.progress_bar = ttk.Progressbar(self.tab2, orient='horizontal', mode='determinate', length=100)
        self.console = tk.Text(self.tab2)
        self.create_interface()

    def run(self):
        self.root.mainloop()

    def file_browser_handler(self):
        file_path = tk.filedialog.askopenfilename()
        self.selected_file_path.set(file_path)

    def stop_parsing(self):
        self.excel_parser.stop_parsing()
        # self.excel_parser.stop_flag = True
        # self.thread.join()

    def start_parsing(self):
        self.excel_parser.start_parsing()
        # self.excel_parser.stop_flag = False
        # self.thread = threading.Thread(target=self.excel_parser.parse)
        # self.thread.start()

    def submit(self):
        print(f"File Path: {self.selected_file_path.get()}")
        print(f"Sheet Name: {self.sheet_name.get()}")
        print(f"Start Index: {self.start_index_input.get()}")
        self.excel_parser = ExcelParser(self.selected_file_path.get(),self.sheet_name.get(), self.start_index_input.get())
        self.notebook.select(self.tab2)

    def create_interface(self):
        row = self.create_file_path_input()
        m_row = self.create_sheet_input(row)
        l_row = self.create_number_input(m_row)
        
        submit_button = tk.Button(self.tab1, text="Submit", command=self.submit)
        submit_button.grid(row=l_row, column=0, columnspan=3, sticky="nsew")

        parse_button = tk.Button(self.tab2, text="Start Parsing", command=self.start_parsing)
        parse_button.grid(row=0, column=0, columnspan=2)

        stop_button = tk.Button(self.tab2, text="Stop Parsing", command=self.stop_parsing)
        stop_button.grid(row=0, column=2, columnspan=2)

        self.progress_bar.grid(row=1, column=0, columnspan=3, sticky="nsew")
        self.console.grid(row=2, column=0, columnspan=4, rowspan=5)
        sys.stdout = ConsoleOutput(self.console)
        self.notebook.pack(expand=True, fill="both")

    def create_file_path_input(self):
        f_row = 0
        # Create File Input Label
        label = tk.Label(self.tab1, text="Enter File Path:")
        label.grid(row=f_row, column=0, columnspan=3)
        # Create File Input Entry
        f_row += 1
        entry = tk.Entry(self.tab1, textvariable=self.selected_file_path, font=self.default_font)
        entry.grid(row=f_row, column=0, columnspan=2, sticky="nsew")
        # Create File Input Button
        f_button = tk.Button(self.tab1, command=self.file_browser_handler, image=self.fIcon)
        f_button.grid(row=f_row, column=3, columnspan=1, sticky="nsew")
        f_row += 1
        return f_row

    def create_number_input(self, l_row):
        index_label = tk.Label(self.tab1, text="Enter Start Index: ")
        index_label.grid(row=l_row, column=0, columnspan=3, sticky="nsew")
        l_row += 1

        index_entry = tk.Spinbox(self.tab1, textvariable=self.start_index_input, font=self.default_font)
        index_entry.grid(row=l_row, column=0, columnspan=3, sticky="nsew")
        l_row += 1
        return l_row

    def create_sheet_input(self, l_row):
        sheet_label = tk.Label(self.tab1, text="Enter Sheet Name: ")
        sheet_label.grid(row=l_row, column=0, columnspan=3, sticky="nsew")
        l_row += 1
        sheet_entry = tk.Entry(self.tab1, textvariable=self.sheet_name, font=self.default_font)
        sheet_entry.grid(row=l_row, column=0, columnspan=3, sticky="nsew")
        l_row += 1
        return l_row


class ConsoleOutput:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, text):
        self.text_widget.insert(tk.END, text)
        self.text_widget.see(tk.END)

    def flush(self):
        pass
