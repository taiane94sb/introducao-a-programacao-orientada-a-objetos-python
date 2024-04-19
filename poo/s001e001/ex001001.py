# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
string = 'Luiz'
print(string)
print(string.lower())
print(string.upper())
print(isinstance(string, str))


class Pessoa:
    ...


p1 = Pessoa()
p1.nome = 'Taiane'
p1.sobrenome = 'Barbosa'
print(p1)
print(p1.nome)
print(p1.sobrenome)

p2 = Pessoa()
p2.nome = 'Matheus'
p2.sobrenome = 'Barbosa'
print(p2)
print(p2.nome)
print(p2.sobrenome)
