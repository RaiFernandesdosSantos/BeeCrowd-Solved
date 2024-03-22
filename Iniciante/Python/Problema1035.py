'''
    Leia 4 valores A, B, C e D. A seguir, se B for
    maior do que C e se D for maior do que A, e a
    soma de C com D for maior que a soma de A e B
    e se C e D, ambos, forem positivos e se a variavel
    A for par escrever a mensagem "Valores aceitos", senao 
    escrever "Valores nao aceitos".

    Entrada: quatro numeros inteiro A, B, C e D.

    Saida: mostre a respectiva mensagem apos a validacao
    dos numeros.
'''

valores = input().split()

a, b, c, d = valores

a = int(a)
b = int(b)
c = int(c)
d = int(d)

if b > c and d > a and (c + d) > (a + b) and c > 0 and d > 0 and a % 2 == 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')