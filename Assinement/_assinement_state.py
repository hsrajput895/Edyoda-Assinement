import json

_dict=[
{"state": "madhya pradesh","capital":"bhopal"},
{"state": "Maharastra","capital":"mumbai"},
{"state": "rajasthan","capital":"Jaipur"},
{"State":"bihar","Capital":"Patana"},
{"State":"Karnatka","Capital":"Banglore"},
{"State":"Tamilnaddu","Capital":"Chennai"}
]
file1 = open("C:\\Users\\hemant pc\\Desktop\\Edyoda\\Assinement\\sample_json1.json","w")
# # convert dict into json
json.dump(_dict,file1)
