# close : Close the file like file->save
# read : Read the content of file.
# readline : Read one line of text file
# truncate : Empties the whole file
# write : Write stuff to the file

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}")
print("If you dont want that enter CLTRL-C.")
print("If you do want that hit RETURN.")

input("?")
print("Opening the file")
#Open command open the file to be written in write mode
target = open(filename, 'w')

print("Truncating the file. Good Bye!")
#Delete all the contents of the file
target.truncate()

print("Input some lines")
#Takes input from user
input1 = input()
input2 = input()

print("I am going to write these line to file")
target.write(input1 + "\n" + input2 + "\n")

print("And finally we close it.")
target.close()


