from _dog import Dog
class BullDog(Dog):
    def __init__(self, name,age, color,sound,bread):
        super().__init__(self,name,age,color)
        self.__bread=bread
        self.sound=sound

    def speak(self):
        print(self.__name ," barks:" ,self.sound)
    
    def bread(self):
        return f"{self.name} bread: {self.__bread}"
if __name__=="__main__":
    _obj_bulldog=BullDog("max",4,"Black","dwarf","Bulldog")
    print(_obj_bulldog.speak())
    print(_obj_bulldog.bread())