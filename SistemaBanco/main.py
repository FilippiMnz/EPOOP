from Cadastro import *

cliente1 = Usuario("Lipe", 99999999, 666666666, "Rua Mariano procopio numero 37", "21/07/2005", "negobomba@gmail.com", "curiosidadeMaxima")
print(cliente1.imprima())

cliente1.setNome("Hominho")
print(cliente1.imprima())


print("Welcome to the los pollos hermanos")
print("Select your option: ")
print(
    "1- Cadastrar"
    "\n2- Fazer Login"
    )
opcao = input(int())

if opcao == 1:
    print("fazer Cadastro")
elif opcao == 2:
    print("fazer Login")

