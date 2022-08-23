import win32com.client

excel = win32com.client.Dispatch("Excel.Application")

excel.Visible = True
wb = excel.WorkBooks.Add()
ws = wb.WorkSheets("Sheet1")
