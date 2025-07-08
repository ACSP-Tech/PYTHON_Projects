#objective: Simulate a basic ATM system that allows a user to perform multiple banking operations.

fixed_acc_bal = 1000

#constructing the menu structure
menu = ["1. Check Balance", "2. Deposit", "3. Withdraw", "4. Exit"]

#creating an indefinite loop
while True:
    # listing  out the ATM options
    for menulist in menu:
        print()
        print(menulist)
    #asking user for what they want to do next
    choice = input("make an integer choice between 1 to 4 from the menu above: ")
    #creating an if condition and treating  each options appropriately
    if choice == "1" or choice == "Check Balance":
        print(f"your current balance is {fixed_acc_bal}")
        repeat = input("Would you like to perform another transaction?(Yes/No?): ")
        if repeat == "Yes":
            continue
        elif repeat == "No":
            print("Thank you for banking with Us! please take your card")
            break
        else:
            print("I can't understand your input, please choose from the menu below: ")
            continue

    elif choice == "2" or choice == "Deposit":
        try:
            deposit = float(input("please insert the amount you would like to deposit below: \n"))
            if deposit <= 0:
                print("Please enter a valid deposit amount.")
                continue
            fixed_acc_bal += deposit
            print(f"Deposit successful. New balance: ${fixed_acc_bal}")
        except ValueError:
            print("Invalid deposit amount! Please enter a number.")
        repeat = input("Would you like to perform another transaction?(Yes/No?): ")
        if repeat == "Yes":
            continue
        elif repeat == "No":
            print("Thank you for banking with Us! please take your card")
            break
        else:
            print("I can't understand your input, please choose from the menu below: ")
            continue

    elif choice == "3" or choice == "Withdraw":
        try:
            withdraw = float(input("please insert the amount you would like to withdraw below: \n"))
            if withdraw <= 0:
                print("Please enter a valid withdraw amount.")
                continue
            elif withdraw > fixed_acc_bal:
                print("Insufficient balance. Transaction cancelled.")
                continue
            fixed_acc_bal -= withdraw
            print(f"withdrawal successful. New balance: ${fixed_acc_bal}")
        except ValueError:
            print("Invalid withdraw amount! Please enter a number.")
        repeat = input("Would you like to perform another transaction?(Yes/No?): ")
        if repeat == "Yes":
            continue
        elif repeat == "No":
            print("Thank you for banking with Us! please take your card")
            break
        else:
            print("I can't understand your input, please choose from the menu below: ")
            continue

    elif choice == "4" or choice == "Exit":
        print(f"Thank you for banking with Us! \nyour final balnce is {fixed_acc_bal} \nGoodbye! please take your card")
        break
    #handling situation where users input an option outside the listed ones
    else:
        print("please check your input, and make a choice from the menu")
        continue