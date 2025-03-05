class Person:
    def __init__(self, name, age, cpf, rg, estado, cidade):
        self.__name = name
        self.__age = age
        self.__cpf = cpf
        self.__rg = rg
        self.__estado = estado
        self.__cidade = cidade

    def getName(self):
        return self.__name
    
    def setName(self, newname):
        self.__name = newname

    def getAge(self):
        return self.__age
    
    def setAge(self, newAge):
        self.__age = newAge
    
    def getCPF(self):
        return self.__cpf
    
    def setCPF(self, novoCPF):
        self.__cpf = novoCPF

    def getRG(self):
        return self.__rg
    
    def setRG(self, novoRG):
        self.__rg = novoRG
    
    def getEstado(self):
        return self.__estadoss
    
    def setEstado(self, novoEstado):
        self.__estado = novoEstado

    def getCidade(self):
        return self.__cidade

    def setCidade(self, novaCidade):
        self.__cidade = novaCidade   
         
    def apresentar(self):
        print(f"Nome: {self.__name}, Idade {self.__age}")
        
