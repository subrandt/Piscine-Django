import unittest
import render

class TestRender(unittest.TestCase):
    def test_replace_placeholders(self):
        content = "<p>{name}</p>"
        settings = {"name": "John Doe"}
        expected_output = "<p>John Doe</p>"
        output = render.replace_placeholders(content, settings)
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()