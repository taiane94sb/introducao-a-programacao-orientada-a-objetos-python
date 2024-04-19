# Enum -> Enumerações
# Enumerações na programação, são usadas em ocasiões onde temos
# um determinado número de coisas para escolher.
# Enums têm membros e seus valores são constantes.
# Enums em python:
#   - são um conjunto de nomes simbólicos (membros) ligados a valores únicos
#   - podem ser iterados para retornar seus membros canônicos na ordem de
#       definição
# enum.Enum é a superclasse para suas enumerações. Mas também pode ser usada
#   diretamente (mesmo assim, Enums não são classes normais em Python).
# Você poderá usar seu Enum com type annotations, com isinstance e
# outras coisas relacionadas com tipo.
# Para obter os dados:
# membro = Classe(valor), Classe['chave']
# chave = Classe.chave.name
# valor = Classe.chave.value

import enum

# def mover(direcao):
#     print(f'Movendo para {direcao}')
    

# mover('esquerda')
# mover('direita')
# mover('acima')
# mover('abaixo')

class Direcoes(enum.Enum):
    ESQUERDA = enum.auto()
    DIREITA = enum.auto()
    ACIMA = enum.auto()
    ABAIXO = enum.auto()
    
def mover(direcao: Direcoes):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção não encontrada')

    print(f'Movendo para {direcao.name} ({direcao.value})')


# Direcoes.ESQUERDA Direcoes.DIREITA Direcoes.ACIMA Direcoes.ABAIXO
print(Direcoes(1), Direcoes(2), Direcoes(3), Direcoes(4))
print()
# Direcoes.ESQUERDA Direcoes.DIREITA Direcoes.ACIMA Direcoes.ABAIXO
print(Direcoes['ESQUERDA'], Direcoes['DIREITA'], Direcoes['ACIMA'], Direcoes['ABAIXO'])
print()
# ESQUERDA DIREITA ACIMA ABAIXO
print(Direcoes(1).name, Direcoes(2).name, Direcoes(3).name, Direcoes(4).name)
print()
# 1 2 3 4
print(Direcoes(1).value, Direcoes(2).value, Direcoes(3).value, Direcoes(4).value)
print()

mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover(Direcoes.ACIMA)
mover('ABCD')
