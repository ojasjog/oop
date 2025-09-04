class BankAccount:
    def __init__(self, owner=str, balance=0):
        self.owner = owner
        self.balance = balance
        

    def deposit(self, amount):
        self.balance+=amount
        print(f"Deposited {amount} into {owner}'s account. New Balance: {self.balance}")

        

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance = self.balance - amount
            print(f"Withdrew {amount} from {owner}'s account. New Balance: {self.balance}")

owner = input("Enter name of account: ")

account = BankAccount(owner)

account.deposit(200)
account.withdraw(400)
account.withdraw(102)