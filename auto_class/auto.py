"""
    Takes a list of variable names, and generates a basic set of getters and setters for those variables.
    Change the variables list to include the variables you desire.

    Instructions:
        Fill out one of the variables in # Settings
        Choose your variable type (private, protected or normal)
        Name your class
        Choose whether or not to write to the local file "NewClass.py" with the output
        Run the module
"""

import sys
import io

from settings import variables, str_variables, str_comma_variables, private, name, create_file, file_name, file_path

# Generate variables if it's empty
if not variables:
    if not str_variables:
        variables = str_comma_variables.split(", ")
    else:
        variables = str_variables.split(" ")


def get(var, indent_count):
    global private
    if private == "private":
        print(tab*indent_count + f"def get{var[0].upper() + var[1:]}(self):\n" + tab*indent_count + tab + f"return self.__{var}")
    elif private == "protected":
        print(tab*indent_count + f"def get{var[0].upper() + var[1:]}(self):\n" + tab*indent_count + tab + f"return self._{var}")
    else:
        print(tab*indent_count + f"def get{var[0].upper() + var[1:]}(self):\n" + tab*indent_count + tab + f"return self.{var}")
    

def set(var, indent_count):
    global private
    if private == "private":
        print(tab*indent_count + f"def set{var[0].upper() + var[1:]}(self, {var}):\n" + tab*indent_count + tab + f"self.__{var} = {var}")
    elif private == "protected":
        print(tab*indent_count + f"def set{var[0].upper() + var[1:]}(self, {var}):\n" + tab*indent_count + tab + f"self._{var} = {var}")
    else:
        print(tab*indent_count + f"def set{var[0].upper() + var[1:]}(self, {var}):\n" + tab*indent_count + tab + f"self.{var} = {var}")

def define(var, indent_count):
    global private
    if private == "private":
        print(tab*indent_count + f"__{var} = None")
    elif private == "protected":
        print(tab*indent_count + f"_{var} = None")
    else:
        print(tab*indent_count + f"{var} = None")

def initiate(var, indent_count):
    global private
    if private == "private":
        print(tab*(1+indent_count) + f"self.__{var} = {var}")
    elif private == "protected":
        print(tab*(1+indent_count) + f"self._{var} = {var}")
    else:
        print(tab*(1+indent_count) + f"self.{var} = {var}")
    

# Settings for the builder
# variables = ["height", "body_colour", "legs_count", "eye_colour", "age", "name", "type"]  # Make a list of strings that are the variables you wish the class to have
tab = "    "
doGap = True
indent_count = 1
# name = "Animal"  # Name of the class

# File Stuff
old_stdout = sys.stdout # Memorize the default stdout stream
sys.stdout = buffer = io.StringIO()

output = ""
# Displaying the output of the builder
print(f"class {name}:")
output += (f"class {name}:")
print(indent_count*tab + "# Attributes")
for var in variables:
    define(var, indent_count)
print()

print(indent_count*tab + "# Initialize")
print(tab + "def __init__(self, ", end="")
for var in variables:
    if var != variables[::-1][0]:
        print(f"{var} = None, ", end="")
    else:
        print(f"{var} = None)", end="")
print(":")
# print(str(variables[:]).replace("[", "").replace("]", "").replace("'", ""), end="", sep=", ")
print()
for var in variables:
    initiate(var, indent_count)


print()
print(indent_count*tab + "# Getters")
for var in variables:
    get(var, indent_count)
    if doGap:
        print()
print()

print(indent_count*tab + "# Mutators")
for var in variables:
    set(var, indent_count)
    if doGap:
        print()
print()


sys.stdout = old_stdout # Put the old stream back in place
whatWasPrinted = buffer.getvalue() # Return a str containing the entire contents of the buffer.

if create_file:
    with open(file_path, 'w') as newClass:
        newClass.write(whatWasPrinted)
do_print_to_log = input("Do you want it printed to log?")
if do_print_to_log.lower() in ["yes", "true", "do", "yep", "y"]:
    print(whatWasPrinted)
