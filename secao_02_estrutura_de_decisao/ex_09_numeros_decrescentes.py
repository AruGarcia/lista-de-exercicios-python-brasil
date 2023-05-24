"""
Exercício 09 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia três números e mostre-os em ordem decrescente.

    >>> ordenar_decrescente(2, 3, 5)
    5, 3, 2
    >>> ordenar_decrescente(10, 5.55, 7)
    10, 7, 5.55
    >>> ordenar_decrescente(20, 30, 17.62)
    30, 20, 17.62
    >>> ordenar_decrescente(7, 1, 15)
    15, 7, 1

"""


def ordenar_decrescente(x, y, z):
    """Escreva aqui em baixo a sua solução"""
    if x > y and x > z:
        maior_num = x
    elif y > x and y > z:
        maior_num = y
    else:
        maior_num = z

    if x < y and x < z:
        menor_num = x
    elif y < x and y < z:
        menor_num = y
    else :
        menor_num = z

    if maior_num > x > menor_num:
        meio_num = x
    elif maior_num > y > menor_num:
        meio_num = y
    else:
        meio_num = z

    print(f'{maior_num}, {meio_num}, {menor_num}')

