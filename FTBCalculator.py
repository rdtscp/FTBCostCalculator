from prettytable import PrettyTable


class FTBCalculator:

    static_fees = [
        (150, "Booking Fee"),
        (250, "Valuation Fee"),
        (500, "Land Registry Fee"),
        (550, "Survey Fee"),
        (1000, "Conveyancing Fee"),
    ]

    def __init__(self, savings, salary, mortgage_broker, help_to_buy):
        self.savings = savings
        self.salary = salary
        self.mortgage_broker = mortgage_broker
        self.help_to_buy = help_to_buy

    def converge_on_price(self, deposit, mortgage, house_price):
        h2b_loan = (house_price / 60 * 40) if self.help_to_buy else 0
        if (self.help_to_buy):
            house_price2 = min(house_price + h2b_loan, 600000)
        stamp_duty = self.get_stamp_duty_discounted(house_price2)
        if (deposit - stamp_duty + mortgage + h2b_loan < house_price2):
            return self.converge_on_price(deposit, mortgage, house_price - 1000)
        else:
            return deposit - stamp_duty, stamp_duty, house_price2

    def get_budget(self):
        deposit = self.savings

        total_fees = sum(fee for fee, _ in self.static_fees)

        deposit -= total_fees

        mortgage_loan = int(self.mortgage_broker.get_loan_amount(self.salary))

        deposit, stamp_duty, house_price = self.converge_on_price(
            deposit, mortgage_loan, deposit + mortgage_loan)

        all_fees = self.static_fees
        all_fees.append((stamp_duty, "Stamp Duty"))
        return deposit, all_fees, house_price

    def get_stamp_duty_discounted(self, house_price):
        tax = 0
        tax_bands = [
            (500000, 0),
            (925000, 0.05)
        ]

        price = house_price
        band = 0
        while price > 0:
            curr_band = tax_bands[band]
            amount_in_band = min(price, curr_band[0])
            tax += amount_in_band * curr_band[1]

            band += 1
            price -= amount_in_band

        return tax
