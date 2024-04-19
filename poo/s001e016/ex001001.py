# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.
from functools import partial


class Foo:
    def __init__(self):
        self.public = 'isso é público'
        self._protected = 'isso é protegido'
        self.__exemplo = 'isso é private'

    def metodo_publico(self):
        print(self.public)
        print(self._protected)
        print(self.__exemplo)
        return 'metodo_publico'

    def _metodo_protected(self):
        print(self.public)
        print(self._protected)
        print(self.__exemplo)
        return '_metodo_protected'

    def __metodo_private(self):
        print(self.public)
        print(self._protected)
        print(self.__exemplo)
        return '__metodo_private'


f = Foo()
print(f.public)
print(f._protected)
# print(f.__exemplo)
print('....')

print('PUBLICO...')
print(f.metodo_publico())
print('....')

print('PROTECTED...')
print(f._metodo_protected())
print('....')

print('PRIVATE...')
# print(f.__metodo_private())
