class BankAccount :
    bank_name = "State Bank of India"
    def __init__(self,holder_name,balance):
        self.name = holder_name
        self.balance = balance
    def display(self):
        print("\nBank Name :",self.bank_name)
        print("Holder Name :",self.name)
        print("Balance :",self.balance)
    @classmethod
    def change_bank(cls,new_bank_name):
        cls.bank_name = new_bank_name
    @staticmethod
    def is_valid_deposit(amount):
        if amount > 0 :
            return True
        return False
b1 = BankAccount("Kamalesh",5000)
b2 = BankAccount("Surya",10000)
BankAccount.change_bank("Indian Bank")
b1.display()
b2.display()
print(BankAccount.is_valid_deposit(1000))
print(BankAccount.is_valid_deposit(-100))
