from datetime import date
import re
"""
● Background: Build a program that validates the personal data of a user’s application.

● Challenge: Allow a user to enter all their personal information for an application and validates the input according to a specific criteria.

● Objective: Use defensive programming to ensure the user input is valid:
    ○ Use conditional statements for input validation.
    ○ Use try-except blocks to gracefully manage unexpected exceptions
    ○ Recognise and address various error types.
    
Input user data
    Name, Surname, Birth date, Cell phone number, E-mail address, Location and Programming languages
"""

# keys = ["name", "surname", "birth_date", "cell_number", "e_mail", "country", "programming_languages"]

# Targeted data like this:
# user1 = dict(name = "", surname = "", birth_date = "", cell_number = "", e_mail = "", country = "", programming_languages = "")


user1 = dict()

name = ""
surname = ""
birth_date = ""
cell_number = ""
e_mail = ""
country = ""
programming_languages = ""


while name == "" :
    name = input("Enter your name: ")
    name = name.strip().lower().capitalize()
    if not name.isalpha() or len(name) < 2 :
        print("\nInvalid input type. Please try again")
        name = ""
        continue
    else: 
        user1.update({"name" : name})
        break

while surname == "" :
    try :
        surname = str(input("\nEnter your surname: "))
        surname = surname.strip().lower().capitalize()
        if not surname.isalpha() or len(surname) < 2 :
            raise ValueError
    except ValueError :
        print("\nInvalid input type. Please try again")
        surname = ""
        continue
    else :
        user1.update({"surname" : surname})
        break
    
while birth_date == "" :
    print("\nEnter your date of birth below ")
    try :
        year = int(input('- year (yyyy): '))
        month = int(input('- month (mm): '))
        day = int(input('- day (dd): '))
        birth_date = date(year, month, day)
    except ValueError as er_message:
        print(f"""\nInvalid input type. Please try again
        Error detail: {er_message} """)
        birth_date = ""
        continue
    else :
        user1.update({"birth_date" : birth_date})
        break

while cell_number == "" :
    try :
        cell_number = int(input("\nEnter your mobile number: "))
        if len(str(cell_number)) != 12 :
            raise Exception
        elif not str(cell_number).isnumeric :
            raise ValueError
    except ValueError :
        print("\nInvalid input type. Only numeric values are allowed. Please try again")
        cell_number = ""
        continue
    except Exception :
        print("\nMobile number has to contain 12 character including country code. Please try again")
        cell_number = ""
        continue
    else :
        cell_number = str(cell_number)
        user1.update({"cell_number" : cell_number})
        break
    
while e_mail == "" :
    try :
        e_mail = (input("\nEnter your e-mail address: "))
        e_mail = e_mail.strip().lower()
        mailcheck = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
        def validate_email_syntax(e_mail):
            if not re.fullmatch(mailcheck, e_mail):
                raise Exception
        #if len(e_mail) < 5 or e_mail.find("@") == "-1" or e_mail.find(".") == "-1":
            #raise Exception
    except Exception :
        print("\nInvalid e-mail address. Please try again")
        e_mail = ""
        continue
    else :
        user1.update({"e_mail" : e_mail})
        break

while country == "" :
    try :
        country = str(input("Enter your country: "))
        country = country.strip().lower().capitalize()
        if not country.isalpha() or len(surname) < 3 :
            raise ValueError
    except ValueError :
        print("\nInvalid input type. Please try again")
        country = ""
        continue
    else :
        user1.update({"country" : country})
        break

while programming_languages == "":
    try : 
        programming_languages = str(input("Enter the programming languages you know (If there is none, please write N/A): "))
        programming_languages = programming_languages.strip().lower()
        if len(programming_languages) < 3 :
            raise Exception
    except Exception :
        print("\nInvalid input type. Please try again")
        programming_languages = ""
        continue
    else :
        user1.update({"programming_languages" : programming_languages})
        break
 
print("Thank you! Application form is completed.")
print("""Your user name: {user_name}
Summary of your form: {user1} """)
f"user_{name}{surname}" = user1