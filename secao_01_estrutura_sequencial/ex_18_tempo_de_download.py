"""
Exercício 18 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
Arredonde o tempo em minutos

    >>> from secao_01_estrutura_sequencial import ex_18_tempo_de_download
    >>> numeros =['50', '2500']
    >>> ex_18_tempo_de_download.input = lambda k: numeros.pop()
    >>> ex_18_tempo_de_download.calcular_tempo_de_download()
    O tempo aproximado do Download é: 7 minuto(s)
    >>> numeros =['100', '2500']
    >>> ex_18_tempo_de_download.input = lambda k: numeros.pop()
    >>> ex_18_tempo_de_download.calcular_tempo_de_download()
    O tempo aproximado do Download é: 3 minuto(s)

"""


def calcular_tempo_de_download():
    """Escreva aqui em baixo a sua solução"""

    # 1 peça o tamanho de um arquivo para download (em MB)
    tamanho_do_arquivo = int(input(f'Qual o tamanho do arquivo? '))
    
    # 2 velocidade de um link de Internet (em Mbps)
    velocidade_da_internet = int(input(f'Qual a velocidade da internet? '))
    tamanho_do_arquivo_em_Mb = tamanho_do_arquivo * 8
    tempo_de_download_segundos = tamanho_do_arquivo_em_Mb / velocidade_da_internet 
    tempo_de_download_minutos = round(tempo_de_download_segundos / 60)

    # output
    ##1 informe o tempo aproximado de download do arquivo (minutos), Arredonde o temp
    print(f'Tempo aproximado do Download é: {tempo_de_download_minutos} minuto(s)')
