class item():
    
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.locked = False

class inventory():
    sklad=[]

    def __init__(self):
        pass
    
    def add_inventory_item(self, some_item:item):
        self.sklad.append(item)

    #some_item is like a pointer in C to a class
    def lock(self, some_item:item):
        some_item.locked = True 
    
    def unlock(self, some_item:item):
        some_item.locked = False

    def purchase(self, some_item:item): 
        pass
    
    def print_inventory(self):
        print (self.sklad[i].name for i in self.sklad)
        
i1 = item("kolio", 1, 2)
i2 = item("daka", 1, 2)
i3 = item("achka", 1, 2)
inv = inventory()
inv.add_inventory_item(i1)
inv.add_inventory_item(i2)
inv.add_inventory_item(i3)
inv.print_inventory()
#inv.lock(inv.sklad[0])

#for i in range(0,3):
    #print(inv.sklad[i].locked
