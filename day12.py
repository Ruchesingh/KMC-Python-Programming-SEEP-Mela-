#constructor Function

class Math():
  def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        print(a,b,c)
        print("This is inti_")
        return None #nalekhenii hunxa
  def add(self):
      return self.a+self.b+self.c
obj=Math(2,4,6)
print(obj.add())

class Rectangle():
    def __init__(self,len,bdth):
        self.len= len
        self.bdth=bdth
        print(len,bdth)
        
    def area(self):
        return self.len*self.bdth
    
obj=Rectangle(6,9)
print(obj.area())     
        

class Employeee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        print(name,salary)
    def datails(self):
        return self.name,
    
    
obj=Employeee("Rucheee",100000)    
print(obj.details())

#Constructor Exercise
#Student Result System

class StudentResult():
    def __init__(self, name, *marks):
        self.name = name
        self.marks = list(marks)
        
    def average(self):
        if len(self.marks)==0:
            return "Zero Division Error"
        return sum(self.marks) / len(self.marks)
    
    def grade(self):
        avg = self.average()
        
       """ if avg[1]:
           average=avg[0]
           if average>=100:
               return "A+"
           else:"""
                    
    
    def display(self):
        return f"name={self.name}, marks={self.marks}, average={self.average()}, grade={self.grade()}"
    

obj = StudentResult("goool", 45, 89, 67)
print(obj.display())
    
        
        
          
        
             
      
  