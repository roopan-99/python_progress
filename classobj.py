class BankAccount:
 def __init__(self ,name,balance):
     self.name=name
     self.balance=balance

 def deposit(self,amount):
    self.balance += amount        

 def withdraw(self,amount):
    if amount <=self.balance:
        self.balance -= amount
        print("Withdraw:",amount)
    else:
        print("Insufficient balance")

 def show_balance(self):
    print("Account Holder:-",self.name)
    print("Balance:",self.balance)

acc1=BankAccount("Roopan",1000)
acc1.deposit(500)
acc1.withdraw(200)
acc1.show_balance()