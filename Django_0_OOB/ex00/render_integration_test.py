import unittest
import os
import render

class TestIntegration(unittest.TestCase):
    def test_generate_CV(self):
        # Create test template and settings files
        with open('test.template', 'w') as file:
            file.write("<p>{name}</p>")
        with open('settings.py', 'w') as file:
            file.write('name = "John Doe"')

        # Run the program
        render.generate_CV('test.template')

        # Check the output
        with open('test.html', 'r') as file:
            content = file.read()
        expected_output = "<p>John Doe</p>"
        self.assertEqual(content, expected_output)

        # Clean up
        os.remove('test.template')
        os.remove('settings.py')
        os.remove('test.html')

if __name__ == '__main__':
    unittest.main()