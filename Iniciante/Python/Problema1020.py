'''
    Leia um valor inteiro correspondete a idade de uma pessoa
    em dias e informe-a em anos, meses e dias.

    Obs: apenas para facilitar o calculo, considere todo o ano
    com 365 dias e todo mes com 30 dias. Nos casos de teste nunca
    havera uma situacao que permita 12 e alguns dias, como 360, 363
    ou 364. Este e apenas um exercicio com o objetivo de testar
    raciocinio matematico simples.

    Entrada: o arquivo de entrada contem um valor inteiro.

    Saida: imprima a saida conforme exemplo fornecido.
'''

idade = int(input())

anos = int(idade / 365)
sobra = idade % 365

meses = int(sobra / 30)
sobra = sobra % 30

dias = sobra

print(f'{anos} ano(s)\n{meses} mes(es)\n{dias} dia(s)')
