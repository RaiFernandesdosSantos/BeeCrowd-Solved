"""
    Leia 2 valores com uma casa decimal (x e y), que devem representar 
    as coordenadas de um ponto em um plano. A seguir, determine qual 
    o quadrante ao qual pertence o ponto, ou se está sobre um dos eixos
    cartesianos ou na origem (x = y = 0).

    Se o ponto estiver na origem, escreva a mensagem “Origem”.

    Se o ponto estiver sobre um dos eixos escreva “Eixo X” ou “Eixo Y”, 
    conforme for a situação.

    Entrada: A entrada contem as coordenadas de um ponto.

    Saida: A saída deve apresentar o quadrante em que o ponto se encontra.
"""

linha = input().split(" ")

pUm, pDois = linha

pUm = float(pUm)
pDois = float(pDois)

if pUm == 0 and pDois == 0:
    print("Origem")
elif pUm == 0:
    print("Eixo Y")
elif pDois == 0:
    print("Eixo X")
elif pUm > 0 and pDois > 0:
    print("Q1")
elif pUm < 0 and pDois > 0:
    print("Q2")
elif pUm < 0 and pDois < 0:
    print("Q3")
elif pUm > 0 and pDois < 0:
    print("Q4")
