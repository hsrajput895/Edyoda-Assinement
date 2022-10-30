class Dog:
   def __init__(self,name,age,color):
      self.__name=name
      self.__age=age
      self.__color=color

   def discription(self):
       print(self.__name "\n" self.__age)
   def get_info(self):
       print(self.__color)
_dog=Dog("max",12,"black")
_dog.discription()
_dog.get_info()