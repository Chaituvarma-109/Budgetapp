"""
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
"""


class Category:
    def __init__(self, category) -> None:
        self.category = category
        self.ledger = []
        self._bal_amount = 0.00

    def add_ledger(self, amt, description):
        ledger_obj = {
            "amount": amt,
            "description": description
        }
        self.ledger.append(ledger_obj)

    def deposit(self, amt, description=None) -> None:
        self._bal_amount += amt
        self.add_ledger(self._bal_amount, description)

    def withdraw(self, amt, description=None) -> bool:
        res = self.check_funds(amt)
        if res:
            self._bal_amount -= amt
            self.add_ledger(-self._bal_amount, description)
            return True
        return False

    def get_balance(self) -> float:
        return self._bal_amount

    def transfer(self, amt, bud_cat) -> bool:
        res = self.check_funds(amt)
        if res:
            self.withdraw(amt, f"Transfer to {bud_cat}")
            bud_cat.deposit(amt,  f"Transfer from {self}")
            return True
        return False

    def check_funds(self, amt) -> bool:
        if amt > self._bal_amount:
            return False
        return True


def create_spend_chart(categories):
    pass
