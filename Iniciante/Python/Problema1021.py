'''
    Leia um valor de ponto flutuante com duas casas
    decimais. Este valor representa um valor monetario.
    A seguir, calcule o menor numero de notas e moedas
    possiveis no qual o valor pode ser decomposto. As
    notas consideradas sao de  100, 50, 20, 10, 5 e 2.
    As moedas possiveis sao de 1, 0.50, 0.25, 0.10,
    0.05 e 0.01. A seguir mostre a relacao de notas
    necessarias.

    Entrada: o arquivo de entrada contem um valor de
    ponto flutunte N(0 <= N <= 1000000.00).

    Saida: imprima a quantidade minima de notas e moedas
    necessarias para trocar o valor inicial, conforme 
    exemplo fornecido.
    
    Obs: utilize ponto(.) para separa a parte decimal.
'''

valor = float(input())

print('NOTAS:')

cem = int(valor / 100)
sobra = valor % 100

print(f'{cem} nota(s) de R$ 100.00')

cinquenta = int(sobra / 50)
sobra = sobra % 50

print(f'{cinquenta} nota(s) de R$ 50.00')

vinte = int(sobra / 20)
sobra = sobra % 20

print(f'{vinte} nota(s) de R$ 20.00')

dez = int(sobra / 10)
sobra = sobra % 10

print(f'{dez} nota(s) de R$ 10.00')

cinco = int(sobra / 5)
sobra = sobra % 5

print(f'{cinco} nota(s) de R$ 5.00')

dois = int(sobra / 2)
sobra = sobra % 2

print(f'{dois} nota(s) de R$ 2.00')
print('MOEDAS:')

um = int(sobra / 1)
sobra = sobra % 1

sobra *= 100

print(f'{um} moeda(s) de R$ 1.00')

cinCent = int(sobra / 50)
sobra = sobra % 50

print(f'{cinCent} moeda(s) de R$ 0.50')

vinCinCent = int(sobra / 25)
sobra = sobra % 25

print(f'{vinCinCent} moeda(s) de R$ 0.25')

dezCent = int(sobra / 10)
sobra = sobra % 10

print(f'{dezCent} moeda(s) de R$ 0.10')

cincoCent = int(sobra / 5)
sobra = sobra % 5

print(f'{cincoCent} moeda(s) de R$ 0.05')

umCent = int(sobra)

print(f'{umCent} moeda(s) de R$ 0.01')
