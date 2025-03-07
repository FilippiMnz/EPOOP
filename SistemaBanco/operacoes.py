class Operacoes:
    def __init__(self, saldo, limite):
        self.__saldo = saldo
        self.__limite = limite

    def getSaldo(self):
        return self.__saldo

    def setSaldo(self, newSaldo):
        self.__saldo = newSaldo

    def getLimite(self):
        return self.__limite
    
    def setLimite(self, newLimite):
        self.__limite = newLimite

class Transacao:
    def __init(self, valor, descricao):
        self.__valor = valor
        self.__descricao = descricao

    def getValor(self):
        return self.__valor
    
    def setValor(self, newValor):
        self.__valor = newValor

    def getDescricao(self):
        return self.__descricao

    def setDescricao(self, newDescricao):
        self.__descricao = newDescricao