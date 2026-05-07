
#Modifier
class A():
    _a=1 #private denotes the double underscore
    b=_a+1
    
    def __add(self):
        return self.__a+self.b
    
    def public__add(self):
        return self.__add()
        
obj=A()
print(obj.b)

#Exercise: 

class BankAccount():
    accountHolder="Ruchee"
    __balance=0
    
    
    def withdrawal(self,amount):
        self.__balance -=amount
        return amount
    
    def deposit(self,amount):
        self.__balance +=amount
        return amount
    
    
    def showBalance(self):
        return self.__balance
        
class StudentAccount(BankAccount):   
    studentId=2
    
    def payLibraryFine(self,amount):
        return self.withdrawal(amount) # private balance use gareko xa withdrawal method bata hami le sida use grna mildaina
     
obj=StudentAccount()

print(obj.payLibraryFine(500))
print(obj.deposit(200))
print(obj.showBalance())
             
    
    


    

