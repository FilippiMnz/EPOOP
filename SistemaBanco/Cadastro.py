from cliente import Cliente

class Usuario(Cliente):
    def __init__(self, nome, cpf, RG, endereco, dataNascimento, email, senha):
        super().__init__(nome, cpf, RG, endereco, dataNascimento)
        self.__email = email
        self.__senha = senha

    def getEmail(self):
        return self.__email
    
    def setEmail(self, newEmail):
        self.__email = newEmail
    
    def getSenha(self):
        return self.__senha

    def setSenha(self, newPass):
        self.__senha = newPass

    