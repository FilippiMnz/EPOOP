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
    
    def sacar(self, saque):
        if saque > self.getSaldo():
            return False
        else:
            novoSaldo = self.getSaldo() - saque 
            self.setSaldo(novoSaldo)
            return f"Saque de {saque}R$ realizado com sucesso, seu novo saldo eh de {self.getSaldo}"
        
    def Depositar(self, valor):
        if valor <= 0:
            return False
        else:
            novoSaldo = valor + self.getSaldo()
            self.setSaldo(novoSaldo)
            return f"Deposito de {valor}R$ foi efetuado com sucesso, seu novo saldo eh de {self.getSaldo}"
        
    

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

    
    def __str__(self):
        return f"{self.data.strftime('%d/%m/%Y %H:%M')} - {self.__descricao}: R$ {self.__valor:.2f}"