#objective: Help users track their daily expenses.
import pandas as pd

daily_exp = {
            'item': [],
            'amount': []
        }

menu = ["1. Add expense", "2. view all expense", "3. total and average", "4. Exit"]

username = input("please enter a username below to kickstart your student management platform: \n")


def expense_tracker(daily_exp):
    while True:

        for menulist in menu:
            print()
            print(menulist)
        try:     
            #asking user for what they want to do next
            choice = int(input(f"Welcome to {username} Simple Expense Tracker \nMake an integer choice between 1 to 4 from the menu above: "))
        except ValueError:
                    print(f"invalid value as {choice}. Please retart and enter a number from 1 to 4 from the menu").strip().lower()
                    continue
        #creating an if condition and treating  each options appropriately
        if choice == 1:
            try:
                description = input(f" Kindly enter the description of the expenses, this stores in lowercase: \n").strip().lower()
                amount = float(input(f"Kindly enter the amount spent on {description} expense \n"))

                daily_exp['item'].append(description)
                daily_exp['amount'].append(amount)

                repeat = input("would you like to Enter another expenses record or perform aother menu operation? Type(Enter) \n or Would youlike to exit the app completely Type(Exit) \n").strip().lower()
                if repeat == "exit":
                    break    
                elif repeat == "enter":
                    continue
                else:
                    print(f"I can't understand {repeat}, you are now been prompted to enter a new expense record")  
                    continue 
            except ValueError:
                print(f"Kindly restart {description} expense record entry and enter a number for the amount")
                continue
            except:
                print(f"Error with the code, kindly restart {description} expense record entry")
                continue
        elif choice == 2:
            a = pd.DataFrame(daily_exp)
            print(a)
            repeat = input("Would you like to exit the app? Type(Exit) \nOr would you like to Enter another expenses record or perform aother menu operation? Type(Enter): \n").strip().lower()
            if repeat == "exit":
                break
            elif repeat == "enter":
                continue
            else:
                print(f"I can't understand {repeat}, you are now been prompted to enter a new expense record")
                continue
        elif choice == 3:
            a = pd.DataFrame(daily_exp)
            total_amount = a["amount"].sum()
            average_amount = a["amount"].mean()
            print(f"""
                  total: {total_amount}
                  average_amount: {average_amount}
                  """)
            repeat = input("Would you like to exit the app? Type(Exit) \nOr would you like to Enter another expenses record or perform aother menu operation? Type(Enter): \n").strip().lower()
            if repeat == "exit":
                break
            elif repeat == "enter":
                continue
            else:
                print(f"I can't understand {repeat}, you are now been prompted to enter a new expense record")
                continue
        elif choice == 4:
            break
        else:
            print(f"out of range value as {choice}. Please retart and enter a number from 1 to 4 from the menu")
            continue
    a = pd.DataFrame(daily_exp)
    print(a)
    return daily_exp

daily_exp_tracker = expense_tracker(daily_exp)

dict_exp = daily_exp_tracker

while True:
    delete_account_info_prompt = input("Would you like to exit the app completely(you will lose all your inputed info)Type(Yes), \nor would you like to continue input at a later time Type(Continue) \n")
    if delete_account_info_prompt ==  "Continue":
        wait_time = input("whenever you are ready to continue Type(Yes), \nif you change your mind and would like to exit the app(lose all input info) Type(No) \n")
        if wait_time == "yes":
           daily_exp_tracker_two = expense_tracker(dict_exp)
        elif wait_time == "No":
            break
        else:
            print("I can't undertanding your input, you are now been prompted again")
            continue
    elif delete_account_info_prompt ==  "Yes":
        break
    else:
        print("invalid input, you are now been prompted again")
        continue