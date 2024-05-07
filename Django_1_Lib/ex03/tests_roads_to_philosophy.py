import unittest
import subprocess

class TestRoadsToPhilosophy(unittest.TestCase):

    def run_program(self, search_term):
        result = subprocess.run(['python3', 'roads_to_philosophy.py', search_term], capture_output=True, text=True)
        return result.stdout.strip()
        
    def test_empty_input(self):
        expected_pages = ["Main Page"]
        expected_output = "\n".join(expected_pages) + "\nIt leads to a dead end!"
        self.assertEqual(self.run_program(""), expected_output)
        
    def test_all_dead_end_pages(self):
        expected_output = "Http Error 404: Page not found\nIt leads to a dead end!"
        self.assertEqual(self.run_program("All dead-end pages"), expected_output)

    def test_philosophy(self):
        self.assertEqual(self.run_program("Philosophy"), "0 roads from philosophy to philosophy")

    def test_mouse(self):
        expected_pages = [
            "Mouse",
            "Rodent",
            "Mammal",
            "Vertebrate",
            "Deuterostome",
            "Bilateria",
            "Clade",
            "Phylogenetics",
            "Biology",
            "Science",
            "Scientific method",
            "Empirical evidence",
            "Proposition",
            "Philosophy of language",
            "Analytic philosophy",
            "Contemporary philosophy",
            "Western philosophy",
            "Philosophy"
        ]
        expected_output = "\n".join(expected_pages) + "\n18 roads from Mouse to philosophy"
        self.assertEqual(self.run_program("Mouse"), expected_output)

    def test_hunger(self):
        expected_pages = [
            "Hunger",
            "Politics",
            "Decision-making",
            "Psychology",
            "Mind",
            "Thought",
            "Consciousness",
            "Awareness",
            "Philosophy"
        ]
        expected_output = "\n".join(expected_pages) + "\n9 roads from Hunger to philosophy"
        self.assertEqual(self.run_program("Hunger"), expected_output)

    def test_france(self):
        expected_pages = [
            "France",
            "Western Europe",
            "Europe",
            "Continent",
            "Geography",
            "Earth",
            "Planet",
            "Hydrostatic equilibrium",
            "Fluid mechanics",
            "Physics",
            "Natural science",
            "Branches of science",
            "Formal science"
        ]
        expected_output = "\n".join(expected_pages) + "\nIt leads to an infinite loop!"
        self.assertEqual(self.run_program("France"), expected_output)

if __name__ == "__main__":
    unittest.main()