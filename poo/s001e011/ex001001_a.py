# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json


CAMINHO_ARQUIVO = 's001e011/ex001001.json'


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('Taiane', 30)
p2 = Pessoa('Matheus', 25)

# bd = [vars(p1), vars(p2)]
bd = [p1.__dict__, p2.__dict__]


def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        print('FAZENDO DUMP')
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    print('__main__')
    fazer_dump()
