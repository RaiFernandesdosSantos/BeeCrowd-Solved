"""
*      Com base na tabela abaixo, escreva um programa que 
 *      leia o código de um item e a quantidade deste item. 
 *      A seguir, calcule e mostre o valor da conta a pagar.
 * 
 *      1 - Chachorro Quente - R$ 4,00;
 *      2 - X-Salada - R$ 4,50;
 *      3 - X-Bacon - R$ 5,00;
 *      4 - Torrada Simples - R$ 2,00;
 *      5 - Refrigerante - R$ 1,50;
 * 
 *      Entrada: O arquivo de entrada contém dois valores 
 *      inteiros correspondentes ao código e à quantidade 
 *      de um item conforme tabela acima.
 * 
 *      Saida: O arquivo de saída deve conter a mensagem 
 *      "Total: R$ " seguido pelo valor a ser pago, com 
 *      2 casas após o ponto decimal.
"""

linha = input().split(" ")

a, b = linha

a = int(a)
b = int(b)

total = 0

if a == 1:
    total = 4 * b
elif a == 2:
    total = 4.5 * b
elif a == 3:
    total = 5 * b
elif a == 4:
    total = 2 * b
elif a == 5:
    total = 1.5 * b

print("Total: R$ {:.2f}".format(total))
