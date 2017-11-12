#!/usr/bin/env python3
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = sys.argv[1]

print('sys.argv[1]', sys.argv[1])

first_enter_tag = False

dic_table = {}
dic_temp = {}

list_table = []
list_row = []

with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('Sheet1')
    print("worksheet.nrow: ", worksheet.nrows)
    print("worksheet.ncols: ", worksheet.ncols)
    for row_index in range(worksheet.nrows):
        if (row_index == 0):
            continue

        for col_index in range(worksheet.ncols):
            if (col_index == 0 and worksheet.cell_value(row_index, col_index) != ''):
                if (first_enter_tag == True):
                    dic_temp[county] = list_table[:]
                    dic_table.update(dic_temp)
                    list_table.clear()
                    dic_temp.clear()
                county = worksheet.cell_value(row_index, col_index)
                dic_temp.setdefault(county)
               # print("show county value: ", county)

                if (first_enter_tag == False):
                    first_enter_tag = True

            if (col_index != 0 and worksheet.cell_value(row_index, col_index) != ''):
                list_row.append(worksheet.cell_value(row_index, col_index))
        list_table.append(list_row[:])
        list_row.clear()

print(dic_table)
