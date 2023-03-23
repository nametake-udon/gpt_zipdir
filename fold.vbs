' Create a folder with today's date and "_send" suffix
Dim fso, currentDate, folderName
Set fso = CreateObject("Scripting.FileSystemObject")
currentDate = Year(Date) & Right("0" & Month(Date), 2) & Right("0" & Day(Date), 2)
folderName = currentDate & "_send"
fso.CreateFolder(folderName)
