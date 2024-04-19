# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
from dataclasses import asdict, astuple, dataclass


# @dataclass(repr=True)
@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    
    # @property
    # def nome_completo(self):
    #     return f'{self.nome} {self.sobrenome}'
     
    # @nome_completo.setter
    # def nome_completo(self, valor):
    #     nome, *sobrenome = valor.split()
    #     self.nome = nome
    #     self.sobrenome = ' '.join(sobrenome)
    
    # def __init__(self, nome, sobrenome):
    #     self.nome = nome
    #     self.sobrenome = sobrenome
    #     self.nome_completo = f'{self.nome} {self.sobrenome}'
    
    # def __post_init__(self):
    #     self.nome_completo = f'{self.nome.upper()} {self.sobrenome.upper()}'


if __name__ == '__main__':
    p1 = Pessoa('Luiz', 'Otávio')
    print(asdict(p1).keys())
    print(asdict(p1).values())
    print(asdict(p1).items())
    print(astuple(p1)[0])
