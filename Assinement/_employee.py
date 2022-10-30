class Employee:
   def __init__(self,name, dob, height, city, state):
        self.name = name
        self .dob = dob
        self.height = height
        self.city = city
        self.state = state
   
   def __str__(self):
      return  f"Employee Name: {self.name}\n Employee dob:{self.dob}\n Employee height:{self.height}\n Employee City:{self.city}\nEmployee State:{self.state}"
