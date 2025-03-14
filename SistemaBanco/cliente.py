import random 
class Cliente:
    def __init__(self, nome, cpf, RG, endereco, dataNascimento, cargo, idConta = None):
        self.__nome = nome
        self.__cpf = cpf
        self.__rg = RG
        self.__endereco = endereco
        self.__dataNascimento = dataNascimento
        self.__cargo = cargo
        self.__idConta = random.randint(1, 100000)

    def getNome(self):
        return self.__nome
    
    def getCPF(self):
        return self.__cpf
    
    def getRG(self):
        return self.__rg
    
    def getEndereco(self):
        return self.__endereco
    
    def getDataNasci(self):
        return self.__dataNascimento
    
    def getId(self):
        return self.__idConta
    
    def setNome(self, newNome):
        self.__nome = newNome

    def setCPF(self, newCPF):
        self.__cpf = newCPF
    
    def setRG(self, newRG):
        self.__rg = newRG

    def setEndereco(self, newEndereco):
        self.__endereco = newEndereco

    def setDataNascimento(self, newDataNascimento):
        self.__dataNascimento = newDataNascimento

    def setId(self, newId):
        self.__idConta = newId
    
    def imprima(self):
        return f"Cliente {self.__nome} CPF: {self.__cpf}, Endereço: {self.__endereco}, Data nascimento: {self.__dataNascimento}, RG: {self.__rg}, conta: {self.__idConta}"