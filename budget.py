from typing import Union
"""
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
"""


class Category:
    def __init__(self, category: str) -> None:
        self.category = category
        self.ledger = []
        self._bal_amount = 0.00

    def __str__(self) -> str:
        bill = self.category.center(30, '*') + '\n'
        for i in self.ledger:
            bill += f'{i.get("description")[:23]:23}' + f'{i.get("amount"):7.2f}' + '\n'
        bill += f'Total: {self.get_balance():.2f}'
        return bill

    def add_ledger(self, amt: Union[float, int], description: str):
        ledger_obj = {
            "amount": amt,
            "description": description
        }
        self.ledger.append(ledger_obj)

    def deposit(self, amt: Union[float, int], description: str = 'No Description') -> None:
        self._bal_amount += amt
        self.add_ledger(amt, description)

    def withdraw(self, amt: Union[float, int], description: str = 'No Description') -> bool:
        res = self.check_funds(amt)
        if res:
            self._bal_amount -= amt
            self.add_ledger(-amt, description)
            return True
        return False

    def get_balance(self) -> float:
        return self._bal_amount

    def transfer(self, amt: Union[float, int], bud_cat: "Category") -> bool:
        res = self.check_funds(amt)
        if res:
            self.withdraw(amt, f"Transfer to {bud_cat}")
            bud_cat.deposit(amt,  f"Transfer from {self}")
            return True
        return False

    def check_funds(self, amt: Union[float, int]) -> bool:
        return amt <= self._bal_amount


def create_spend_chart(categories):
    pass
