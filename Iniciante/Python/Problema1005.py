'''
    Leia 2 valores de ponto flutuante de dupla precisão 
    A e B, que correspondem a 2 notas de um aluno. A 
    seguir, calcule a média do aluno, sabendo que a 
    nota A tem peso 3.5 e a nota B tem peso 7.5 (A 
    soma dos pesos portanto é 11). Assuma que cada nota 
    pode ir de 0 até 10.0, sempre com uma casa decimal.
    
    Entrada: o arquivo de entrada contém 2 valores com 
    uma casa decimal cada um.
    
    Saida: imprima a mensagem "MEDIA" e a média do aluno 
    conforme exemplo abaixo, com 5 dígitos após o ponto decimal 
    e com um espaço em branco antes e depois da igualdade. 
    Utilize variáveis de dupla precisão (double) e como todos o
    s problemas, não esqueça de imprimir o fim de linha após o 
    resultado, caso contrário, você receberá "Presentation Error".
'''

n1 = float(input())
n2 = float(input())
media = ((n1 * 3.5) + (n2 * 7.5)) / 11

if media > 10:
    media -= 1

print('MEDIA = {:.5f}'.format(media))