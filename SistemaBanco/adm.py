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
            adm = True
            return True
        
        if adm == True:
            print("Menu ADM:")
            print("1- Modificar")
            print("2- Excluir")
            print("3- Sair")
            option = input(int())
            if option == 1:
                print("Insira o cpf do usuario que deseja: ")
                nome = input()
                print(self.getCPF())
