class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print('Insufficient funds: Charging a $5 fee')
            self.balance -= 5
        return self

        @staticmethod
        def can_withdraw(balance, amount):
            if (balance - amount) < balance:
                return False
            else:
                return True

    def display_account_info(self):
        print(f"balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 1:
            self.balance += (self.balance * self.int_rate)
            return self

class user:

    def __init__(self,name):
        self.name = name
        self.account = {
            'checking' : BankAccount(.02,1000),
            'savings' : BankAccount(.05, 5000)
        }
    
    def display_balance(self):
        print(f"User: {self.name}, Your Checking Balance: {self.account['checking'].display_account_info()}")
        print(f"User: {self.name}, Your Savings Balance: {self.account['savings'].display_account_info()}")
        return self

    def transfer_funds(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_balance()
        user.display_balance()
        return self


Amir = user('Amir')
Jordan = user('Jordan')

Amir.account['checking'].deposit(800)
Jordan.account['checking'].deposit(200)
Amir.display_balance()
Jordan.display_balance()


