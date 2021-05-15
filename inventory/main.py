from inventory import *

if __name__ == '__main__':
    inv = Inventory(
        Item('phone', 3), 
        Item('laptop', 5)
        )

    item_type = 'phone'

    try:
        num_left = inv.purchase(item_type)
    
    except InvalidItemType:
        print(f"Sorry, we don't sell {item_type}s.")
    
    except OutOFStock:
        print(f"Sorry, {item_type}s are out of stock.")

    except OperationDenied:
        # another part of the program is using this item
        print(f"Sorry, we couldn't process your purchase. Please try again.")

    except:
        print(f"An unexpected error has occurred.")
    
    else:
        print(f"Purchase complete. There are {num_left} {item_type}s left.")
    
    finally:
        print("Execution continues regardless of errors.")
