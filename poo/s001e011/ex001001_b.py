# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

from ex001001_a import CAMINHO_ARQUIVO, Pessoa


with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    pessoas = json.load(arquivo)

    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])

    print(f'nome: {p1.nome} - idade: {p1.idade}')
    print(f'nome: {p2.nome} - idade: {p2.idade}')
