# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import numpy as np
import tkinter as tk

from parser_interface import ParserInterface


def solve_lf_poly(x3, x2, x1, x, a):
    coefficients = [x3, x2, x1, x]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ui = ParserInterface()
    ui.run()

    # # Replace 'your_file.xlsx' with the path to your Excel file
    # file_path = 'C:\\Users\\aelmendo\\Documents\\CompetitorFiles\\CREE_LEDs.xlsx'

    # # Read the Excel file
    # # You might need to specify the sheet name or number if the Excel file has multiple sheets
    # excelFile = pd.ExcelFile(file_path)
    # dataFrame=excelFile.parse('Models');

    # for index,row in dataFrame.iterrows():
    #     if(index<10):
    #         parse_row(row,index)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
