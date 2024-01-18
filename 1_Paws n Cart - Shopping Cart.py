""" 
>> Background: Valentina has a special place in her heart for her animal companions. 
She frequently shops online for pet supplies and volunteers at a nearby animal shelter.

>> Challenge: Develop a shopping cart application, called Paws n Cart, for pet-related products 
to help manage your products and that can provide information on adoption centres and pet care advice.

>> Objective: Develop a program to:
    ○ Create a cart mechanism, using Strings or Lists, that will store different items.
    ○ Allow users to add and remove items from the cart.
    ○ Ensure that the cart is being displayed to the user clearly.
    ○ Calculate the total cost of the cart when requested by the user.
    ○ Allow the user to checkout when they are ready. """

# Firstly, list at least 5 available items with price here.
# Then create variables for total cost, cart item, basket price etc
# In this way, our product list and follow up variables are ready at the beginning.

prod_list = ["cat food", "dog food", "fish food", "cat toy", "bird nest", "dog toy", "bird food"]
stock_list = [1, 15, 8, 18, 9, 17, 10]
price_list = [9.90, 10.90, 6.90, 19.90, 20, 17.50, 4.90]

total_cost = 0
cart_item = 0
cart_list = []
basket_price_list = []
basket_stock_list = []

# Now, ask user choice among menu options.

print("""Welcome to Paws n Cart!\n---------------------------------------------------------------------------------------
This is your shopping cart:
---------------------------------------------------------------------------------------\n
Would you like to:""")

user_choice = ""

while user_choice == "" :
    print("""1. Add an item to your cart
2. Remove an item from your cart
3. View the total cost of your cart
4. Checkout \n""")

    user_choice = input("Please, enter the number of the option you would like to choose: ")

    user_choice_options = ["1", "2", "3", "4"]
    
    while user_choice not in user_choice_options :
        print("!!!Invalid answer!!!")
        user_choice = input("Please, enter the number of the option you would like to choose: ")

    if user_choice == "1" :
        print(f"""\nBrowse currently available procucts below : 
                1. {prod_list[0]} is £{price_list[0]} with {stock_list[0]} available stock
                2. {prod_list[1]} is £{price_list[1]} with {stock_list[1]} available stock
                3. {prod_list[2]} is £{price_list[2]} with {stock_list[2]} available stock
                4. {prod_list[3]} is £{price_list[3]} with {stock_list[3]} available stock
                5. {prod_list[4]} is £{price_list[4]} with {stock_list[4]} available stock
                6. {prod_list[5]} is £{price_list[5]} with {stock_list[5]} available stock
                7. {prod_list[6]} is £{price_list[6]} with {stock_list[6]} available stock""")
        
        user_prod = input("\nEnter the number of the item you would like to add to cart: ")

        user_prod_options = ["1", "2", "3", "4", "5", "6", "7"]

        while user_prod not in user_prod_options :
            print("!!!Invalid answer!!!")
            user_prod = input("Please, enter the number of the item you would like to add to cart: ")

        else :
            user_prod = int(user_prod)
            while int(stock_list[user_prod-1]) < 1 :
                print(f"""Sorry! '{prod_list[user_prod-1]}' is out of stock now. 
\nWhat would you like to:
    1. Try to add another product
    2. Return to main menu""")
                action = input("Enter the number of the option you would like to choose: ")
                action_list = ["1", "2"]
                while action not in action_list : 
                    print("!!!Invalid answer!!! ")
                    action = input("Enter the number of the option you would like to choose: ")

                if action == "1" :
                    user_prod = input("\nEnter the number of the item you would like to add to cart: ")
                    user_prod = int(user_prod)

                elif action == "2" : 
                    user_choice = ""
                    break
                
            else:
                print(f"\nA '{prod_list[user_prod-1]}' is added to cart!")
                stock_list[user_prod-1] -= 1
                total_cost += price_list[user_prod-1]
                cart_item += 1
                cart_list.append(prod_list[user_prod-1])
                basket_price_list.append(price_list[user_prod-1])
                basket_stock_list.append("1")
                print(f"""\n---------------------------------------------------------------------------------------
This is your shopping cart: """)
                for i in range(cart_item) :
                    print(f"{cart_list[i]}  ----->  {basket_price_list[i]}£  ----->  {basket_stock_list[i]} piece")
                if cart_item > 1 :
                    print(f"""\nSubtotal:
There are {cart_item} items in cart.
    ---------------------------------------------------------------------------------------\n""")
                elif cart_item == 0 : #This is product add menu. It is impossible to have 0 prod in cart but, I wrote this code in case of cover every possibility :D
                    print("\nYour cart is empty!")
                
                else :
                    print(f"""\nSubtotal:
There is {cart_item} item in cart.
    ---------------------------------------------------------------------------------------\n""")
                        
        print("\nWhat would you like to do now?")

        user_choice = ""
        continue
    
    elif user_choice == "2" :
        if cart_item == 0 :
            print("\nYour cart is already empty. Try another action.")
        else :
            print(f"""Your cart currently consists {cart_item} item.
This is your shopping cart: """)
            for i in range(cart_item) :
                print(f"{cart_list[i]}  ----->  {price_list[i]}£  ----->  {basket_stock_list[i]} piece")
            
            remove_item = input("\nEnter the 'item name' you would like to remove: ")
            remove_item.lower()
            remove_item.strip("")

            while remove_item not in cart_list:
                print("Invalid answer!")
                remove_item = input("\nEnter the item name you would like to remove: ")
                remove_item.lower()
                remove_item.strip("")
            else:
                p = prod_list.index(remove_item)
                stock_list[p] += 1
                total_cost -= price_list[p]
                cart_item -= 1

                i = cart_list.index(remove_item)
                cart_list.pop(i)
                basket_price_list.pop(i)
                basket_stock_list.pop(i)
            
                print(f"\nA '{remove_item}' has been removed from cart succesfully.")
                print(f"""\n---------------------------------------------------------------------------------------
This is your shopping cart: """)
                for i in range(cart_item) :
                    print(f"{cart_list[i]}  ----->  {basket_price_list[i]}£  ----->  {basket_stock_list[i]} piece")
                if cart_item > 1 :
                    print(f"""\nSubtotal:
There are {cart_item} items in cart.
    ---------------------------------------------------------------------------------------\n""")
                elif cart_item == 0 :
                    print("\nYour cart is empty!")
                
                else :
                    print(f"""\nSubtotal:
There is {cart_item} item in cart.
    ---------------------------------------------------------------------------------------\n""")

        print("\nWhat would you like to do now?")

        user_choice = ""
        continue

    elif user_choice == "3" :
        if cart_item == 0 :
            print("\nYour cart is empty. Try another action.")
        else :
            print(f"""---------------------------------------------------------------------------------------
The total cost of your shopping cart is £{round(total_cost, 2)}.
---------------------------------------------------------------------------------------""")
        
        print("\nWhat would you like to do now?")

        user_choice = ""
        continue

    elif user_choice == "4" :
        if cart_item == 0 :
            print("\nYour cart is empty. Thank you for visiting us.")
        else :
        # Exit from the program.
            print("Thank you for shopping with Paws n Cart")
            











