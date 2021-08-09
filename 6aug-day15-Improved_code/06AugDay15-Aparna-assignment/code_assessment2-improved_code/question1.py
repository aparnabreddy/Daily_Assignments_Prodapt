import json, requests
try:
    data=requests.get("https://jsonplaceholder.typicode.com/todos")
    Extracted_data=data.json()
    Empty_list=[]
    Data_list_details = [i for i in Extracted_data if i["completed"]==True]
    Empty_list.append(Data_list_details)
    print(Empty_list)
except:
    print("Check the link and try again")
else:
    print("Got the details")
finally:
    print("Task completed")