from inventory import *

if __name__ == '__main__':
    inv = Inventory(
        Item('phone', 3), 
        Item('laptop', 0)
        )
    
    #item_type = input("What d'ya wanna buy, bro?")

    item_type = 'car'

    try:
        num_left = inv.purchase(item_type)
    
    except (InvalidItemType, OutOfStock, OperationDenied) as ex:
        ex.call()
        
    except:
        print(f"An unexpected error has occurred.")
    
    else:
        print(f"Purchase complete. There are {num_left} {item_type}s left.")
    
    finally:
        print("Execution continues regardless of errors.")
