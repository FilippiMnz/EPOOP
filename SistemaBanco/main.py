from Cadastro import *

cliente1 = Usuario("Lipe", 99999999, 666666666, "Rua Mariano procopio numero 37", "21/07/2005", "negobomba@gmail.com", "curiosidadeMaxima")
print(cliente1.imprima())

cliente1.setNome("Hominho")
print(cliente1.imprima())