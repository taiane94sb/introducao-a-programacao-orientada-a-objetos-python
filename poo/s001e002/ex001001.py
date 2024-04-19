# Introdução ao método __init__ (inicializador de atributos)
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


# p1 = Pessoa()
# p1.nome = 'Taiane'
# p1.sobrenome = 'Barbosa'
p1 = Pessoa('Taiane', 'Barbosa')
print(p1)
print(p1.nome)
print(p1.sobrenome)

# p2 = Pessoa()
# p2.nome = 'Matheus'
# p2.sobrenome = 'Barbosa'
p2 = Pessoa('Matheus', 'Barbosa')
print(p2)
print(p2.nome)
print(p2.sobrenome)
