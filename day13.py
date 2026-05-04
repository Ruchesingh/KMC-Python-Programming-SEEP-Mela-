#inheritance
class Parent():
    a=100
    b=50   
    def add(self):
        
        return self.a +self.b
    #def teacher(self):
       # return "I am a good teacher"
    
class Child(Parent):
    #b="Ruchee Singh"
    d=90
    def display(self):
        return self.add()
obj = Child()
print(obj.b)
print(obj.a)
print(obj.display())

#Constructor Inheritance
class TestParent():
     def __init__(self,a):
         print("I am testing code")
class TestChild(TestParent):
    def __init__(self,a,b,c,d):
        print("Okay Done")
        self.b=b 
        TestParent.__init__(self,a)
        super().__init__(a)
        
        #dui ota madey kunai nii grda hunxa
    def test(self):
        return self.b
class Child(TestChild):
    pass
obj=Child(4,5,6,7)   

#Question Practice
#Banking System
class Account:
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited {amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdrawn {amount}")
        else:
            print("Insufficient balance")

    def show_balance(self):
        return self.balance


class SavingsAccount(Account):
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.transactions.append(f"Interest added {interest}")


class PremiumSavingsAccount(SavingsAccount):
    def withdraw(self, amount):
        min_balance = 1000
        if self.balance - amount >= min_balance:
            super().withdraw(amount)
        else:
            print("Cannot withdraw: minimum balance required")

    def redeem_points(self):
        self.balance += self.reward_points
        self.transactions.append(f"Redeemed {self.reward_points} points")
        self.reward_points = 0
        
acc = PremiumSavingsAccount()

acc.account_number = "12345"
acc.balance = 5000
acc.transactions = []

acc.interest_rate = 0.05
acc.reward_points = 200
acc.deposit(1000)
acc.withdraw(2000)
acc.add_interest()
acc.redeem_points()

print(acc.balance)
print(acc.transactions)