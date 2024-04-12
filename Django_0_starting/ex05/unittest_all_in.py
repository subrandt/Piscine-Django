import unittest
import io
import sys
from all_in import use_dict

class TestMyFunction(unittest.TestCase):
    def setUp(self):
        self.states = {
            "Oregon" : "OR",
            "Alabama" : "AL",
            "New Jersey": "NJ",
            "Colorado" : "CO"
        }

        self.capital_cities = {
            "OR": "Salem",
            "AL": "Montgomery",
            "NJ": "Trenton",
            "CO": "Denver"
        }

    def test_state_to_capital(self):
        capturedOutput = io.StringIO()          # Create StringIO object
        sys.stdout = capturedOutput               #  and redirect stdout.
        use_dict("Oregon")                       # Call function.
        sys.stdout = sys.__stdout__               # Reset redirect.
        self.assertEqual(capturedOutput.getvalue().strip(), "Salem is the capital of Oregon")  # Now works same as before.

if __name__ == '__main__':
    unittest.main()