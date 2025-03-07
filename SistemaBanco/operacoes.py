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

    def pagarNoCredito(self, valorCompra, limiteCredito):
        if valorCompra > limiteCredito:
            return False
        else:
            self.__limite = valorCompra - limiteCredito