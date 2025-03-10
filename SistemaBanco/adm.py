from Cadastro import *

class ADM(Usuario):
    def __init__(self, nome, cpf, RG, endereco, dataNascimento, email, senha, cargo, idConta = None):
        super().__init__(nome, cpf, RG, endereco, dataNascimento, email, senha, idConta)
        self.__cargo = cargo
    
    def getCargo(self):
        return self.__cargo
    
    def setCargo(self, newCargo):
        self.__cargo = newCargo

    
    def Supremo(self, Usuario):
        if self.getCargo() == "adm":
            return True