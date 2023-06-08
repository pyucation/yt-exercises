"""
Topic: OOP
Difficulty: 3/5
Requires: classes, instance attributes, methods

Task:
You are given a class "Account", which represents the bank account of thousands
of customers of the bank.
While revising the code you recognize that certain attributes are publicly
accessible, which is a high-level security risk. Change the class, more
specifically the encapsulation of some instance attributes, to make it more
secure.

Hint: Use the @property decorator.
"""

class Account:
    overdraft_interest = 0.07

    def __init__(self, acc_number, holder, pin, balance=0):
        self.acc_number = acc_number
        self.holder = holder
        self.pin = pin
        self.balance = balance
        self.overdraft = False
        self.pin_correct = False

    def transfer_money(self, account, amount):
        self.balance -= amount
        account.balance += amount

    # called monthly
    def apply_overdraft_interest(self):
        if self.overdraft:
            self.balance *= 1 + self.overdraft_interest

    def check_overdraft(self):
        if self.balance < 0:
            self.overdraft = True
        else:
            self.overdraft = False

    def enter_pin(self, pin):
        if pin == self.pin:
            self.pin_correct = True
            return True
        return False



if __name__ == "__main__":
    my_account = Account("UK7812349876", "Boris Smith", 1234)
    other_account = Account("UK3468419384", "Tina Alvarez", 9876)

    my_account.balance = 100000
    my_account.check_overdraft()
    other_account.balance = -900
    other_account.check_overdraft()

    other_account.overdraft = False
    other_account.apply_overdraft_interest()

    my_account.transfer_money(other_account, 100000000)
    my_account.check_overdraft()
    my_account.balance = 100000
    my_account.check_overdraft()

    other_account.pin = 0000

    my_account.holder = "HackerBoy9000"
