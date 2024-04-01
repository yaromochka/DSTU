from unittest import TestCase, main
from Calculator.main import calculator


class CalculatorTest(TestCase):
    def test_plus(self):
        self.assertEqual(calculator('2+2'), 4)

    def test_minus(self):
        self.assertEqual(calculator('3-1'), 2)


    def test_multi(self):
        self.assertEqual(calculator('4*3'), 12)


    def test_divide(self):
        self.assertEqual(calculator('12/2'), 6)


    def test_no_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('abracadabra')
        self.assertEqual('Выражение должно содержать хотя бы один знак (+-/*)', e.exception.args[0])


    def test_two_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('2+2+2')
        self.assertEqual('Выражение должно содержать два целых числа и один знак', e.exception.args[0])


    def test_many_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('2+3*10')
        self.assertEqual('Выражение должно содержать два целых числа и один знак', e.exception.args[0])


    def test_no_ints(self):
        with self.assertRaises(ValueError) as e:
            calculator('2.2+3.0')
        self.assertEqual('Выражение должно содержать два целых числа и один знак', e.exception.args[0])


    def test_strings(self):
        with self.assertRaises(ValueError) as e:
            calculator('a+b')
        self.assertEqual('Выражение должно содержать два целых числа и один знак', e.exception.args[0])


if __name__ == '__main__':
    main()