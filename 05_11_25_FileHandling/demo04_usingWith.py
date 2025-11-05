# Another syntax to handle files is by using 'with' statement
# It automatically takes care of closing the file after its suite finishes
with open("vegetables.txt", "r") as text_file: 
    fileContent = text_file.read()     
    lines = text_file.readlines()
    for line in lines:
        print(f"Line: {line.strip()}")