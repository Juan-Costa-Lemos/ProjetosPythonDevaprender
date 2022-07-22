from turtle import Turtle

t = Turtle()

#velocidade
t.speed(2)
print(' ********************** Bem-vindo ao Turtle **********************')
while True:
    andar = input('Deseja andar para frente ou para trás? f:frente t:trás \n')
    if andar == 'f':
        frente = int(input('Deseja andar quantos pixel para frente?\n'))
        t.forward(frente)
        virar = input('Desaja virar para a esquerda ou para direita? e:esquerda d:direita \n')
        if virar == 'e':
            esquerda = int(input('Quantos pixels a esquerda? \n'))
            t.left(esquerda)
            t.forward(100)
        elif virar == 'd':
            direita = int(input('Quantos pixels a direita? \n'))
            t.right(direita)
            t.forward(100)
        continuar = input('Deseja continuar? s:sim n:não \n')
        if continuar == 's':
            continue
        elif continuar == 'n':
            print('Obrigado por jogar, até a proxíma!!')
            break
    elif andar == 't':
        tras = int(input('Deseja andar quantos pixel para trás?\n'))
        t.backward(tras)
        virar = input('Desaja virar para a esquerda ou para direita? e:esquerda d:direita \n')
        if virar == 'e':
            esquerda = int(input('Quantos pixels a esquerda?\n'))
            t.left(esquerda)
            t.forward(100)
        elif virar == 'd':
            direita = int(input('Quantos pixels a direita?\n'))
            t.right(direita)
            t.forward(100)
        continuar = input('Deseja continuar? s:sim n:não \n')
        if continuar == 's':
            continue
        elif continuar == 'n':
            print('Obrigado por jogar, até a proxíma!!')
            break
    

    
    
            