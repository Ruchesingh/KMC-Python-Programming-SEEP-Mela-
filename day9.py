      #keyword argument
      #keyword same hunuprxa,case sensitive 
""""def user_info(fname,lname,age):
       return f'my name is {fname} ,{age} '
print(user_info(fname="Ruchiii",age=10,lname="Singh"))"""
   
"""def sum_number(*num): #argument tuple ma linxaa 
    print(num)
    print(type(num))
sum_number(1)
sum_number(1,2,3)
sum_number()"""
# we can use len in tuple [len()>=1]
"""sum=0
if len(num)>1:
    for i in num:
           sum=sum+i
         return f'The sum is'  
else:
    return "len must be more than 1"
    
    
print(sum_number(1,2)) 
print(sum_number())      """

"""def sum_number(*num):
    sum=0
    for i in num:
        if not isinstance(i,str):
         sum=sum+i
    return f'The sum is {sum}'    
              
print(sum_number(1,"test",3,7,"rest"))"""
#argumentary keyword kargu-** bcz of keywords also created ,all are in dictionary
""""def per(**data):
      
    if 'eng' not in data or 'nep' not in data or 'math'not in data:
          print("error")
    else:
         print("eng", data['eng'])
         print("nep", data['nep'])
         print("math", data['math'])
  
per(eng=100,nep=45,math=89)

per(eng=50,nep=15)"""
#missing key
           
# positinal and keywords argument
""""def student(*marks,**info):hami le positional argument jaile agadhi rakhnu prxa ani null nii rakhna mildiana"""

""""Event Logger System"""































































































































































