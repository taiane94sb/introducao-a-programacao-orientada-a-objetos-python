# Problema dos parâmetros mutáveis em funções Python
def adiciona_clientes(nome, lista=None):
    if lista is None:
        print('Lista vazia...')
        lista = []
    lista.append(nome)
    return lista


cliente1 = adiciona_clientes('Taiane')
adiciona_clientes('Matheus', cliente1)
adiciona_clientes('Sueli', cliente1)
cliente1.append('José')

cliente2 = adiciona_clientes('Cilene')
adiciona_clientes('Simone', cliente2)

cliente3 = adiciona_clientes('Constança')
adiciona_clientes('Carminha', cliente3)

print(cliente1)
print(cliente2)
print(cliente3)
