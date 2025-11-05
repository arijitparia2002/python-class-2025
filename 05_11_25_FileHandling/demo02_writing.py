
text_file  = open("C:/Users/ariji/Desktop/Ai Class PPT/Ai Class Python Codes/05_11_25_FileHandling/fruits.txt", "w")

# write something to the file
text_file.write("Mango is the king of fruits\n")
text_file.write("Grapes are small fruits\n")

text_file.close()


# if the file does not exist, it will be created
new_file  = open("vegetables.txt", "w")

new_file.write("Carrot is orange in color\n")
new_file.write("Spinach is green leafy vegetable\n")

new_file.close()