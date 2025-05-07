class Bank:
    bank_name = "Meezan Bank Limited"

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
        

    def display_info(self):
        print(f"Account holder: {self.account_holder}, Bank Name: {self.bank_name}")


account1 = Bank("anas")


account1.display_info()


Bank.change_bank_name("Bank Al-Habib Limited")


account1.display_info()

#print(account1.bank_name)
