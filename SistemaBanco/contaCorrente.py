from ContasBancarias import Conta

class ContaCorrente(Conta):
    def __init__(self, nome, idConta, saldo, tarifa, LimiteCredito, TipoConta):
        super().__init__(nome, idConta, saldo, TipoConta)
        self.__tarifa = tarifa
        self.__credito = LimiteCredito
        TipoConta = "Corrente"

    def getTarifa(self):
        return self.__tarifa
    
    def setTarifa(self, newTarifa):
        self.__tarifa = newTarifa
    
    def getCredito(self):
        return self.__credito
    
    def setCredito(self, newCredito):
        self.__credito = newCredito

    