#multiple inheritance
class Parent1():
    a=10
    b=20
class Parent2():
    b=30
    c=45
    
class Child(Parent1,Parent2):
      a=80
obj=Child()
print(obj.a)
print(Child.__mro__)

#lambda function

def add(x,y):
    return x+y
print(add(4,9))


data=lambda x,y :x+y
print(data(8,9))

data=[1,2,3,4]
a=[i**2 for i in data]
print(a)

square=lambda *args:[i**2 for i in args] # list comprehensive
print(square(1,2,3,4,5))
print(square(15,26))

