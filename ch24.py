print("let's practice everything")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs')

poem="""
\t The lovely world
with logic so firmly planted
cannot discern\n the needs of love
\n\t\twhere there is none.
"""

print("-----------------")
print(poem)
print("--------------")

five = 10-2+3-6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started*500
    jars = jelly_beans /1000
    return jelly_beans, jars

start_point = 10000
beans, jars = secret_formula(start_point)

#remember there is a another way to print strings
print("With a starting poing of :{}".format(start_point))
#it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars.")

formula = secret_formula(start_point)

print("We\'d have {} beans, {} jars." .format(*formula))
