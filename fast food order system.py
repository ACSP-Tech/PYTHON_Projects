#objective: A fast-food ordering system that supports multiple customers.

#defining the list of items to be displayed to user
food_item = ["1. Burger", "2. Fries", "3. Drink"]

#defining variables to be used in the loop and summary
customer = 0
number = 1

bill_fries = 0
bill_drink = 0
bill_burger = 0
total_burger_bill = 0
total_fries_bill = 0
total_drink_bill= 0
discount = 0

#creating an indefinite loop that stop on exit keyword
while True:
    # displaying the food items to users to make a choice from
    for item in food_item:
        print()
        print(item)
    
    #handling value errors
    try:
        #asking for user choice, creating an if statement that stores the bill for that particular customer
        food_name = input("Kindly enter the food name needed from the option above: \n")
        if food_name == "Burger":
            quantity = int(input(f"How many {food_name} do you want?: "))
            bill_burger = quantity * 5
            total_burger_bill += bill_burger
        elif food_name == "Fries":
            quantity = int(input(f"How many {food_name} do you want?: "))
            bill_fries = quantity * 2
            total_fries_bill += bill_fries
        elif food_name == "Drink":
            quantity = int(input(f"How many {food_name} do you want?: "))
            bill_drink = quantity * 1.5
            total_drink_bill += bill_drink
        #handling choice outside the menu
        else:
            print("Invalid food_name input. Please enter a food name from the options.")
            continue
    except ValueError:
        print("I can't understand your input, please start again and choose from the menu below: ")
        continue 
    #asking user if he would like to serve another customer
    repeat = input("Would you like to serve another food item to this same customer? (Yes/No?): ")
    #repeat the sequence is yes
    if repeat == "Yes":
            continue
    #display the bill for that particular customer once done serving him
    elif repeat == "No":
        total_bill = total_burger_bill + total_fries_bill + total_drink_bill
        new_bill = total_bill
        if total_bill > 20:
            discount = total_bill * 0.1
            new_bill = total_bill - discount
        print(f"""the {number} customer bill summary is: \n
              Burgers: ${total_burger_bill} \n
              Fries: ${total_fries_bill} \n
              Drinks: ${total_drink_bill} \n
              Discount: ${discount} \n
              Total bill for {number} customer is ${new_bill}""")
        customer += 1
        number += 1
        #asking user if they would like to exit the app, or serve another customer? 
        exit = input(f"would you like to serve another no.{number} customer(type yes) or exit the app(type Exit) (Yes/Exit): ")
        #resetting the bill if user choose to serve another customer
        if exit == "Yes":
            total_burger_bill = 0
            total_fries_bill = 0
            total_drink_bill = 0
            continue
        #exiting, displaying total customer served
        elif exit == "Exit":
            print(f"total number of customer served for this session is {customer}")
            break
        #handling input outside option
        else:
            print("I can't understand your input, you are now serving another customer. please choose from the menu below: ")
            continue
    #handling user input outside option  
    else:
        print("I can't understand your input, please start again and choose from the menu below: ")
        continue