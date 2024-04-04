import sys

def state_from_capital(capital: str):
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

    # inversion of the dictionaries:
    capital_to_state = {v: k for k, v in capital_cities.items()}
    abbr_to_state = {v: k for k, v in states.items()}

    try:
        tmp = capital_to_state[capital]
        print(abbr_to_state[tmp])

    except Exception:
        print("Unknown capital city")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(1)
    state_from_capital(sys.argv[1])