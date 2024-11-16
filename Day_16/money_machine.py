class MoneyMachine():
    def __init__(self):
        self.profit = 0
        self.CURRENCY = '$'
        self.money_received = 0
        
    
    def report(self):
        print(f"Money: {self.CURRENCY}{self.profit}")
    
    def process_coins(self):
        quarters = int(input("Quarters: "))
        dimes = int(input("Dimes: "))
        nickles= int(input("Nickles: "))
        pennies= int(input("Pennies: "))
        self.money_received = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)
        
        return self.money_received
    
    def make_payment(self, cost):
        self.process_coins()

        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is ${change} dollars in change.")
            self.profit += cost
            return True
        else:
            return False
