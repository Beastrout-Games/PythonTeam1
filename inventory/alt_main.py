import store.inventory as inv
from store.menu import menu

if __name__ == '__main__':
    devices = inv.Inventory(
        inv.Item('phone', 5),
        inv.Item('laptop', 10),
        inv.Item('tablet', 0)
        )

    menu(devices)