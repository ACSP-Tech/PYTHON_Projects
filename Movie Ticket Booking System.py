#objective: Manage ticket booking for a cinema.

import pandas as pd

movie_df = {
    "movie_name" : ["my love from another star", "blood sisters", "kaiju"],
    "available_seat" : [10, 6, 9],
    "ticket_price" : [4500, 5000, 3500]
}


menu = ["1. book a ticket", "2. view movies and seats", "3. Exit"]

def movie_cinema(movie_df):
    while True:
        a = pd.DataFrame(movie_df)
        print(a)
        print("what would you like to do next?")
        for menulist in menu:
            print(menulist)
        try:
            choice = int(input("Kindly make a voice from the option above Type an integer from 1 to 3 \n"))
        except:
            print("please type an integer from 1 to 3")
            continue
        if choice == 1:
            try:
                movie = input("enter a movie name from the already displayed table \n").strip().lower()
                seat = int(input("enter the integer number of seat ticket to book for the event \n"))
            except:
                print("there is an error with your input, you are now been prompted to restart, please follow the instructions \n")
                continue
            movie_name = [name for name in movie_df["movie_name"]]
            if movie in movie_name:
                index = movie_name.index(movie)
                seat_df = movie_df["available_seat"][index]
                if seat_df > seat:
                    movie_df["available_seat"][index] = seat_df - seat
                    repeat = input("Ticket booked successfully! \nThank you for your patronage!!! \nwould you like to perform another operation?, enter yes or no \n").strip().lower()
                    if repeat == "yes":
                        continue
                    elif repeat == "no":
                        exit = input("would you like to exit the app").strip().lower()
                        if exit == "Yes":
                            return movie_df
                            break
                        elif exit == "no":
                            continue
                        else:
                            continue
                    else:
                        continue
                elif seat_df == seat:
                    movie_df["available_seat"][index] = seat_df - seat
                    repeat = input("Ticket booked successfully! \nThank you for your patronage!!! \nwould you like to perform another operation?, enter yes or no \n").strip().lower()
                    if repeat == "yes":
                        continue
                    elif repeat == "no":
                        exit = input("would you like to exit the app").strip().lower()
                        if exit == "Yes":
                            return movie_df
                            break
                        elif exit == "no":
                            continue
                        else:
                            continue
                    else:
                        continue
                else:
                    print("seat value out of range, please restart")
                    continue
            else:
                print("invalid movie name, kindly restart")
                continue
        elif choice == 2:
            continue
        elif choice == 3:
            break
        else:
            print("invalid input, please make an integer choice from 1 to 3")
    return movie_df

movie_ticket_system = movie_cinema(movie_df)

dict_movie = movie_ticket_system 