""""import csv

student=( 'Ruchee','ktm',23)

with open('student.csv', 'w') as f:
    writer= csv.writer(f) # tuple write ko lagi
    writer.writerow(student)
    
import csv

students=[
    ("Name","Address","Age"),
    ('Ram','Ktm',27),
    ('Rana','Mnr',28),
    ('Ratna','Ktm',23)
    
]
with open('students.csv','w') as f:
      writer=csv.writer(f)
      for student in students:
          writer.writerow(student) # single write at once
          writer.writerows(students) # bulk write at once

import csv

student={'name': "Rena", "address":"ktm","age":45}
with open("person.csv","w")as f:
    writer=csv.DictWriter(f,fieldnames=student.keys())  # Dictionary writer ko lagi
    writer.writeheader()
    writer.writerow(student)

import csv

students=[
        {'name':"Ram","Address":"Ktm","age":28},
        {'name':"Rekhaaaaa","Address":"Mnr","age":25},
        {'name':"Tilok","Address":"Pkr","age":29},
]    
with open("students.csv","w") as f:
     writer=csv.DictWriter(f, fieldnames=['name','Address','age'])
     writer.writeheader()
     for student in students:
         writer.writerow(student) # single write at once
         """
         
"""import csv

students=[
        {'name':"Ram","Address":"Ktm","age":28},
        {'name':"Rekhaaaaa","Address":"Mnr","age":25},
        {'name':"Tilok","Address":"Pkr","age":29},
]    
with open("students.csv","w", newline='',encoding='utf-8') as f:
     writer=csv.DictWriter(f, fieldnames=['name','Address','age'])
     writer.writeheader()
     for student in students:
         writer.writerows(students) # bulk write at once
         """
         
         
         
#Removing File

import os    
""""try:
    os.remove("person.csv")
except FileNotFoundError:
    print("File does not exist")
        
print(os.path.exists("person.csv"))


print(os.path.exists("student.csv"))


if os.path.exists("person.csv"):
    os.remove("person.csv")
else:
    print("File does not exist")

#os.mkdir("hello")  #make directory/folder
os.rename("hello",'hi')
os.rmdir("hii") # remove directory


# list comprehensive
ls=[1,2,3,4,5]
a=[]
# non pythonic code
for i in ls:
    a.append(i**2)
print(a)


 # pythonic way
a=[i*2 for i in ls]
print(a)


age=17
# ternary operator
is_authorized="unauthorized" if age<18 else "Authorized"
print(is_authorized)"""

""""numbers=[12,1,4,7]
a=["even" if i%2==0 else "odd" for i in numbers]
print(a)


for i in numbers:
     if i%2==0:
         a.append("even")
     else:
         a.append("odd")
         
print(a)

numbers=[-8,7,3,-9,5,9,2,1,4]
integer=['positive' if i>0 else 'negative' for i in numbers]
print(integer)

numbers=[-8,7,3,-9,5,9,2,1,4]
a=[i for i in numbers if i>0]
print(a)"""

# dictionary comprehensive
#non-pythonic 
us_price={'milk':2.05,'bread':2.6, 'butter':2.6}
nep_price={}
for k,v in us_price.items():
    nep_price.update({k: v*145})
print(nep_price)    

#pythonic
us_price={'milk':2.05,'bread':2.6, 'butter':2.6}
nep_price={
    k: v*145
    for k,v in us_price.items()
}
print(nep_price)