class InvalidItemType(Exception):
    def __init__(self, item_type):
        self.item_type = item_type

    def call(self):
        print(f"Sorry, we don't sell {self.item_type}s.")


class OutOFStock(Exception):
    def __init__(self, item_type):
        self.item_type = item_type
        
    def call(self):
        print(f"Sorry, {self.item_type}s are out of stock.")


class OperationDenied(Exception):
    def call(self):
        print(f"Sorry, we couldn't process the requested operation. Please try again.")
