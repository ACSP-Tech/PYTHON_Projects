#objective: Simulate a mini-store system.
import pandas as pd

shop_df = pd.DataFrame({
    "item_name" : ["rice_1_cup", "beans_1_cup", "garri_1_cup", "fish", "red_oil_1_bottle", "groundnut_oil_1_bottle", "crayfish_1_stachet", "maggi_1_packet", "onions", "dark_soy_sauce", "oyeser_sauce", "spagehtti", "pepper", "meat_1_kilo", "chicken_1_kilo", "liver_1_kilo", "tomatoes_1_pcs", "green_onions_1_pcs"],
    "price" : [600, 800, 500, 4500, 3500, 4000,  2500, 1500, 200, 1500, 1500, 1000, 200, 5000, 6000, 3000, 50, 50]
})

cart_dict = {
    "item_name" : [],
    "quantity" : [],
    "price" : [],
    "line_total": [] 
}

username = input("please enter a username below to kickstart your calculator shopping cart system platform: \n").strip().lower()

def shop_cart_sys(cart_dict):
    while True:
        print(f"Welcome to {username} shooping cart system")
        print(shop_df)
        try:
            add_to_cart = input("would you like to add an item to your cart? Type(Yes/No) \n").strip().lower()
            if add_to_cart == "yes": 
                item = input("kindly enter the item name from the table already displayed above: \n").strip().lower()
                if item in shop_df['item_name'].values:
                    quantity = int(input(f"How many {item} quantity would you like to buy? \n")) #
                    price = shop_df.loc[shop_df['item_name'] == item, 'price'].values[0]
                    line_total = quantity * price
                    cart_dict['item_name'].append(item)
                    cart_dict['quantity'].append(quantity)
                    cart_dict['price'].append(price)
                    cart_dict['line_total'].append(line_total)

                    repeat = input("item has been added successfully! \nWould you like to view cart Type(view) \nor would you like to add another item to your cart Type(continue) \n").strip().lower()
                    if repeat == "continue":
                        continue
                    elif repeat == "view":
                        a = pd.DataFrame(cart_dict)
                        print(a)
                        total_bill = a["line_total"].sum()
                        print(f"your total bill is {total_bill}")
                        cart_option = input(f"""Type in what you eould like to do next 
                                            \nWould you like to remove an item from your cart type(remove) 
                                            \nDo you want to clear all items in your cart type(clear)
                                            \nDO you want to process your cart and exit the app type(exit) 
                                            \nDo you want to add items to your cart type(add) \n""").strip().lower()
                        if cart_option == "add":
                            continue 
                        elif cart_option == "remove":
                            item_remove = input("Enter the item name from your cart you would like to remove: \n").strip().lower()
                            remove_item_from_cart(cart_dict, item_remove)
                            print(f"{item_remove} has been removed successfully from your cart!")
                            a = pd.DataFrame(cart_dict)
                            print(a)
                            total_bill = a["line_total"].sum()
                            print(f"your new total bill is {total_bill}")
                            continue
                        elif cart_option == "clear":
                            clear = input("Warning!!! you are about to delete all the items in your cart, would you like to proceed? Type(Yes/No): \n").strip().lower()
                            if clear == "yes":
                                for key in cart_dict:
                                    cart_dict[key].clear()
                                print(f" all the item in your cart has been successfully deleted, you now been prompted to restart")
                                continue
                            elif clear == "No":
                                print("Alright, you are now been prompted to restart \n")
                                continue
                            else:
                                print("I can't understand your input, you are expected to choose either Yes or No, you are now been prompted to restart")
                                continue
                        elif cart_option == "exit":
                            a = pd.DataFrame(cart_dict)
                            print(a)
                            total_bill = a["line_total"].sum()
                            print(f"your total bill is {total_bill}")
                            print(f"your cart items below is now been processed! \nyour order will be delivered to your doorstep shortly \n Thanks for shopping with us")
                            break 
                        else:
                            print("I can't understand your input, you are expected to choose either clear, remove or exit, you are now been prompted to restart")
                            continue
                    else:
                        print(f"invalid input, please input either continue or view, you are now been prompted to restart")
                        continue
                else:
                    print("please choose an item from our already listed items, you are now been prompted to restart \n")
                    continue
            elif add_to_cart == "no":
                cart_option = input(f"""Type in what you eould like to do next 
                                            \nWould you like to remove an item from your cart type(remove) 
                                            \nDo you want to clear all items in your cart type(clear)
                                            \nDO you want to process your cart and exit the app type(exit) 
                                            \nDo you want to add items to your cart type(add) \n""").strip().lower()
                if cart_option == "add":
                    continue 
                elif cart_option == "remove":
                    item_remove = input("Enter the item name from your cart you would like to remove: \n").strip().lower()
                    remove_item_from_cart(cart_dict, item_remove)
                    print(f"{item_remove} has been removed successfully from your cart!")
                    a = pd.DataFrame(cart_dict)
                    print(a)
                    total_bill = a["line_total"].sum()
                    print(f"your new total bill is {total_bill}")
                    continue
                elif cart_option == "clear":
                    clear = input("Warning!!! you are about to delete all the items in your cart, would you like to proceed? Type(Yes/No): \n").strip().lower()
                    if clear == "yes":
                        for key in cart_dict:
                            cart_dict[key].clear()
                        print(f" all the item in your cart has been successfully deleted, you now been prompted to restart")
                        continue
                    elif clear == "No":
                        print("Alright, you are now been prompted to restart \n")
                        continue
                    else:
                        print("I can't understand your input, you are expected to choose either Yes or No, you are now been prompted to restart")
                        continue
                elif cart_option == "exit":
                    a = pd.DataFrame(cart_dict)
                    print(a)
                    total_bill = a["line_total"].sum()
                    print(f"your total bill is {total_bill}")
                    print(f"your cart items below is now been processed! \nyour order will be delivered to your doorstep shortly \n Thanks for shopping with us")
                    break 
                else:
                    print("I can't understand your input, you are expected to choose either clear, remove or exit, you are now been prompted to restart")
                    continue
            else:
                print("enter yes or no")
                continue
        except:
            print("there is something wrong with your add to cart input, you are been prompted to resart")
    return cart_dict


def remove_item_from_cart(cart_dict, item_to_remove):
    try:
        index = cart_dict["item_name"].index(item_to_remove)
        for key in cart_dict:
            cart_dict[key].pop(index)
        print(f"{item_to_remove} has been removed successfully from your cart!")
    except ValueError:
        print(f"Item {item_to_remove} not found in cart. Please check the spelling or view your cart before trying again.")

cart_shop_system = shop_cart_sys(cart_dict)

dict_cart = cart_shop_system 