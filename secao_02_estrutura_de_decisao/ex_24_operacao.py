"""
Exercício 24 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da
operação deve ser acompanhado de uma frase que diga se o número é:
  par ou ímpar;
  positivo ou negativo;
  inteiro ou decimal.

Mostre o restultado com duas casas decimais

    >>> fazer_operacao_e_classificar(2, 3, '+')
    Resultado: 5.00
    Número é impar, positivo e inteiro.
    >>> fazer_operacao_e_classificar(-4, 2, '/')
    Resultado: -2.00
    Número é par, negativo e inteiro.
    >>> fazer_operacao_e_classificar(0, 2, '*')
    Resultado: 0.00
    Número é par, neutro e inteiro.
    >>> fazer_operacao_e_classificar(-3.14, 2, '*')
    Resultado: -6.28
    Número é negativo e decimal.
    >>> fazer_operacao_e_classificar(3.14, 2, '-')
    Resultado: 1.14
    Número é positivo e decimal.

"""


def fazer_operacao_e_classificar(n_1: float, n_2: float, operacao: str):
    """Escreva aqui em baixo a sua solução"""
    
    
    resultado = None
    par_ou_impar = None
    posi_neg = None
    int_dec = None
    int_dec = None
    

    if operacao == '+':
        resultado = (n_1 + n_2)
    elif operacao == '-':
        resultado = (n_1 - n_2)
    elif operacao == '/':
        resultado = (n_1 / n_2)
    else:
        resultado = (n_1 * n_2)

    resultado_round = round(resultado)

    #Número é impar, positivo e inteiro.


    if resultado == 0:
        par_ou_impar = 'par, '
        posi_neg = 'neutro'
        int_dec = 'inteiro'

    elif resultado == resultado_round:

        if resultado % 2 == 0:
            par_ou_impar = 'par, '
        else:
            par_ou_impar = 'impar, '

        if resultado < 0:
            posi_neg = 'negativo'
        else:
            posi_neg = 'positivo'

        int_dec = 'inteiro'

    elif resultado != resultado_round:

        par_ou_impar = ''

        if resultado < 0:
            posi_neg = 'negativo'
        else:
            posi_neg = 'positivo'

        int_dec = 'decimal'

    else:
        par_ou_impar = 'nulo, '
        
        if resultado < 0:
            posi_neg = 'negativo'
        else:
            posi_neg = 'positivo'

        int_dec = 'decimal'

    #Número é impar, positivo e inteiro.

    print(f'Resultado: {resultado:.2f}')
    print(f'Número é {par_ou_impar}{posi_neg} e {int_dec}.')
