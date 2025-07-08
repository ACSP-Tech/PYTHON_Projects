#objective:  A basic calculator that remembers past results.

cal_dict = {
    "operation" : [],
    "result" : []
}


menu = ["1. add", "2. subtract", "3. Multiply", "4. Divide", "5. View History", "6. Exit"]

username = input("please enter a username below to kickstart your calculator with history platform: \n").strip().lower()

def calculator_history(cal_dict):
    while True:
        try:
            num1 = float(input(f"Welcome to {username} calaculator with history \nEnter the first number below \n"))
            num2 = float(input("\nEnter the second number below \n"))
        except ValueError:
            print("please don't enter any other data types aside from a number or an integer, you are been prompted to restart your current entry \n")
            continue
        for menulist in menu:
                print()
                print(menulist)
        try:    
            #asking user for what they want to do next
            choice = int(input(f"\nplease choose what you would like to do with {num1} and {num2} from the options above \n"))
        except:
            print("invalid input. Please retart and enter a number from 1 to 4 from the menu")
            continue
        #creating an if condition and treating  each options appropriately
        if choice == 1:
            operations = f"{num1} + {num2}"
            results = num1 + num2
            print(f"\nThe result of {num1} and {num2} operation is {results}")
            cal_dict["operation"].append(operations)
            cal_dict['result'].append(results)
            repeat = input("would you like to perform another operation? Type(Enter) \nor Would youlike to exit the app completely Type(Exit) \n").strip().lower()
            if repeat == "exit":
                break    
            elif repeat == "enter":
                continue
            else:
                print(f"I can't understand {repeat}, you are now been prompted to enter a new operation")  
                continue
        elif choice == 2:
            operations = f"{num1} - {num2}"
            results = num1 - num2
            print(f"\n{results}")
            cal_dict["operation"].append(operations)
            cal_dict['result'].append(results)
            repeat = input("would you like to perform another operation? Type(Enter) \n or Would youlike to exit the app completely Type(Exit) \n").strip().lower()
            if repeat == "exit":
                break    
            elif repeat == "enter":
                continue
            else:
                print(f"I can't understand {repeat}, you are now been prompted to enter a new operation")  
                continue
        elif choice == 3:
            operations = f"{num1} * {num2}"
            results = num1 * num2
            print(f"\n{results}")
            cal_dict["operation"].append(operations)
            cal_dict['result'].append(results)
            repeat = input("would you like to perform another operation? Type(Enter) \n or Would youlike to exit the app completely Type(Exit) \n").strip().lower()
            if repeat == "exit":
                break    
            elif repeat == "enter":
                continue
            else:
                print(f"I can't understand {repeat}, you are now been prompted to enter a new operation")  
                continue
        elif choice == 4:
            operations = f"{num1} / {num2}"
            try:
                results = num1 / num2
            except ZeroDivisionError:
                print("you are attempt to divide a number by zero which will cause an error, you will now be prompted to restart \n")
                continue
            print(f"\n{results}")
            cal_dict["operation"].append(operations)
            cal_dict['result'].append(results)
            repeat = input("would you like to perform another operation? Type(Enter) \n or Would youlike to exit the app completely Type(Exit) \n").strip().lower()
            if repeat == "exit":
                break    
            elif repeat == "enter":
                continue
            else:
                print(f"I can't understand {repeat}, you are now been prompted to enter a new operation")  
                continue
        elif choice == 5:
            import pandas as pd
            a = pd.DataFrame(cal_dict)
            print(a)
            repeat = input("would you like to perform another operation? Type(Enter) \n or Would youlike to exit the app completely Type(Exit) \n").strip().lower()
            if repeat == "exit":
                break    
            elif repeat == "enter":
                continue
            else:
                print(f"I can't understand {repeat}, you are now been prompted to enter a new operation")  
                continue
        elif choice == 6:
            break
        else:
            print(f"out of range value as {choice}. Please retart and enter a number from 1 to 6 from as the operator from the list \n")
            continue
    import pandas as pd
    a = pd.DataFrame(cal_dict)
    print(f"you have been exited successfully from the app, here is your calculation for today \n{a}")
    return cal_dict

cal_with_hist = calculator_history(cal_dict)

dict_cal = cal_with_hist

while True:
    delete_account_info_prompt = input("Would you like to exit the app completely(you will lose all your operation info)Type(Yes), \nor would you like to continue another operation at a later time Type(Continue) \n").strip().lower()
    if delete_account_info_prompt ==  "continue":
        wait_time = input("whenever you are ready to continue Type(Yes), \nif you change your mind and would like to exit the app(lose all input info) Type(No) \n").strip().lower()
        if wait_time == "yes":
           daily_exp_tracker_two = calculator_history(dict_cal)
        elif wait_time == "No":
            break
        else:
            print("I can't undertanding your input, you are now been prompted again")
            continue
    elif delete_account_info_prompt ==  "yes":
        break
    else:
        print("invalid input, you are now been prompted again")
        continue