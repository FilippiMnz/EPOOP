class Conta:
    def __init__(self, nome, idConta, saldo):
        self.__nome = nome
        self.__idConta = idConta
        self.__saldo = saldo

    def getNome(self):
        return self.__nome

    def setNome(self, newNome):
        self.__nome = newNome

    def getId(self):
        return self.__idConta
    
    def setId(self, newID):
        self.__idConta = newID

    def getSaldo(self):
        return self.__saldo
    
    def setSaldo(self, newSaldo):
        self.__saldo = newSaldo