'''
    Leia um valor inteiro. A seguir, calcule o menor numero de notas 
    possiveis (cedulas) no qual o valor pode ser decomposto. As notas
    consideradas sao de 100, 50, 20, 10, 5, 2, 1. A seguir mostre o
    valor lido e a relacao de notas necessarias.

    Entrada: o arquivo contem um valor inteiro N(0 < N < 1000000).

    Saida: imprima o valor lido e, em seguida, a quantidade minima de 
    cada tipo necessarias, conforme o exemplo fornecido. Nao esqueca 
    de imprimir o fim de linha apos cada linha, caso contrario 
    seu programa apresentara a mensagem: "Presetation error".
'''

valor = int(input())

print(valor)

cem = int(valor / 100)
sobra = valor % 100

print(f'{cem} nota(s) de R$ 100,00')

cinquenta = int(sobra / 50)
sobra = sobra % 50

print(f'{cinquenta} nota(s) de R$ 50,00')

vinte = int(sobra / 20)
sobra = sobra % 20

print(f'{vinte} nota(s) de R$ 20,00')

dez = int(sobra / 10)
sobra = sobra % 10

print(f'{dez} nota(s) de R$ 10,00')

cinco = int(sobra / 5)
sobra = sobra % 5

print(f'{cinco} nota(s) de R$ 5,00')

dois = int(sobra / 2)
sobra = sobra % 2

print(f'{dois} nota(s) de R$ 2,00')

um = sobra

print(f'{um} nota(s) de R$ 1,00')
