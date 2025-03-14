from operacoes import *
class CartaoCredito:
    def __init__(self, cliente, limite):
        self.__cliente = cliente
        self.__limite = limite
        self.__fatura = 0
        self.__transacoes = []

    def getCliente(self):
        return self.__cliente
    
    def getLimite(self):
        return self.__limite
    
    def getFatura(self):
        return self.__fatura
    
    def getTransacoes(self):
        return self.__transacoes
    
    def comprar(self, valor, descricao):
        if valor >(self.__limite - self.__fatura):
            return False
        else:
            self.__fatura += valor
            transacao = Transacao(valor, descricao)
            self.__transacoes.append(transacao)
            return f"Compra de R$ {valor:.2f} em {descricao} realizada com sucesso"

    def pagamentoFatura(self, conta):
        if self.__fatura > conta.saldo:
            return f"Saldo Insuficiente"
        else:
            conta.sacar(self.fatura)