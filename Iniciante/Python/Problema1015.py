'''
    Leia os quatro valores correspondentes aos eixos x e y 
    de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) 
    e calcule a distância entre eles, mostrando 4 casas decimais 
    após a vírgula, segundo a fórmula:
    Distancia = raiz((x2 - x1)^2 + (y2 - y1)^2)

    Entrada: o arquivo de entrada contém duas linhas de dados. 
    A primeira linha contém dois valores de ponto flutuante: 
    x1 y1 e a segunda linha contém dois valores de ponto 
    flutuante x2 y2.

    Saida: calcule e imprima o valor da distância segundo a 
    fórmula fornecida, com 4 casas após o ponto decimal. 
'''
import math

linha1 = input().split(" ")
linha2 = input().split(" ")

x1, y1 = linha1
x2, y2 = linha2

distancia = math.sqrt((math.pow((float(x2) - float(x1)), 2) + math.pow((float(y2) - float(y1)), 2)))

print('{:.4f}'.format(distancia))