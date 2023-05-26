"""
Exercício 21 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo
é de 1 real e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma
nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,
uma nota de 5 e quatro notas de 1.

    >>> calcular_troco(256)
    '2 notas de R$ 100, 1 nota de R$ 50, 1 nota de R$ 5 e 1 nota de R$ 1'
    >>> calcular_troco(1)
    '1 nota de R$ 1'
    >>> calcular_troco(5)
    '1 nota de R$ 5'
    >>> calcular_troco(10)
    '1 nota de R$ 10'
    >>> calcular_troco(11)
    '1 nota de R$ 10 e 1 nota de R$ 1'
    >>> calcular_troco(399)
    '3 notas de R$ 100, 1 nota de R$ 50, 4 notas de R$ 10, 1 nota de R$ 5 e 4 notas de R$ 1'
"""


def calcular_troco(valor: int) -> str:
    """Escreva aqui em baixo a sua solução"""
    
    num_notas_100 = valor // 100
    num_notas_50 = int(((valor % 100) // 10) / 5)
    num_notas_10 = int((valor % 100) // 10 - (num_notas_50 * 5))
    num_notas_5 = int((valor % 10) / 5)
    num_notas_1 = int((valor % 10) - (num_notas_5 * 5))

    if 100 <= valor <= 600:
        if num_notas_50 == 0 and num_notas_10 == 0 and num_notas_5 == 0 and num_notas_1 == 0:
            print(f"'{num_notas_100} nota de R$ 100'")

        elif num_notas_50 > 0 and num_notas_10 == 0 and num_notas_5 == 0 and num_notas_1 == 0:
            print(f"'{num_notas_100} notas de R$ 100 e {num_notas_50} nota de R$ 50'")
        
        elif num_notas_50 > 0 and num_notas_10 > 0 and num_notas_5 == 0 and num_notas_1 == 0:
            print(f"'{num_notas_100} notas de R$ 100, {num_notas_50} nota de R$ 50 e {num_notas_10} notas de R$ 10'")

        elif num_notas_50 > 0 and num_notas_10 == 0 and num_notas_5 > 0 and num_notas_1 == 0:
            print(f"'{num_notas_100} notas de R$ 100, {num_notas_50} nota de R$ 50, e {num_notas_5} notas de R$ 5'")

        elif num_notas_50 > 0 and num_notas_10 == 0 and num_notas_5 > 0 and num_notas_1 > 0:
            print(f"'{num_notas_100} notas de R$ 100, {num_notas_50} nota de R$ 50, {num_notas_5} nota de R$ 5 e {num_notas_1} nota de R$ 1'")

        elif num_notas_50 > 0 and num_notas_10 > 0 and num_notas_5 > 0 and num_notas_1 == 0:
            print(f"'{num_notas_100} notas de R$ 100, {num_notas_50} nota de R$ 50, {num_notas_10} notas de R$ 10 e {num_notas_5} notas de R$ 5'")
        
        else: # num_notas_50 > 0 and num_notas_10 > 0 and num_notas_5 > 0 and num_notas_1 > 0:
            print(f"'{num_notas_100} notas de R$ 100, {num_notas_50} nota de R$ 50, {num_notas_10} notas de R$ 10, {num_notas_5} notas de R$ 5 e {num_notas_1} notas de R$ 1'")
        
    elif 99 <= valor <= 1:

        if num_notas_50 > 0 and num_notas_10 == 0 and num_notas_5 == 0 and num_notas_1 == 0:
                print(f"'{num_notas_50} nota de R$ 50'")

        elif num_notas_50 > 0 and num_notas_10 > 0 and num_notas_5 == 0 and num_notas_1 == 0:
                print(f"'{num_notas_50} nota de R$ 50, {num_notas_10} e notas de R$ 10'")
            
        elif num_notas_50 > 0 and num_notas_10 > 0 and num_notas_5 > 0 and num_notas_1 == 0:
                print(f"'{num_notas_50} nota de R$ 50, {num_notas_10} notas de R$ 10 e {num_notas_5} notas de R$ 5'")
        
        elif num_notas_50 > 0 and num_notas_10 > 0 and num_notas_5 > 0 and num_notas_1 > 0:
                print(f"'{num_notas_50} nota de R$ 50, {num_notas_10} notas de R$ 10, {num_notas_5} notas de R$ 5 e {num_notas_1} notas de R$ 1'")

            
            
        elif num_notas_50 == 0 and num_notas_10 > 0 and num_notas_5 == 0 and num_notas_1 == 0:
            print(f"'{num_notas_10} e notas de R$ 10'")

        elif num_notas_50 == 0 and num_notas_10 > 0 and num_notas_5 > 0 and num_notas_1 == 0:
            print(f"'{num_notas_10} notas de R$ 10 e {num_notas_5} notas de R$ 5'")
            
        elif num_notas_50 == 0 and num_notas_10 > 0 and num_notas_5 > 0 and num_notas_1 > 0:
            print(f"'{num_notas_10} notas de R$ 10, {num_notas_5} notas de R$ 5 e {num_notas_1} notas de R$ 1'")



        elif num_notas_50 == 0 and num_notas_10 == 0 and num_notas_5 > 0 and num_notas_1 == 0:
            print(f"'{num_notas_5} notas de R$ 5'")
            
        else: #num_notas_50 == 0 and num_notas_10 == 0 and num_notas_5 > 0 and num_notas_1 > 0:
            print(f"'{num_notas_5} notas de R$ 5 e {num_notas_1} notas de R$ 1'")
            
    else:
        print(f"'{num_notas_1} nota de R$ 1'")