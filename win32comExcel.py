import win32com.client

excel = win32com.client.Dispatch("Excel.Application")

excel.Visible = True
wb = excel.WorkBooks.Add()
ws = wb.WorkSheets("Sheet1")
ws.Cells(1,1).Value = "Hello World"

wb.SaveAs('./test.xlsx')
excel.Quit()

wb = excel.WorkBooks.Open('./test.xlsx')
ws = wb.ActiveSheet
print(ws.Cells(1,1).Value)
excel.Quit()
