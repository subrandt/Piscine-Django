import random
from beverages import HotBeverage


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
    
    # Serve 12 beverages
    try:
        for i in range(12):
            result = coffee_machine.serve(HotBeverage)
            print(f"Served Beverage: {result.name}")
            print(f"Total served beverages: {coffee_machine.served_cups}")
            print(result)
    except CoffeeMachine.BrokenMachineException:
        # Repair the coffee machine
        print("The coffee machine is broken. Repairing...")
        coffee_machine.repair()
        print("The coffee machine has been repaired.")

    # Serve 12 beverages again
    try:
        for i in range(12):
            result = coffee_machine.serve(HotBeverage)
            print(f"Served Beverage: {result.name}")
            print(f"Total served beverages: {coffee_machine.served_cups}")
            print(result)
    except CoffeeMachine.BrokenMachineException:
        # Repair the coffee machine
        print("The coffee machine is broken. Repairing...")
        coffee_machine.repair()
        print("The coffee machine has been repaired.")



if __name__== '__main__':
    test_coffee_machine()