class Coffee:
    def __str__(self):
        return "This is the worst coffee you ever tasted."

    class Intern:
        def __init__(self, name="My name? I’m nobody, an intern, I have no name."):
            self.Name = name

        def __str__(self):
            return self.Name

        def work(self):
            raise Exception("I’m just an intern, I can’t do that...")

        def make_coffee(self):
            return self.Coffee()


def test_intern():
    try:
        # Create an instance of Coffee
        some_coffee = Coffee()
        print("Some coffee: ", some_coffee)

        # Try to make coffee with Coffee instance, this should fail
        try:
            some_coffee.make_coffee()
        except AttributeError:
            print("Coffee class cannot make coffee")

        # Create an instance of Intern
        Intern = Coffee.Intern()
        print("Intern: ", Intern)

        # Create an instance of Intern and make coffee, this should succeed
        nobody = Intern()
        print("Instantiation without name: ", nobody)
        print("Make me a coffee, nobody! ", nobody.make_coffee())
        mark = Intern("Mark")
        print("Instantiation with name: ", mark)
        print("Make me a coffee, Mark! ", mark.make_coffee())

        # Try to make Intern work, this should fail
        try:
            nobody.work()
        except Exception as e:
            print(e)

    except Exception as e:
        print(e)

if __name__ == '__main__':
    test_intern()