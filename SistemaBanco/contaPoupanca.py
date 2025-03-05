from ContasBancarias import Conta

class Poupanca(Conta):
    def __init__(self, nome, idConta, saldo, rendimento, cartaoDebito):
        super().__init__(nome, idConta, saldo)
        self.__rendimento = rendimento
        self.__cartaoDebito = cartaoDebito

    def getRedimento(self):
        return self.__rendimento
    
    def setRendimento(self, newRendimento):
        self.__rendimento = newRendimento

    def getCartaoDebito(self):
        return self.__cartaoDebito
    
    def setCartaoDebito(self, newCartaoDebito):
        self.__cartaoDebito = newCartaoDebito