'''
    Leia um numero inteiro, que eh o tempo de duracao em
    segundos de um determinado evento em uma fabrica, e
    informe-o expresso em formato horas:minutos:segundos

    Entrada: o arquivo de entrada contem um valor inteiro N.

    Saida: imprima o tempo lido no arquivo de entrada (segundos),
    convertido para horas:minutos:segundos, conforme exemplo
    fornecido.
'''

segundo = int(input())

horas = int(segundo / (60 * 60))
sobra = segundo % (60 * 60)

minutos = int(sobra / 60)
sobra = sobra % 60

print(f'{horas}:{minutos}:{sobra}')