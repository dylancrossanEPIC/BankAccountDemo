from bank_accounts import *

Dave = BankAccount(1000, "Dave")
Sarah = BankAccount(2000, "Sarah")

Dave.deposit(1000)
Sarah.deposit(2000)


# Dave.withdraw(100)

Dave.transfer(500,Sarah)

Jim = InterestRewardsAcct(1000, "Jim")
Jim.deposit(100)
Jim.transfer(100, Dave)

Blaze = SavingsAcct(1000, "Blaze")
Blaze.getBalance()
Blaze.deposit(100)
Blaze.transfer(1000, Sarah)