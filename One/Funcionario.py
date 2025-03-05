from person import Person
class Funcionario(Person):
    def __init__(self, name, age, cpf, rg, estado, cidade, id, cargo):
        super().__init__(name, age, cpf, rg, estado, cidade)
        self.__id = id
        self.__cargo = cargo

    def getId(self):
        return self.__id
    
    def setId(self, newId):
        self.__id = newId

    def getCargo(self):
        return self.__cargo

    def setCargo(self, newCargo):
        self.__cargo = newCargo

    
    def infoFuncionario(self):
        print(f"Funcionario {super().apresentar()} e trabalha como {self.__cargo} e possui o ID: {self.__id}")