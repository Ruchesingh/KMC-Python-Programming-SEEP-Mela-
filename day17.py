#file handling

""""with open("hello.txt","w") as f:
  f.write("Hello World")  
print(f.closed()) """  
  
  
""""with open("hello.txt","r") as f:
  print(f.read(10))  # read  first 10 characters
  
with open("hello.txt","r") as f:
  #  print(f.read())
   # print(f.tell())
   # f.seek(12)
   # print(f.read(4))
    print(f.readline())
    for i in f:
        print(i)
with open("python.jpg","r") as f: # read in text mode
    print(f.read())"""       
    
 #json string
""""import json 
person={"name":'Ruchee',"age":22, "address":'ktm',
            "skills":['python','php'],"is_programmar":True,"phone":None}
person_json =json.dumps(person) #dictornary to json string
print(person_json, type(person_json))"""

"""json_string= '''
{"name":"Ruchee","age":22, "address":"ktm",
            "skills":["python","php"],"is_programmar":True,"phone":None}
person_json  """
""""
with open("person.json", "w") as f:
    #f.write(person_json) #json string to json file
    json.dump(person,f,indent=4) # dictionary to json file
    #hami le dumps string ko lagi use hunxa
with open("person.json","r") as f:
    data=f.read() # variable ho sabai yesma hunxa (string ma aauxa)
    json_data =json.loads(data) #( dictionary ma aauxa)
    
    print(json_data, type(json_data)) 
    
with open("person.json","r") as f:
      json_data =json.load(f) # json file to dictionary
      print(json_data, type(json_data)) """
      
      
 #CSV
import csv
with open("sample_users.csv", "r") as f:
    data=csv.DictReader(f)
    #dictionary ma liyera aauxaaa
    for i in data:
        print(i['first_name'],i['address'])      