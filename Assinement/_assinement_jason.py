import json
from _employee import Employee

class Main():
 
 if __name__ == "__main__":
    file = open("G:\\Edyoda\\Assinement\\sample_json.json","r")
    # file = open("_21_json\\sample_json.json")

    # convert json into dict
    data = json.load(file)
    # print(data)
    # print(type(data))

    lst=[]
    for i in data:
      _employee_obj = Employee(i["name"], i["dob"],i["height"], i["city"], i["state"])
      lst.append(_employee_obj)
      print(lst)

    for j in lst:
      print(j)

# file1 = open("C:\\Users\\hemant pc\\Desktop\\Edyoda\\Assinement\\sample_json1.json","w")
# # convert dict into json
# json.dump(data,file1)
