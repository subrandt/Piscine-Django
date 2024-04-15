class HotBeverage:
    price = 0.30
    name = "hot beverage"

    def description(self):
        return "Just some hot water in a cup."
    
    def __str__(self):
        return self.description()


class Coffee(HotBeverage):
    name = "coffee"
    price = 0.40

    def description(self):
        return "A coffee, to stay awake."

class Tea(HotBeverage):
    name = "tea"
    # price is not neccessary
    def description(self):
        return "Just some hot water in a cup."
    
class Chocolate(HotBeverage):
    name = "chocolate"
    price = 0.50

    def description(self):
        return "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
    name = "cappuccino"
    price = 0.45

    def description(self):
        return "Un po’ di Italia nella sua tazza!"


if __name__== '__main__':

    hot_beverage = HotBeverage()
    print("\nname : ", hot_beverage.name)
    print("price : ", hot_beverage.price)
    print("description : ", hot_beverage.description())

    coffee = Coffee()
    print("\nname : ", coffee.name)
    print("price : ", coffee.price)
    print("description : ", coffee.description())

    tea = Tea()
    print("\nname : ", tea.name)
    print("price : ", tea.price)
    print("description : ", tea.description())

    chocolate = Chocolate()
    print("\nname : ", chocolate.name)
    print("price : ", chocolate.price)
    print("description : ", chocolate.description())

    cappuccino = Cappuccino()
    print("\nname : ", cappuccino.name)
    print("price : ", cappuccino.price)
    print("description : ", cappuccino.description())
    