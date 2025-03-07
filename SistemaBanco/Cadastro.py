from pessoa import Pessoa

class Usuario(Pessoa):
    def __init__(self, nome, cpf, RG, endereco, dataNascimento, email, senha):
        super().__init__(nome, cpf, RG, endereco, dataNascimento)
        self.__email = email
        self.__senha = senha