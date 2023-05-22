"""
Exercício 03 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que peça as 4 notas bimestrais e mostre a média.

    >>> from secao_01_estrutura_sequencial import ex_04_notas_bimestrais
    >>> numeros =['7', '8','9','10']
    >>> ex_04_notas_bimestrais.input = lambda k: numeros.pop()
    >>> ex_04_notas_bimestrais.calcular_media()
    A média anual é 8.5

"""


def calcular_media():
    """Escreva aqui em baixo a sua solução"""
    nota01=int(input('Insira a nota do primeiro bimestre: '))
    nota02=int(input('Insira a nota do segundo bimestre: '))
    nota03=int(input('Insira a nota do terceiro bimestre: '))
    nota04=int(input('Insira a nota do último bimestre: '))
    media= (nota01+nota02+nota03+nota04)/4
    print(f'A média anual é {media}')
