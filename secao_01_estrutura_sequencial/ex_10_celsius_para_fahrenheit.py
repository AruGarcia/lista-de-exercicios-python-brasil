"""
Exercício 10 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
Mostrar apenas valor inteiro da temperatura

    >>> from secao_01_estrutura_sequencial import ex_10_celsius_para_fahrenheit
    >>> ex_10_celsius_para_fahrenheit.input = lambda k: '0'
    >>> ex_10_celsius_para_fahrenheit.transformar_para_fahrenheit()
    Essa temperatura é de 32 Fahrenheit
    >>> ex_10_celsius_para_fahrenheit.input = lambda k: '21'
    >>> ex_10_celsius_para_fahrenheit.transformar_para_fahrenheit()
    Essa temperatura é de 70 Fahrenheit

"""


def transformar_para_fahrenheit():
    """Escreva aqui em baixo a sua solução"""
    temp_celcius = int(input(f'Qual a temperatura em graus celsius você quer passar para fahrenheit?'))
    temp_fahrenheit = (temp_celcius * 1.8) + 32
    print(f'Essa temperatura é de {temp_fahrenheit:.0f} Fahrenheit')

