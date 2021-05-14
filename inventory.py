# https://www.programiz.com/python-programming/user-defined-exception

class InvalidItemType(Exception):
    pass

class OutOfStock(Exception):
    pass


class Item:
    def __init__(self, item_type, quantity, price):
        self.item_type = item_type
        self.quantity = quantity
        self.price = price
        self.locked = False


class Inventory:
    warehouse = [Item('phone', 2, 300.00)]

    def find(self, item_type):
        for item in self.warehouse:
            if item.item_type == item_type:
                return item

        raise InvalidItemType


    def lock(self, item_type):
        try:
            item = self.find(item_type)
        except:
            pass
        else:
            item.locked = True


    def unlock(self, item_type):
        try:
            item = self.find(item_type)
        except:
            pass
        else:
            item.locked = False

    def add_inventory_item(self, some_item: Item):
        found = False

        for i in self.warehouse:
            if i.name == some_item.name:
                i.quantity += some_item.quantity
                found = True
                break

        if not found:
            self.warehouse.append(some_item)


    def purchase(self, item_type, quantity):
        item = self.find(item_type)
        if not item:
            raise InvalidItemType
        if item.quantity <= 0:
            raise OutOfStock
        
        item.quantity -= 1
        return item.quantity

    def print_inventory(self):
        for i in self.warehouse:
            print(f"Name: {i.item_type} Quantity: {i.quantity} Price: {i.price} Status: {i.locked}")

    def check_quantity(self,item_type):
        found = False

        for i in self.warehouse:
            if i.item_type == item_type:
                return i.quantity



# i1 = Item("domati", 1, 2)
# i2 = Item("banani", 1, 2)
# i3 = Item("krastavici", 1, 2)
# i4 = Item("banani", 10, 2)


# #inv = Invetory()

# inv.add_inventory_item(i1)
# inv.add_inventory_item(i2)
# inv.add_inventory_item(i3)
# inv.add_inventory_item(i4)
# #inv.print_inventory()

# inv.lock("achka")
# #inv.print_inventory()
# inv.unlock("achkaaa")
# #inv.print_inventory()

def main():
    item_type = 'phone'
    inv = Inventory()
    
    inv.lock(item_type)

    try:
        num_left = inv.purchase(item_type, 1)
    except InvalidItemType:
        print("Sorry, we don't sell {}".format(item_type))
    except OutOfStock:
        print("Sorry, that item is out of stock.")
    else:
        print(f"Purchase complete. There are {num_left} {item_type}s left")
    finally:
        inv.unlock(item_type)

if __name__ == '__main__':
    main()
