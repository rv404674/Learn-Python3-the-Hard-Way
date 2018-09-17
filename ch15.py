#import argv module from sys
from sys import argv

#load script name in argv and filename in filename
script, filename = argv

#open the file
txt = open(filename)
print(f"Here's your file {filename};")
print(txt.read())

print("Type the filename again:")
file_again = input(">")

txt_again = open(file_again)

print(txt._again.read())
