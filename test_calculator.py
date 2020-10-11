import unittest

from FTBCalculator import FTBCalculator
from MortgageBroker import MortgageBroker


class TestFTBCalculator(unittest.TestCase):
    FIXED_COSTS = sum(fee for fee, _ in FTBCalculator.static_fees)

    def test_affordability(self):
        salary = 50000
        savings = 50000
        broker = MortgageBroker(4)
        calc = FTBCalculator(savings, salary, broker, True)

        deposit, all_fees, house_price = calc.get_budget()
        sum_all_fees = sum(fee for fee, _ in all_fees)

        self.assertEqual(deposit, savings - self.FIXED_COSTS)
        self.assertEqual(sum_all_fees, self.FIXED_COSTS)
        self.assertEqual(house_price, 250000 - self.FIXED_COSTS)

    def test_affordability2(self):
        salary = 60000
        savings = 200000
        broker = MortgageBroker(5)
        calc = FTBCalculator(savings, salary, broker, True)

        deposit, all_fees, house_price = calc.get_budget()
        sum_all_fees = sum(fee for fee, _ in all_fees)

        self.assertEqual(deposit, savings - self.FIXED_COSTS)
        self.assertEqual(sum_all_fees, self.FIXED_COSTS)
        self.assertEqual(house_price, 500000 - self.FIXED_COSTS)

    def test_affordability3(self):
        salary = 70000
        savings = 80000
        broker = MortgageBroker(5)
        calc = FTBCalculator(savings, salary, broker, True)

        deposit, all_fees, house_price = calc.get_budget()
        sum_all_fees = sum(fee for fee, _ in all_fees)

        self.assertEqual(deposit, savings - self.FIXED_COSTS)
        self.assertEqual(sum_all_fees, 2450)
        self.assertEqual(house_price, 600000 - self.FIXED_COSTS)


if __name__ == '__main__':
    unittest.main()
