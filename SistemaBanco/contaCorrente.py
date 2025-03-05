from ContasBancarias import Conta

class ContaCorrente(Conta):
    def __init__(self, nome, idConta, saldo, tarifa, credito):
        super().__init__(nome, idConta, saldo)
        self.__tarifa = tarifa
        self.__credito = credito