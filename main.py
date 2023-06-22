from openpyxl import Workbook

wb = Workbook()

ws1 = wb.get_sheet_by_name('Sheet')

ws1.title = 'aiden'

ws2 = wb.create_sheet('aiden2')

print(wb.sheetnames)



wb.save('balances.xlsx')