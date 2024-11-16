class MenuItem():
    def __init__(self, name, cost, ingredients):
        self.name = name
        self.cost = cost
        self.ingredients = ingredients


menu_item_1 = MenuItem('espresso', 1.5, {
    "water": 50,
    "coffee": 10
})
menu_item_2 = MenuItem('latte', 2.5, {
    "water": 200,
    "milk": 150,
    "coffee": 24
})
menu_item_3 = MenuItem('cappucino', 3.0, {
    "water": 250,
    "milk": 100,
    "coffee": 24
})

class Menu():
    def __init__(self):
        self.menu_items = {
            menu_item_1.name: menu_item_1,
            menu_item_2.name: menu_item_2,
            menu_item_3.name: menu_item_3
        }

    def get_items(self):
        return f"{menu_item_1.name}/{menu_item_2.name}/{menu_item_3.name}"
    
    def find_drink(self, order_name):
        if order_name in self.menu_items:
            return self.menu_items[order_name]
        else:
            return None