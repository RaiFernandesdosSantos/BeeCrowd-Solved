'''
    Leia 2 valores inteiros e armazene-os nas variáveis A e B. 
    Efetue a soma de A e B atribuindo o seu resultado na variável 
    X. Imprima X conforme exemplo apresentado abaixo. Não apresente 
    mensagem alguma além daquilo que está sendo especificado e não 
    esqueça de imprimir o fim de linha após o resultado, caso contrário, 
    você receberá "Presentation Error".
    
    Entrada: a entrada contém 2 valores inteiros.
    
    Saida: imprima a mensagem "X = " (letra X maiúscula) seguido 
    pelo valor da variável X e pelo final de linha. Cuide para que 
    tenha um espaço antes e depois do sinal de igualdade, conforme 
    o exemplo abaixo.
'''

a = int(input())
b = int(input())
c = a + b
print('X = {}'.format(c))