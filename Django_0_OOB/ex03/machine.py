import random
from beverages import HotBeverage , Coffee, Tea, Chocolate, Cappuccino


class CoffeeMachine:
    def __init__(self, name, status="working"):
        self.name = name
        self.status = status
        self.served_cups = 0
    
    class EmptyCup(HotBeverage):
        name = "empty cup"
        price = 0.90
        def description(self):
            return "An empty cup?! Gimme my money back!"
        
    
    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")
    
    def repair(self):
        self.status = "working"
        self.served_cups = 0
        

    def serve(self, beverage):
        if self.served_cups >= 10:
            self.status = "broken"
            raise CoffeeMachine.BrokenMachineException()
        else:
            self.served_cups += 1
            if random.randint(0, 1):
                return CoffeeMachine.EmptyCup()
            else:
                return beverage()


def test_coffee_machine():

    # Instantiate a coffee machine
    coffee_machine = CoffeeMachine("The Amazing Coffee Machine")
    print(coffee_machine.name)
    print("Status : ", coffee_machine.status)

# Dictionary of hot beverage classes
    hot_beverages = {"Tea": Tea, "Coffee": Coffee, "Chocolate": Chocolate, "Cappuccino": Cappuccino}
 
    # Serve 12 beverages
    try:
        for i in range(12):
            beverage_name = random.choice(list(hot_beverages.keys()))
            beverage_class = hot_beverages[beverage_name]
            result = coffee_machine.serve(beverage_class)
            print(f"Total served beverages: {coffee_machine.served_cups}")
            print(result)
    except CoffeeMachine.BrokenMachineException as e:
        print(e)
        # Repair the coffee machine
        coffee_machine.repair()
        print("The coffee machine has been repaired.")

    # Serve 12 beverages again
    try:
        for i in range(12):
            beverage_name = random.choice(list(hot_beverages.keys()))
            beverage_class = hot_beverages[beverage_name]
            result = coffee_machine.serve(beverage_class)
            print(f"Total served beverages: {coffee_machine.served_cups}")
            print(result)
    except CoffeeMachine.BrokenMachineException as e:
        print(e)
        # Repair the coffee machine
        coffee_machine.repair()
        print("The coffee machine has been repaired.")



if __name__== '__main__':
    test_coffee_machine()