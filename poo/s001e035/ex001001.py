# __new__ e __init__ em classes Python
# __new__ é o método responsável por criar e
# retornar o novo objeto. Por isso, new recebe cls.
# __new__ ❗️DEVE retornar o novo objeto❗️
# __init__ é o método responsável por inicializar
# a instância. Por isso, init recebe self.
# __init__ ❗️NÃO DEVE retornar nada (None)❗️
# object é a super classe de uma classe
class A:
    def __new__(cls, *args, **kwargs):
        instancia = super().__new__(cls)
        print('Sou o new', instancia)
        return instancia

    def __init__(self, x):
        self.x = x
        print('Sou o init', x)

    def __repr__(self):
        print('Sou o repr')
        return 'A()'


a = A(123)
print(a)
# Sou o new Sou o repr
# A()
# Sou o init 123
# Sou o repr
# A()
