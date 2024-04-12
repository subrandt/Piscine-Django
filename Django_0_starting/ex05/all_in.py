import sys

def use_dict(arg: str):
    
    if arg == "":
        return
    
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
    
    # transform dictionaries to lower case for comparison
    states_lower = {k.lower(): v for k, v in states.items()}
    
    arg_lower = arg.lower()
    

    
    # if it is a state
    if arg_lower in states_lower:
        tmp_state = states_lower[arg_lower]
        print(tmp_state)
        print(capital_cities[tmp_state], "is the capital of", arg.title())
        return
    
    # inversion of the dictionaries:
    capital_to_state_lower = {v.lower(): k for k, v in capital_cities.items()}
    abbr_to_state = {v: k for k, v in states.items()}
    
    #  if it is a capital
    if arg_lower in capital_to_state_lower:
        tmp2 = capital_to_state_lower[arg_lower]
        print(arg.title(), "is the capital of", abbr_to_state[tmp2])
        return

    else:
        print(arg, "is neither a capital city nor a state")

    
def get_args(arg: str):
    # try:
        
        after_split = [arg.strip() for arg in arg.split(',')]
        
        for element in after_split:
            use_dict(element)
        

    # except Exception:
    #     print("error")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(1)
    
    get_args(sys.argv[1])