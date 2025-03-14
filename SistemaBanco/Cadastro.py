from cliente import Cliente

class Usuario(Cliente):
    def __init__(self, nome, cpf, RG, endereco, dataNascimento, email, senha, cargo, idConta = None):
        super().__init__(nome, cpf, RG, endereco, dataNascimento,cargo, idConta)
        self.__email = email
        self.__senha = senha
        self.__contas = []

    def getEmail(self):
        return self.__email
    
    def setEmail(self, newEmail):
        self.__email = newEmail
    
    def getSenha(self):
        return self.__senha

    def setSenha(self, newPass):
        self.__senha = newPass

    def imprima(self):
        return super().imprima() + f" Email: {self.__email}"
    
    def adicionarConta(self, conta):
        if isinstance(conta, Usuario):
            self.__contas.append(conta)
            return True
    
    def removerConta(self, cpf):
        for conta in self.__contas:
            if conta.getCPF() == cpf:
                self.__contas.remove(conta)
                return True
        return False
        
    def Listar_contas(self):
        for conta in self.__contas:
            conta.imprima()
    
    def ModificarConta(self, cpf):
        for conta in self.__contas:
            if conta.getCPF() == cpf:
                print(f"Olá {self.__nome}, Conta: {self.__idConta}")
    
    def Login(self):
        if super().getNome() == "admin":
            print(f"Administrador Detectado, insira sua senha: ")
            senha = input("password: ")
            if senha == "root":
                return True

