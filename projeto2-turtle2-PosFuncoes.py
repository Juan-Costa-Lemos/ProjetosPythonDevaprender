from turtle import Turtle

t = Turtle()

t.speed(2)
print(' ********************** Bem-vindo ao Turtle **********************')

def rotacionar():
    lado = input('Desaja virar para a esquerda ou para direita? e:esquerda d:direita \n')
    if lado == 'e':
            esquerda = rotarcionar_esquerda(t)
            t.left(esquerda)
    elif lado == 'd':
           direita = rotarcionar_direita(t)
           t.right(direita)
    return lado

def movimentar_frente(turtle):
    frente = int(input('Deseja andar quantos pixel para frente?\n'))
    return frente      

def movimentar_tras(turtle):
    tras = int(input('Deseja andar quantos pixel para trás?\n'))
    t.backward(tras)
    return tras

def rotarcionar_esquerda(turtle):
    esquerda = int(input('Quantos pixels a esquerda? \n'))
    return esquerda

def rotarcionar_direita(turtle):
    direita = int(input('Quantos pixels a direita? \n'))
    t.forward(100)
    return direita

def continuar_jogando():
    continuar = input('Deseja continuar? s:sim n:não \n')
    return continuar

while True:
    andar = input('Deseja andar para frente ou para trás? f:frente t:trás \n')
    if andar == 'f':
        frente = movimentar_frente(t)
        t.forward(frente)
        rotacionar()

        continuar = continuar_jogando()
        if continuar == 's':
            continue
        elif continuar == 'n':
            print('Obrigado por jogar, até a próxima!!')
            break
    elif andar == 't':
        tras = movimentar_tras(t)
        t.backward(tras)
        rotacionar()
        continuar = continuar_jogando()
        if continuar == 's':
            continue
        elif continuar == 'n':
            print('Obrigado por jogar, até a próxima!!')
            break