import unittest

from samplePackage import format_text


class TestClass(unittest.TestCase):
    
    def test_format_text(self):
        expected_out = "my input: Jane Doe"
        real_out = format_text("Jane Doe")
        self.assertEqual(expected_out, real_out)


if __name__ == '__main__':
    unittest.main()
