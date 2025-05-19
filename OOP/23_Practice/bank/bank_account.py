class BankAccount:
    def __init__(self, accountHolder, initialBalance):
        self.accountholder = accountHolder
        self.__initailbalance = initialBalance

    def Deposit(self, amount):
        if amount > 0:
            self.__initailbalance += amount
            print(f"Deposited: Rs.{amount}")
        else:
            print(f"Deposit must be positive")

    def Withdraw(self, amount):
        if amount <= self.__initailbalance:
            self.__initailbalance -= amount
            print(f"Withdrawn: Rs.{amount}")
        else:
            print("Insufficient funds.")

    def Get_balance(self):
        print(f"Current balance: {self.__initailbalance}")

    def set_balance(self, amount):
        if amount >= 0:
            self.__initailbalance = amount
            print(f"Balance set to: Rs.{amount}")
        else:
            print("Balance must be a non-negative number.")