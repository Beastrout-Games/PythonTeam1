class InvalidItemType(Exception):
    pass

class OutOFStock(Exception):
    pass

class OperationDenied(Exception):
    pass


class Item(object):
    def __init__(self, item_type, quantity) -> None:
        self.item_type = item_type
        self.quantity = quantity
        self.locked = False


class Inventory(object):
    def __init__(self, *items: Item) -> None:
        self.items = items
    

    def find(self, item_type):
        for item in self.items:
            if item.item_type == item_type:
                return item
        else:
            raise InvalidItemType(item_type)


    def lock(self, item_type):
        self.find(item_type).locked = True


    def unlock(self, item_type):
        self.find(item_type).locked = False
    

    def purchase(self, item_type):
        item = self.find(item_type)
        
        if item.locked:
            raise OperationDenied(item_type)
        
        elif item.quantity <= 0:
            raise OutOFStock(item_type)
        
        self.lock(item_type)
        item.quantity -= 1
        # do other operations, maybe
        self.unlock(item_type)

        return item.quantity


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
