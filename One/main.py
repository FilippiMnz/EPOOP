from person import Person


if __name__ == "__main__":

    pessoa = Person("Filippi", 19)
    print(pessoa.getAge())
    print(pessoa.getName())
    pessoa.apresentar()
    pessoa.setName("Gustavo")
    pessoa.setAge(20)
    pessoa.apresentar()

