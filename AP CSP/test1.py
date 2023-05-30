import xlrd

# 打开Excel文件
workbook = xlrd.open_workbook('teat.xls')

# 选择第一个sheet
sheet = workbook.sheet_by_index(0)

# 读取数据
for row in range(sheet.nrows):
    for col in range(sheet.ncols):
        cell_value = sheet.cell(row, col).value
        print(cell_value)