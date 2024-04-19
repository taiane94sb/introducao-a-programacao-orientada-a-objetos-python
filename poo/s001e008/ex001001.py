# Atributos de classe
class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


# p1 = Pessoa('Taiane', 30)
# p2 = Pessoa('Matheus', 25)

dados = {'nome': 'João', 'idade': 35}
p1 = Pessoa(**dados)
print(p1.nome)
print(p1.idade)
p1.nome = 'EITA1'
print(p1.nome)
print(p1.idade)
p1.__dict__['outra'] = 'coisa'
print(p1.nome)
print(p1.idade)
print(p1.outra)
p1.__dict__['nome'] = 'EITA2'
print(p1.nome)
print(p1.idade)
print(p1.outra)
del p1.__dict__['outra']
print(p1.__dict__)
print(vars(p1))
print(p1.nome)
print(p1.idade)
