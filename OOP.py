class bankaccount: 
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"deposited ${amount}. new balance ${self.balance}")
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"withdrawed ${amount}. new balance ${self.balance}")  
        else:
            print("Invalid withdrawal amount or insufficient funds.")  
    
    def  check_balance(self):
         print(f"account balance: $(self.balance)")   

class SavingsAccount(bankaccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.2):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate
    def apply_interest(self):
        interest =  self.balance * self.interest_rate
        self.balance += interest
        print(f"interest applied: ${interest: .2f}. new balance: ${self.balance: .2f}")   


savings = SavingsAccount("Alice", 500, 0.3) 
savings.deposit(200) 
savings.apply_interest() 
savings.withdraw(100) 
savings.check_balance()

account = bankaccount("John", 100)  
account.deposit(50)  
account.withdraw(30) 
account.check_balance()




       
