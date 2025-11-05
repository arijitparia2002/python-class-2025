
text_file  = open("C:/Users/ariji/Desktop/Ai Class PPT/Ai Class Python Codes/05_11_25_FileHandling/fruits.txt", "r")
content = text_file.read()
print(content)
# if you want to read line by line
# line = text_file.readline()
text_file.close()