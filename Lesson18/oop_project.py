from bank_accounts import *

Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")

Dave.getBalance()
Sara.getBalance()

Sara.deposit(500)

Sara.widthdraw(1000)

Sara.transfer(2000, Dave)

Jim = InterestRewardsAcct(1000, "Jim")

Jim.getBalance()

Jim.deposit(1000)

Jim.transfer(100, Dave)

Jim.getBalance()

Blaze = SavingsAcct(1000, "Blaze")

Blaze.getBalance()

Blaze.deposit(500)

Blaze.transfer(333, Sara)

Blaze.getBalance()

Blaze.widthdraw(50)
