"""
Exercício 18 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

    >>> validar_data('')
    'Data inválida'
    >>> validar_data('1')
    'Data inválida'
    >>> validar_data('1/2/2004')
    'Data válida'
    >>> validar_data('1/02/2004')
    'Data válida'
    >>> validar_data('01/02/2004')
    'Data válida'
    >>> validar_data('30/02/2004')
    'Data inválida'
    >>> validar_data('01/13/2004')
    'Data inválida'

"""


def validar_data(data: str):
    """Escreva aqui em baixo a sua solução"""
    data_list = data.split("/")
    tamanho_lista = len(data_list)

    if tamanho_lista <= 1:
        return 'Data inválida'
    else:
        dia = int(data_list[0])
        mes = int(data_list[1])
        ano = int(data_list[2]) 
        if dia == 30 and mes == 2 and ano <= 9999:
            return 'Data inválida'
        elif dia <= 31 and mes <= 12 and ano <= 9999:
            return 'Data válida'
        else:
            return 'Data inválida'
    
