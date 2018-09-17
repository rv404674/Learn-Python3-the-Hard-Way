#Names, Variables, Code, Functiions

#this one is like your scripts with argv

def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#thiis just takes one arguement
def print_one(arg1):
    print(f"arg1: {arg1}")


#this arguement takes no arguement
def print_none():
    print("I got nothing'.")

print_two("Zed", "Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
