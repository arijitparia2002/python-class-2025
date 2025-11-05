
text_file  = open("C:/Users/ariji/Desktop/Ai Class PPT/Ai Class Python Codes/05_11_25_FileHandling/fruits.txt", "r")
# if you want to read line by line
# line = text_file.readline()
# line1 = text_file.readline()


# print(line)
# print(line1)

lines = text_file.readlines()
print(lines)

for line in lines:
    print(line.strip())
    

text_file.close()