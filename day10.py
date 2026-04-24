
#return should same formate here we use dictonary to store the log event and its details. The function validates the input, constructs the log structure, and handles metadata appropriately. If the priority is set to "high", it adds an alert flag to the metadata.

#event logger:
def log_event(event_type, *args, **kwargs):
    pass
    if not isinstance(event_type, str):
        return {
            "Error": "Event type must be a string"
        }
    if len(args) <=0:
        return {
          "Error": "At least one message is required"
        }
    if kwargs["priority"]=="high":
        kwargs["alert"]=True
    return {
        "type": event_type,
        "messages": list(args),
        "meta": kwargs
    }    
print(log_event(
    1, "name r is not defined ",
    "type error cannot add str and int",
    timestamp=f'{datetime.now()}',
    user="root",
    priority="low"))

    
print(log_event(
    "ERROR", "name r is not defined ",
    "type error cannot add str and int",
    timestamp=f'{datetime.now()}',
    user="root",
    priority="high"))

#Recursion Function : function call by function
def test():
    print("This is fuction")
    return test()
test()

 
    
   