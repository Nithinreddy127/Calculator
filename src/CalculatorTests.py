import unittest
from Calculator import Calculator
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition(self):
        test_data = CsvReader('/src/TestFile/Addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_subtraction(self):
        test_data3 = CsvReader('/src/TestFile/subtraction.csv').data
        for row in test_data3:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_multiply(self):
        test_data2 = CsvReader('/src/TestFile/Multiplication.csv').data
        for row in test_data2:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_div(self):
        test_data5 = CsvReader('/src/TestFile/Division.csv').data
        for row in test_data5:
            self.assertEqual(self.calculator.div(row['Value 1'], row['Value 2']), round(float(row['Result']), 9))
            self.assertEqual(self.calculator.result, round(float(row['Result']), 9))

    def test_square(self):
        test_data1 = CsvReader('/src/TestFile/Square.csv').data
        for row in test_data1:
            self.assertEqual(self.calculator.square(row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_root(self):
        test_data5 = CsvReader('/src/TestFile/Root.csv').data
        for row in test_data5:
            self.assertEqual(self.calculator.squareroot(row['Value 1']), round(float(row['Result']), 8))
            self.assertEqual(self.calculator.result, round(float(row['Result']), 8))


if __name__ == '__main__':
    unittest.main()
