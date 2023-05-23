"""
Exercício 17 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o custo seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

    >>> from secao_01_estrutura_sequencial import ex_17_loja_de_tintas_complexa
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '100'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 19 litros de tinta.
    Você pode comprar 2 lata(s) de 18 litros a um custo de R$ 160. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 6 lata(s) de 3.6 litros a um custo de R$ 150. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 1 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 105. Vão sobrar 2.6 litro(s) de tinta.
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '200'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 37 litros de tinta.
    Você pode comprar 3 lata(s) de 18 litros a um custo de R$ 240. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 11 lata(s) de 3.6 litros a um custo de R$ 275. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 2 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 185. Vão sobrar 2.6 litro(s) de tinta.

"""
import math

def calcular_latas_e_preco_de_tinta():
    """Escreva aqui em baixo a sua solução"""
#1 O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.

    area_pintada = float(input(f'Qual o tamanho da área em metros quadrados que vai ser pintada? '))

#2 Rendimento da tinta 1 litro 6 metros. Quantos litros de tinta vou usar. Acrescente 10% de folga e sempre arredonde os valores para cima

    quantidade_de_tinta = math.ceil((area_pintada / 6) * 1.1)

#3 Latas de 18 litros, que custam R$ 80,00; #2 comprar apenas latas de 18 litros;

    quantas_latas_de_18 = (quantidade_de_tinta // 18) + 1
    valor_das_latas_de_18 = quantas_latas_de_18 * 80
    quanta_tinta_sobra_18 = (18 * quantas_latas_de_18) - quantidade_de_tinta

#4 galões de 3,6 litros, que custam R$ 25,00; #3 comprar apenas galões de 3,6 litros;

    quantas_latas_de_3_6 = (quantidade_de_tinta // 3.6) + 1 
    valor_das_latas_de_3_6 = quantas_latas_de_3_6 * 25
    quanta_tinta_sobra_3_6 = ((3.6 * quantas_latas_de_3_6) - quantidade_de_tinta)

#4 misturar latas e galões, de forma que o custo seja menor.

    
