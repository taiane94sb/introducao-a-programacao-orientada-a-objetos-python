# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
class Pessoa:
    cpf = '1234'

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print('Classe PESSOA')
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Cliente(Pessoa):
    def falar_nome_classe(self):
        print('Classe CLIENTE')
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Aluno(Pessoa):
    cpf = 'cpf aluno'
    ...


# help(Pessoa)
# help(Cliente)
# help(Aluno)
# print()

c1 = Cliente('Luiz', 'Otávio')
print(c1.nome)
print(c1.sobrenome)
print(c1.cpf)
print()

a1 = Aluno('Maria', 'Helena')
print(a1.nome)
print(a1.sobrenome)
print(a1.cpf)
print()

c1.falar_nome_classe()
a1.falar_nome_classe()
