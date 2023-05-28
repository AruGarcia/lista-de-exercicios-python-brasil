"""
Exercício 25 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

  "Telefonou para a vítima?"
  "Esteve no local do crime?"
  "Mora perto da vítima?"
  "Devia para a vítima?"
  "Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeito",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".

    >>> investigar('Sim','Sim','Sim','Sim','Sim')
    'Assassino'
    >>> investigar('Sim','Sim','Sim','Sim','Não')
    'Cúmplice'
    >>> investigar('Sim','Sim','Sim','Não','Não')
    'Cúmplice'
    >>> investigar('Sim','Sim','Não','Não','Não')
    'Suspeito'
    >>> investigar('Sim','Não','Não','Não','Não')
    'Inocente'
    >>> investigar('Não','Não','Não','Não','Não')
    'Inocente'

"""


def investigar(telefonou: str, estava_no_local: str, mora_perto: str, devia: str, trabalhou: str, ):
    """Escreva aqui em baixo a sua solução"""
    risco1 = 0
    risco2 = 0
    risco3 = 0
    risco4 = 0
    risco5 = 0
    

    if telefonou.lower() == 'sim':
        risco1 += 1
    else:
        pass
        
    if estava_no_local.lower() == 'sim':
        risco2 += 1
    else:
        pass
        
    if mora_perto.lower() == 'sim':
        risco3 += 1
    else:
        pass
        
    if trabalhou.lower() == 'sim':
        risco4 += 1
    else:
        pass
    
    if devia.lower() == 'sim':
        risco5 += 1
    else:
        pass

    soma = risco1 + risco2 + risco3 + risco4 + risco5
    
    if soma <= 1:
        return 'Inocente'
    elif soma == 2:
        return 'Suspeito'
    elif 3 <= soma <= 4:
        return 'Cúmplice'
    else:
        return 'Assassino'
