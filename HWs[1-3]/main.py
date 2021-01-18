import unittest
from hexnumber import HexNumber

class TestHexNumber(unittest.TestCase):

    def test_sum(self):
        num1 = HexNumber('B37A8')
        num2 = HexNumber('61AF790')

        result = num1.add(num2)

        self.assertEqual('6262F38', result)

    def test_invalid_hexnumber(self):
        num = HexNumber('be37A8')

        self.assertEqual(None, num)


if __name__ == '__main__':
    unittest.main()