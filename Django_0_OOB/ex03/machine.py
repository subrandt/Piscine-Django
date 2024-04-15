
from beverages import HotBeverage


class CoffeeMachine:
    def __init__(self, cups, status="working"):
        self.cups = cups
        self.status = status
    
    class EmptyCup(HotBeverage):
        name = "empty cup"
        price = 0.90
        def description(self):
            return "An empty cup?! Gimme my money back!"
        
    
    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")
    
    # def repair():

    def serve():
        if random.randint(0, 1):
            return CoffeeMachine.EmptyCup()
        else:
            return Coffee()