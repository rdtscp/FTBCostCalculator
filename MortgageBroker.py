class MortgageBroker:

    def __init__(self, mortgage_loan_factor):
        self.mortgage_loan_factor = mortgage_loan_factor

    def get_loan_amount(self, salary):
        return salary * self.mortgage_loan_factor
