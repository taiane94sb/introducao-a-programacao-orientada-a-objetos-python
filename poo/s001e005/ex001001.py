# Escopo da classe e de métodos da classe
class Animal:
    # nome = 'Leão'

    def __init__(self, nome):
        self.nome = nome

        variavel = 'valor'
        print(variavel)

    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}'

    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)


# print(Animal.nome)
leao = Animal(nome='Leão')
print(leao.nome)
print(leao.comendo(alimento='carne'))
print(leao.comendo('carne'))
print(leao.executar(alimento='carne'))
print(leao.executar('carne'))
