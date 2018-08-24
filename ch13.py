#This chapter is about commandline arguement

from sys import argv
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variableis:", third)

print(int(third)+20)
