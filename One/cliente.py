from person import Person

class cliente(Person):
    def __init__(self, name, born, cpf, rg, estado, cidade, id):
        super().__init__(name, born, cpf, rg, estado, cidade)
        self.__id = id