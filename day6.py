# for loop exercise finite loop
for i in [1,2,3,4,5]:
    
 # (if (i%2==0):
    print(i)
    for i in "Ruchee":
        print(i)
    a={
    "name":"Ruchee",
    "college": "XYZ University"
       }
    for i in a:
        print(f'{i}: {"a[i]"}')
    for i in a.values():
        print(i)
     
    odd=[]
    even=[]
    for i in range(10,100,1):
        if (i%2==0):
            even.append(i)
        else:
            odd.append(i)
    print("Even numbers:", even)
    print("Odd numbers:", odd)
    num=[]
    a=[1,2,3,4,"Hello", "World",1,2,3,4,True]  
    for i in a:
        # if (type(i)==int):rakhnu hunaa  class ma object compare grna garo hunxa...
        if not isinstance(i,str):
             num.append(i)
    print("Integer values:", num)
    #addition
    a=[1,2,3,4,5]
    total=0
    for i in a:
        total+=i
    print(total)
    for i in [1,2,3]:
        for j in [4,5,6,7]:
            print(i,j)
            
     # while  infinite loop
     
    i=1 
    while(i<=10):
        print(i)
        i+=1
        
    a= [1,2,3,4,5,6,7,8,9,10,"hello", "world", True, False]
    while (a):
      print(a)
      break
     