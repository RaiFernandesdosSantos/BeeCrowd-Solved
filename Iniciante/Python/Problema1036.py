"""
    Leia 3 valores de ponto flutuante e efetue o calculo das 
    raizes de Baskhara. Se nao for possivel calcular as raizes,
    mostre a  mensagem correspondente "Impossivel calcular", caso haja
    uma divisao por 0 ou raiz de numero negativo.

    Entrada: leia 3 numeros de ponto flutuante (double) A, B e C.

    Saida: se nao houver possibilidade de calcular as raizes, apresenta
    a mensagem "Impossivel calcular". Caso contrario, imprima o resultado
    das raizes com 5 digitos apos o ponto, com uma mensagem correspondente
    conforme exemplo abaixo.
"""

import math

linha = input().split(" ")

a, b, c = linha

a = float(a)
b = float(b)
c = float(c)

delta = (math.pow(b, 2)) - (4 * a * c)

if delta < 0 or a == 0:
    print("Impossivel calcular")
else:
    xUm = ((-1 * b) + (math.sqrt(delta))) / (2 * a)
    xDois = ((-1 * b) - (math.sqrt(delta))) / (2 * a)
    print("R1 = {:.5f}\nR2 = {:.5f}".format(xUm, xDois))
