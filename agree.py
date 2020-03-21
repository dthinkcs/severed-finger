import re


user_input = input("Do you agree?\n")
if re.search("^y(es)?$", user_input, re.IGNORECASE):
    print("Agreed.")
elif re.search("^n(o)?$", user_input, re.IGNORECASE):
    print("Not Agreed.")
