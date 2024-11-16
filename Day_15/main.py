MENU = {
      "espresso": {
          "ingredients": {
              "water": 50,
              "coffee": 10
          },
          "cost": 1.5
      },
      "latte": {
          "ingredients": {
              "water": 200,
              "milk": 150,
              "coffee": 24
          },
          "cost": 2.5
      },
      "cappucino": {
          "ingredients": {
              "water": 250,
              "milk": 100,
              "coffee": 24
          },
          "cost": 3.0
      },

}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

off = False
def start_machine():
    global off
    prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()

    def print_report(resources):
        for resource in resources:
            if resource == 'money':
                print(f"{resource.capitalize()}: ${"{:.2f}".format(resources[resource])}")
            else:
                print(f"{resource.capitalize()}: {resources[resource]}ml")

    def is_resources_sufficient(chosen_drink, resources):
        drink = MENU[chosen_drink]
        drink_ingredients = drink['ingredients']

        for resource in resources:
            if resource in drink_ingredients:
                if resources[resource] < drink_ingredients[resource]:
                    print(f"Sorry there is not enough {resource} for now, come back later.")
                    return False
                else: 
                    return True


    def process_coins():
        quarters = int(input("Quarters: "))
        dimes = int(input("Dimes: "))
        nickles= int(input("Nickles: "))
        pennies= int(input("Pennies: "))
        coins = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)
        
        return coins



    def is_transaction_successful(chosen_drink):
        if is_resources_sufficient(chosen_drink=prompt, resources=resources) == True:
            inserted_money = process_coins()
            drink = MENU[chosen_drink]
            cost = drink['cost']

            if inserted_money < cost:
                print("Sorry that\'s not enough money. Money refunded.")
                return False
            else:
                if inserted_money > cost:
                    change = inserted_money - cost
                    print(f"Here is ${"{:.2f}".format(change)} dollars in change.")
                resources['money'] += cost
                return True

    def make_coffee(chosen_drink):
        if is_transaction_successful(chosen_drink=chosen_drink) == True:
            drink = MENU[chosen_drink]
            drink_ingredients = drink['ingredients']

            for resource in resources:
                if resource in drink_ingredients:
                   resources[resource] -= drink_ingredients[resource]

            print("Here is your latte. Enjoy!")
            

    if prompt == "report":
        print_report(resources=resources)
    elif prompt == "off":
        off = True
    else:
        make_coffee(chosen_drink=prompt)

while not off:
    start_machine()