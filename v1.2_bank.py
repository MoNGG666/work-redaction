import math
import random

class Account:
    def __init__(self, account_number: int, customer_name: str, customer_address: str, balance: float):
        self.account_number = account_number
        self.customer_name = customer_name
        self.customer_address = customer_address
        self.balance = balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount


class Bank:
    def __init__(self):
        self.accounts = {}
        self._next_account_number = 1

    def create_account(self, customer_name: str, customer_address: str, initial_balance: float) -> Account:
        account_number = self._generate_account_number()
        account = Account(account_number, customer_name, customer_address, initial_balance)
        self.accounts[account_number] = account
        return account

    def get_account(self, account_number: int) -> Account:
        try:
            return self.accounts[account_number]
        except KeyError:
            raise ValueError(f"Account {account_number} not found")

    def _generate_account_number(self) -> int:
        number = self._next_account_number
        self._next_account_number += 1
        return number


class Customer:
    def __init__(self, name: str, address: str, bank: Bank):
        self.name = name
        self.address = address
        self.bank = bank

    def open_account(self, initial_balance: float) -> Account:
        return self.bank.create_account(self.name, self.address, initial_balance)


def banking_scenario():
    bank = Bank()
    customer1 = Customer("Alice", "Moscow, Stremyannyi per, 1", bank)
    customer2 = Customer("Bob", "Vorkuta, ul. Lenina, 5", bank)

    # Alice opens an account and deposits some money
    alice_account = customer1.open_account(initial_balance=500.0)
    alice_account.deposit(100.0)
    print(f"Alice's balance: {alice_account.balance}")  # 600.0

    # Bob opens an account and deposits some money
    bob_account = customer2.open_account(initial_balance=1000.0)
    bob_account.deposit(500.0)
    print(f"Bob's balance: {bob_account.balance}")  # 1500.0

    # Alice withdraws some money
    alice_account.withdraw(300.0)
    print(f"Alice's balance: {alice_account.balance}")  # 300.0

    # Attempt to overdraw
    try:
        alice_account.withdraw(500.0)
    except ValueError as e:
        print(e)  # Insufficient funds

    # Account information retrieval
    retrieved_account = bank.get_account(alice_account.account_number)
    print(f"Account {retrieved_account.account_number} by {retrieved_account.customer_name} "
          f"({retrieved_account.customer_address}), balance {retrieved_account.balance}")


if __name__ == "__main__":
    banking_scenario()
