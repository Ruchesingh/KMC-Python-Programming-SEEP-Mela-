#Recursion Exercise
def fac(n):
     if n==1 or n==1:
        return 1
     else:
        return n*fac(n-1)
 
print(fac(5)) 


#class and objects: class ko name capital ma rakhnu prxa,
#function lai member fuction ani variables lai attributes

class Person():
    a=100
    b=1000
    
data=Person()
print(data.a)
print(data.b)

data2=Person()
print(data2.a)
print(data2.b)


 
 
data.door="main door"
print(data.door)

print(data2.door)


class Test():
    a="Ruchi"
    b="singh"
    
    def add(self): 
        
        # object lai thaha huna class ko attributes or fuction(method)
        # haru tei vayera self or kunai first parameter use grnu prxa
     return self.a+self.b
obj1=Test()
print(obj1.a)
print(obj1.add())

class Test():
    a=100
    b=134
    
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a - self.b
    def result(self):
        return self.add(),self.sub()
    
obj1=Test()
print(obj1.result())


#Practice Question
class Student():
    name="Rucheee"
    marks=[20,0,6,45,0]
    average=0
    
    def grade(self):
      average=0
      for i in self.marks:
          average=average+i
          
      if average>= 80:
          return "Grade A" 
      elif average >=60-79:
          return "Grade B"
           
      elif average >=40-59:
          return "Grade C"
      elif average <"Fail":
          return "Grade B"
obj1=Student()
print(obj1.grade()) 
    

