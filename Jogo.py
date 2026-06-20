import random


def game():
    
    numero = random.randint(1,100)
    # print(numero)
    print("Um número entre 1 a 100 foi sorteado! Adivinhe!")
    while True:
        
        escolha = int(input("Escreva o número:"))   


    
        if escolha < 1 or escolha > 100:
            print("Escolha um número entre 1 a 100!")

        else:
            if numero > escolha:
                print("Seu número é menor que o número sorteado")
            elif numero < escolha:
                print("Seu número é maior que o número sorteado")
            else:
                print("Você acertou!")
                break

game()


# -----------------add def depois github-------------------

