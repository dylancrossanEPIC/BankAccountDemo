class BalanceException (Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\n Account '{self.name}' created.\nBlanace = ${self.balance:2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:2f} ")

    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f"\n Deposit complete.")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return 
        else:
            raise BalanceException(f"\n Sorry, account '{self.name}' only has a balance of ${self.balance:2f}")

    def withdraw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\n Withdraw complete")
            self.getBalance()
        except BalanceException as error:
            print(f'\n Withdraw interrupted: {error}')

    def transfer(self,amount, account):
        try:
            print('\n*********\n\n Beginning Transfer....')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\n Transfer Complete!\n\n*********')
        except BalanceException as error:
            print(f'\n Transfer interrupted: {error}')

class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount *1.05)
        print("\n Deposit complete")
        self.getBalance()

class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - (amount + self.fee)
            print("\n Withdraw complete")
            self.getBalance()
        except BalanceException as error:
            print(f'\n Withdraw interrupted: {error}')