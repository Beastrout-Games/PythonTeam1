import inventory as inv
from exceptions import *

def menu(stock):
    print("Welcome to out little shop! We offer:")
    for i in stock.items:
        print(i.item_type)

    while True:

        item_type = input("Enter your selection: ")

        try:
            num_left = stock.purchase(item_type)
        
        except (InvalidItemType, OutOfStock, OperationDenied) as ex:
            ex.call()
            
        except:
            print(f"An unexpected error has occurred.")
        
        else:
            print(f"Purchase complete.")
        
        finally:
            again = input("Would you like to purchase anything else? (y/Y) ")

            if again not in ['yes', 'Yes', 'y', 'Y']:
                print("Thank you for your visit at our store!")
                break
