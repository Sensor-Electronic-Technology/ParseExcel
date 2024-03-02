import pandas as pd
import numpy as np
import threading


def parse_after_first_word(str):
    words = str.split()
    return ' '.join(words[1:])


def func2(x, a1, t1, y0):
    return a1 * np.exp(np.divide(-x, t1)) + y0
    # Linear Function - for Cree Data Flux and VF vs Temperature


def func3(x, m, t_bin):
    return m * (x - t_bin) + 1

    # Function for finding which value in array is closest to 1 - use for finding nominal current


def closest(lst, k):
    lst = np.asarray(lst)
    idx = (np.abs(lst - k)).argmin()
    return idx

    # Function to find negative elements from 1 list and delete the associated index items from 3 lists This
    # function is an attempt to solve a problem where the curve_fit function doesn't work when encountering
    # numbers less than 0


def negdelarr(arr1, arr2, arr3):
    negs = []
    it = np.nditer(arr1, flags=['f_index'])
    for i in it:
        if i < 0:
            negs.append(it.index)
    # np.delete(arr1,negs,axis=1)
    arr1 = np.delete(arr1, negs)
    arr2 = np.delete(arr2, negs)
    arr3 = np.delete(arr3, negs)
    return arr1, arr2, arr3


# Define Functions
# Polynomial Function - for Cree Data Flux & VF vs current
def solve_poly(x, a, b, c, d):
    return a * x ** 3 + b * x ** 2 + c * x + d


class ExcelParser:
    def __init__(self, file_path, sheet_name, start_index):
        self.thread = None
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.start_index = start_index
        self.excelFile = pd.ExcelFile(file_path)
        self.data_frame = self.excelFile.parse(sheet_name)
        self.row_count = 0
        self.stop_flag = False

    def start_parsing(self):
        self.stop_flag = False
        print("Starting Thread")
        self.thread = threading.Thread(target=self.parse)
        self.thread.start()

    def stop_parsing(self):
        self.stop_flag = True
        #self.thread.join()

    def parse(self):
        print(F"Start: {self.start_index}")
        for rindex,row in self.data_frame.iterrows():
            if(rindex>=self.start_index and self.stop_flag==False):
                good_row=pd.notnull(row.iat[0])
                good_row&=pd.notnull(row.iat[1])
                if good_row:
                    self.parse_row(row,rindex)

    def parse_row(self, row, index):
        part=parse_after_first_word(row.iat[0])
        FPF = row.iloc[6:10]
        
        print(f"Name: {part} [0]: {FPF[0]} [1]: {FPF[1]} [2]: {FPF[2]} [3]: {FPF[3]}")
        #
        # # get model name
        # PN = data.iat[i, 0]
        # print(PN)
        # # get current bounds
        # ILB = data.iat[i, 4]
        #
        # # print('ILB')
        # # print(ILB)
        # IUB = data.iat[i, 5]
        # # print('IUB')
        # # print(IUB)
        # # Set temp lower bound
        # TLB = 25
        # # Set temp Upper bound
        # TUB = 125
        # # Set Flux Slope Temperature Coefficient
        # FSTC = data.iat[i, 14]
        # # print('fstc')
        # # print(FSTC)
        # # Set binning temp
        # Tbin = data.iat[i, 15]
        # # print(Tbin)
        # # Set Voltage Slope Temperature Coefficient
        # VSTC = data.iat[i, 16]
        # # get Flux polynomial function constants
        # # print(VSTC)
        # FPF = data.iloc[i][6:10]
        # # print(FPF)
        # # get Voltage polynomial function constants
        # VPF = data.iloc[i][10:14]
        # print(VPF)

    @property
    def row_count(self):
        self._row_count = self.data_frame['A'].dropna().shape[0]
        return self._row_count

    @row_count.setter
    def row_count(self, value):
        self._row_count = value

    @property
    def stop_flag(self):
        return self._stop_flag

    @stop_flag.setter
    def stop_flag(self, value):
        self._stop_flag = value
