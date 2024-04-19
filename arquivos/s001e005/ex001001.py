import json

pessoa = {
    'nome': 'Taiane',
    'sobrenome': 'Barbosa',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.66,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

with open('arquivos\s001e005\ex001001.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)
    print(type(pessoa))
    print('nome: ', pessoa['nome'])
    print('sobrenome: ', pessoa['sobrenome'])
    print('enderecos: ', pessoa['enderecos'])
    print('altura: ', pessoa['altura'])
    print('numeros_preferidos: ', pessoa['numeros_preferidos'])
    print('dev: ', pessoa['dev'])
    print('nada: ', pessoa['nada'])
