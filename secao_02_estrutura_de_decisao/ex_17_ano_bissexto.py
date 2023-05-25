"""
Exercício 17 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não
bissexto.
    >>> eh_ano_bissexto(400)
    True
    >>> eh_ano_bissexto(800)
    True
    >>> eh_ano_bissexto(2100)
    False
    >>> eh_ano_bissexto(2004)
    True
    >>> eh_ano_bissexto(2022)
    False

"""


def eh_ano_bissexto(ano: int):
    """Escreva aqui em baixo a sua solução"""
    resto_4 = ano % 4
    resto_100 = ano % 100
    resto_400 = ano % 400
    
    if resto_4 == 0 and resto_100 != 0:
            print('True')
    elif resto_4 == 0 and resto_100 == 0 and resto_400 == 0:
            print('True')
    else:
        print('False')