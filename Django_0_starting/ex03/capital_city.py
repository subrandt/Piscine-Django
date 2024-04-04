import sys

def capital_city(capital: str):
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
    
    try:
        tmp = states[capital]
        print(capital_cities[tmp])

    except Exception:
        print("Unknown state")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(1)
    capital_city(sys.argv[1])