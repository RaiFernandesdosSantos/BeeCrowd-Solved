'''
    Faça um programa que leia três valores e apresente o maior 
    dos três valores lidos seguido da mensagem “eh o maior”. 
    Utilize a fórmula: MaiorAB = (a + b + abs(a - b)) / 2.

    Obs.: a fórmula apenas calcula o maior entre os dois primeiros 
    (a e b). Um segundo passo, portanto é necessário para chegar 
    no resultado esperado.

    Entrada: o arquivo de entrada contém três valores inteiros.

    Saida: imprima o maior dos três valores seguido por um 
    espaço e a mensagem "eh o maior".
'''

linha = input().split(" ")

a, b, c = linha
a, b, c = int(a), int(b), int(c)

maior = (a + b + abs((a - b))) / 2
resultado = (int(maior) + int(c) + abs(int(maior) - int(c)))/2

print('%d eh o maior'%resultado)