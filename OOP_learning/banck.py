

class BankAccount:
    def __init__(self, account_number, balance):
        self.account = account_number
        self.balance = balance

    def deposit(self, amount):
        try:
            int_v = int(amount)
            if int_v > 0:
                self.balance += int_v
            else:
                print("Deposit amount must be positive")
        except ValueError:
            print("Sorry, only numbers")

    def withdraw(self, amount):
            try:
                int_v = int(amount)
                if int_v <=0:
                    print("Withdrawal amount must be positive.")
                elif int_v <= self.balance:
                    self.balance -= int_v
                else:
                    print(f"Sorry, you don't have enough balance to withdraw {int_v}$")
            except ValueError:
                print("Sorry, only numbers")
        

    def checkBalance(self):
        return f"Hello owner of the account {self.account}, you have in bank {self.balance}$"


p1 = BankAccount(100, 0)
p2 = BankAccount(101, 200)
 
p1.deposit(100)
print(p1.checkBalance())
p1.withdraw(90)
print(p1.checkBalance())

p2.deposit(100)
print(p2.checkBalance())
p2.withdraw(500)
print(p2.checkBalance())