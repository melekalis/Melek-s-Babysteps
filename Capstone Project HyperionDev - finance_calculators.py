import math
investment = "to calculate the amount of interest you'll earn on your investment"
bond = "to calculate the amount you'll have to pay on a home loan"

print("Welcome! You can calculate either 'investment' or 'bond' amount in this page.")

print(f"\ninvestment: This option is {investment} \nbond: This option is {bond}")

user_answer = ""

while user_answer == "" :
    user_answer = str(input("\nPlease, enter either 'investment' or 'bond' from the menu above to proceed: "))
    user_answer = str(user_answer.strip(""))
    user_answer = str(user_answer.lower())

    user_answer_options = ["investment", "bond"]

    while user_answer not in user_answer_options :
        print("!!! Invalid answer !!!")
        user_answer = str(input("\nPlease, enter either 'investment' or 'bond' from the menu above to proceed: "))
        user_answer = str(user_answer.strip(""))
        user_answer = str(user_answer.lower())


    if user_answer == "investment" :
        deposit_p = int(input("\nPlease enter the amount of money: "))
        interest_rate = int(input("Please enter the preferred interest rate: "))
        r = interest_rate / 100
        t = int(input("Please enter the number of years you plan on investing: "))
        interest = ""
        
        while interest == "" :
            interest = str(input("Please enter the type of interest. Enter either 'simple' or 'compound': "))
            interest = str(interest.strip(""))
            interest = str(interest.lower())
            
            interest_options = ["simple", "compound"]
            
            while interest not in interest_options :
                print("!!! Invalid interest type !!!")
                interest = str(input("Please enter the type of interest. Enter either 'simple' or 'compound': "))
                interest = str(interest.strip(""))
                interest = str(interest.lower())
        
            if interest == "simple" :
                A = float(deposit_p *(1 + r*t))
                investment = float(A - deposit_p)
                investment = round(investment, 2)
                print(f"\nThe amount of interest you'll earn is '{investment}' via simple interest.")
                break

            elif interest == "compound" :
                A = float(deposit_p * math.pow((1+r),t))
                investment = float(A - deposit_p)
                investment = round(investment, 2)
                print(f"\nThe amount of interest you'll earn is '{investment}' via compound interest.")
                break

    elif user_answer == "bond" :
        P_present_value = float(input("\nPlease enter the present value of your house: "))
        interest_rate = int(input("Please enter the preferred interest rate: "))
        interest_rate = interest_rate / 100
        i = float(interest_rate / 12)
        n_months = int(input("Please enter the number of months you plan to take to repay the bond : "))
        
        repayment = (i * P_present_value)/(1 - (1 + i)**(-n_months))
        repayment = round(repayment, 2)
        
        print(f"\nThe amount you'll have to pay on a home loan is '{repayment}'.")
        break