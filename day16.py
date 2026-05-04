""""# list comprehensive
list=[1,2,3,4,5,6,7,8,9,10]
a=[i**2 for i in list]
print(a)
#Even
even=[i for i in list if i%2==0]
print(even)
#odd
odd=[i for i in list if i%2!=0] 
print(odd)
# adding 10 to each element in the list
add=[i+10 for i in list]
print(add)"""

#File handling

#write
""""f=open("hello.txt","w")
f.write("Hello World")  
f.close()

#Read
f=open("hello.txt","r")
print(f.read())
f.close()

print("Hello")
1/0
print("hiii")
f.close()"""
#Exception Handling
""""def division(a,b):
    try:
         div =a/b
    except ZeroDivisionError:
        print("Cannot Divide by Zero")
    except TypeError:
        print("Invalid Datatype")
    except Exception as e:   # handle any kind of exception 
        print(e)
    else:
        print("I will run if there is not exception raised")
        return div   
    finally:
        print("I will run no matter what happens in the code") 
print(division(3,9)) """
# zero divisionhandling
f=open("hello.txt","r")
print(f.read())
try:
    1/0
except Exception as e:
    print(e)
f.closed




