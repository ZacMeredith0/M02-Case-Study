# Zac Meredith. What did you make in school. This app will be able to ask a person for their first name, last name, and their GPA to figure out what they made in school like Dean's List and Honor Roll. 
# They also will be prompted if they didn't make either

lastname = input("What is your last name?  ")
if lastname == "ZZZ": exit()
firstname = input("What is your first name? ")
gpa = input("Please enter your GPA? ")

if float(gpa) >= 3.5:
       print(lastname, firstname, "qualifies for the Dean's List.")
elif float(gpa) >= 3.25:
       print(lastname, firstname, "qualifies for the Honor Roll.")
else:
       print(lastname, firstname,  "does not qualify for either the Dean's List or the Honor Roll.")