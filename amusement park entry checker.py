#objective: Check multiple visitors' ticket prices.
#constructing an indefinite loop that only break on a keyword
while True:
    # asking user for vistor input and storing it in a variable
    visitor_name = input("kindly type in the visitor name or type Done to exit app: ")
    #constructing an if condition based on the user input
    if visitor_name == "Done" or visitor_name == "done":
        #keyword to break is done, break if the user input is done
        break
    #in case of other string, takes and store it as vistor name
    else:
        #try and except to handle other data type inout error in age
        try:
            #ask user for age and stores it in the age variable
            age = int(input(f"Enter an integer below \nwhat is {visitor_name} age?  \n"))
            #constructing different if condition and assigning ticket fee based on the condition that is meet
            if 0 <= age < 5:
                ticket_fee = 0
            elif 5 <= age <= 17:
                ticket_fee = 5
            elif 18 <= age <= 59:
                ticket_fee = 10
            elif age >= 60:
                ticket_fee = 7
            #in case of a negative age which is an invalid value, restart sequence
            else:
                print("Restart, please don't input a negative age")
                continue
        except ValueError:
            print("I don't understand your input, please input an integer in the age, Kindly restart")
            continue
        #collecting user input on if they have a coupon
        coupon = input("Do you have a coupon: Enter (Yes/No)")
        #applying a 20% discount if coupon exist
        if coupon == "Yes" or coupon == "yes":
            #calculating the discount
            final_price = ticket_fee - (ticket_fee * 0.2)
            #displaying final price
            print(f"the ticket price for {visitor_name} is ${final_price}")
        #handling the situation where user does not have a coupon
        elif coupon == "No" or coupon == "no":
            final_price = ticket_fee
            print(f"the ticket price for {visitor_name} is ${final_price}")
        #restarting the sequence if feedback for coupon is neither yes or no
        else:
            print("Kindly restart, please input Yes or No in the coupon question:")

                 


