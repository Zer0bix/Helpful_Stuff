# Settings
variables = []  # Fill the list with the attributes of the class (e.g. ["size", "speed"])
str_variables = "location height age"         # If variables is empty, it will use this (separate variable names with a space " ") e.g. "size speed"
str_comma_variables = "make, model, year, isRunning"  # If both variables and str_variables are empty, it will use this (separate variable names with a comma and a space ", ") e.g. "size, speed"
private = "protected"  # Options: "private", "protected", ""        # any empty input will translate to normal attributes
name = "Car"  # Name of the class 

# File settings
create_file = True  # Push the output to "NewClass.py"?
file_name = "NewClass.py"
file_path = "auto_class/create/" + file_name