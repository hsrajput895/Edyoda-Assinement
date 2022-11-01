from _dog import Dog
class JackRussellTerrier(Dog):
    def __init__(self, name,age, color,sound):
        super().__init__(self ,name,age,color)
        self.__sound=sound

    def speak(self):
        return f"{self.__name} barks: {self.__sound}"
    def owner():
        print("Owner of the Jackrusselterrier is Aditya")
    def get_info(self):
        return super().get_info()
if __name__== "__main__":
    _obj_jackrusselterrier=JackRussellTerrier("Jacky",4,"White","Bark")
    print(_obj_jackrusselterrier.speak())
    print(_obj_jackrusselterrier.owner())
    print(_obj_jackrusselterrier.get_info())