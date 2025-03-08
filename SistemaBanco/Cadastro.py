from cliente import Cliente

class Usuario(Cliente):
    def __init__(self, nome, cpf, RG, endereco, dataNascimento, email, senha):
        super().__init__(nome, cpf, RG, endereco, dataNascimento)
        self.__email = email
        self.__senha = senha
        self.__contas = []

    def getEmail(self):
        return self.__email
    
    def setEmail(self, newEmail):
        self.__email = newEmail
    
    def getSenha(self):
        return self.__senha

    def setSenha(self, newPass):
        self.__senha = newPass

    def imprima(self):
        return super().imprima() + f" Email: {self.__email}"
    
    def Listar_contas(self):
        for conta in self.__contas:
            return f"Usuario: {self.__nome}, CPF: {self.__cpf}"