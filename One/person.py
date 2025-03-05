class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def getName(self):
        return self.__name
    
    def setName(self, Newname):
        self.__name = Newname

    def getAge(self):
        return self.__age
    
    def SetAge(self, NewAge):
        self.__age = NewAge
    
    def apresentar(self):
        print(f"Nome: {self.__name}, Idade {self.__age}")
        
