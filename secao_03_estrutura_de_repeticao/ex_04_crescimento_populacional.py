"""
Exercício 04 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a
população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o
número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas
de crescimento.

    >>> calcular_ano_ultrapassagem_populacional()
    'População de A, depois de 63 ano(s) será de 515033 pessoas, superando a de B, que será de 510964 pessoas'


"""


def calcular_ano_ultrapassagem_populacional() -> str:
    """Escreva aqui em baixo a sua solução"""
    pop_a = 80000
    pop_b = 200000
    ano = 0

    while int(pop_a) <= int(pop_b):
        ano += 1
        pop_a += (pop_a * 0.03)
        pop_b += (pop_b * 0.015)
    return (f'População de A, depois de {ano} ano(s) será de {pop_a:.0f} pessoas, superando a de B, que será de {pop_b:.0f} pessoas')




