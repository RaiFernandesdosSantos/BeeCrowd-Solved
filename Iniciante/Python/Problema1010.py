'''
    Neste problema, deve-se ler o código de uma peça 1, 
    o número de peças 1, o valor unitário de cada peça 1, 
    o código de uma peça 2, o número de peças 2 e o valor 
    unitário de cada peça 2. Após, calcule e mostre o valor 
    a ser pago.
    
    Entrada: o arquivo de entrada contém duas linhas de dados. 
    Em cada linha haverá 3 valores, respectivamente dois inteiros 
    e um valor com 2 casas decimais.
    
    Saida: a saída deverá ser uma mensagem conforme o exemplo 
    fornecido abaixo, lembrando de deixar um espaço após os 
    dois pontos e um espaço após o "R$". O valor deverá ser 
    apresentado com 2 casas após o ponto.
'''

prod1 = input().split(" ")
prod2 = input().split(" ")

cod1, qtde1, valor1 = prod1
cod2, qtde2, valor2 = prod2

total = (int(qtde1) * float(valor1)) + (int(qtde2) * float(valor2))

print('VALOR A PAGAR: R$ {:.2f}'.format(total))