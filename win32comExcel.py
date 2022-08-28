import win32com.client

excel = win32com.client.Dispatch("Excel.Application")

excel.Visible = True
wb = excel.WorkBooks.Open("./practice.xlsx")
ws = wb.ActiveSheet
print(ws.Cells(1,1).Value)

ws.Cells(1,2).Value = "is"
ws.Range("C1").Value = "Good"
ws.Range("C1").Interior.ColorIndex = 10
