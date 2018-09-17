#This exercise just teaches what the function return

def add_twoNumbers(a,b):
    print(f"adding {a} + {b}")
    return a+b

def subtract_twoNumbers(a,b):
    print(f"subtracting {a} - {b}")
    return a-b

age = add_twoNumbers(12,13)
diff = subtract_twoNumbers(20,15)

print(age)
print(diff)
