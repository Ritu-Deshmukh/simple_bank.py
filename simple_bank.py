class bank_account:
  def __init__(self,name,acc_number,balance):
    self.name = name
    self.acc_number = acc_number
    self.balance = balance
    self.amount = 0

  def display_acc_info(self):
    print(f"name : {self.name}, acc_number : {self.acc_number}, balance : {self.balance}")

  def deposit(self,amount):
    self.balance += amount
    print(f"Deposited {amount}. New balance : {self.balance}")

  def withdraw(self,amount):
    self.balance -= amount
    print(f"Withdrew {amount}. New balance : {self.balance}")
