class BankAccount:
  def __init__(self, account_number, customer_name, date_of_opening, balance=0.0):

    self.account_number = account_number
    self.customer_name = customer_name
    self.date_of_opening = date_of_opening
    self.balance = balance

  def deposit(self, amount):

    self.balance += amount
    return amount

  def withdraw(self, amount):

    if amount > self.balance:
      return "Insufficient balance"
    self.balance -= amount
    return amount

  def check_balance(self):

    print(f"Current balance: ${self.balance:.2f}")

  def customer_details(self):

    print(f"\nCustomer Name: {self.customer_name}")
    print(f"Account Number: {self.account_number}")
    print(f"Date of Opening: {self.date_of_opening}")
    print(f"Balance: ${self.balance:.2f}")

# Example
account1 = BankAccount("1234567890", "John Doe", "2023-07-16")

deposit_amount = account1.deposit(100.00)
print(f"Deposited ${deposit_amount:.2f}")

withdrawal_amount = account1.withdraw(50.00)
print(f"Withdrew ${withdrawal_amount:.2f}")

withdrawal_amount = account1.withdraw(100.00)
print(withdrawal_amount)

account1.check_balance()

account1.customer_details()
