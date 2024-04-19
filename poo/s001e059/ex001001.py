# namedtuples - tuplas imutáveis com nomes para valores
# Usamos namedtuples para criar classes de objetos que são apenas um
# agrupamento de atributos, como classes normais sem métodos, ou registros de
# bases de dados, etc.
# As namedtuples são imutáveis assim como as tuplas.
# from collections import namedtuple
from typing import NamedTuple


class Carta(NamedTuple):
    valor: str = 'VALOR'
    naipe: str = 'NAIPE'


# Carta = namedtuple(
#     'Carta', ['valor', 'naipe'],
#     defaults=['VALOR', 'NAIPE']
# )
as_espadas = Carta('A')
as_espadass = Carta('B', 'NAIPEE')

print(as_espadas._asdict())
print(as_espadass._asdict())
print(as_espadas)
print(as_espadass)
print(as_espadas[0])
print(as_espadass[0])
print(as_espadas.valor)
print(as_espadass.valor)
print(as_espadas[1])
print(as_espadass[1])
print(as_espadas.naipe)
print(as_espadass.naipe)

print()
print(as_espadas._fields)
print(as_espadass._fields)
print(as_espadas._field_defaults)
print(as_espadass._field_defaults)


for valor in as_espadas:
    print(valor)

for valor in as_espadass:
    print(valor)
