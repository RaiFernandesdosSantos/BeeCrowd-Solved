'''
    Leia 3 valores inteiros e ordene-os em ordem crescente.
    No final, mostre os valores em ordem crescente, uma linha
    em branco e em seguida. Os valores na sequencia como foram lidos.

    Entrada: A entrada contem três valores inteiros.

    Saida: Imprima a saida conforme foi especificada.
'''

linha = input().split(" ")

a, b, c = linha
a1, b1, c1 = int(a), int(b), int(c)

for i in range(3):
    if a1 > b1:
        a1, b1 = b1, a1
    elif a1 > c1:
        a1, c1 = c1, a1
    elif b1 > c1:
        b1, c1 = c1, b1

print(str(a1) + '\n' + str(b1) + '\n' + str(c1))
print('\n' + a + '\n' + b + '\n' + c)