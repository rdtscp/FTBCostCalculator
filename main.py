import argparse
from prettytable import PrettyTable

from FTBCalculator import FTBCalculator
from MortgageBroker import MortgageBroker


def calculate_affordability(savings, salary, mortgage_loan_factor, help_to_buy):
    broker = MortgageBroker(mortgage_loan_factor)
    ftbcalc = FTBCalculator(savings, salary, broker, help_to_buy)

    deposit, all_fees, house_price = ftbcalc.get_budget()
    sum_all_fees = sum(fee for fee, _ in all_fees)

    print("With £{} savings, you would spend £{} on fees:".format(
        savings, sum_all_fees))
    fees_table = PrettyTable()
    fees_table.field_names = ["Fee", "Cost(£)"]
    for fee, type in all_fees:
        fees_table.add_row([type, fee])
    fees_table.align["Fee"] = "l"
    fees_table.align["Cost(£)"] = "r"
    print(fees_table.get_string(sortby="Cost(£)"))
    print("\nWhich means your effective deposit on a house of price £{} is £{}".format(
        house_price, deposit))


def main():
    parser = argparse.ArgumentParser(
        description='Calculate House Price you can Afford')
    parser.add_argument('savings', type=int,
                        help='Integer value of £GBP saved.')
    parser.add_argument('salary', type=int, help='Annual Salary in £GBP.')
    parser.add_argument('--mortgage_loan_factor', type=float,
                        default=4.5, help='Factor of Salary Lending will Give')
    parser.add_argument('--help_to_buy', type=bool,
                        default=False, help='Use Help to Buy Equity Loan')
    args = parser.parse_args()

    calculate_affordability(args.savings, args.salary,
                            args.mortgage_loan_factor, args.help_to_buy)


if __name__ == "__main__":
    main()
