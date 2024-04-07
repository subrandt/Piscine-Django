import sys

def get_args(arg: str):
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }

    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(1)

    for arg in sys.argv:
        get_args(arg)