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
        some_coffee = Coffee()
        print("Some coffee: ", some_coffee)

        Intern = Coffee.Intern()
        print("Intern: ", Intern)

        
        nobody = Intern()
        print("Instantiation without name: ", nobody)
        print("Make me a coffée, nobody! ", nobody.make_coffee())
        mark = Intern("Mark")
        print("Instantiation with name: ", mark)
        print("Make me a coffée, Mark! ", mark.make_coffee())

        nobody.work()
        
    except Exception as e:
        print(e)


if __name__ == '__main__':
    test_intern()