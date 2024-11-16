class CoffeeMaker():
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }

    def report(self):
        print(f"Water: {self.resources['water']}")
        print(f"Milk: {self.resources['milk']}")
        print(f"Coffee: {self.resources['coffee']}")

    def is_resource_sufficient(self, drink):
        for resource in self.resources:
            if resource in drink.ingredients:
                if self.resources[resource] < drink.ingredients[resource]:
                    print(f"Sorry there is not enough {resource}")
                    return False
                else: 
                    return True
    
    def make_coffee(self, order):
        for resource in self.resources:
                if resource in order.ingredients:
                   self.resources[resource] -= order.ingredients[resource]
        print("Here is your latte. Enjoy!")
        