import random

def game():
    numero = random.randint(1,100)
    # print(numero)
    print("Um número entre 1 a 100 foi sorteado! Adivinhe!")
    
    while True:
        try:
            escolha = int(input("Escreva o número: "))
        except ValueError:
            print("Digite apenas números!")
            continue
            
        if escolha < 1 or escolha > 100:
            print("Escolha um número entre 1 a 100!")    
        elif numero > escolha:
            print("Seu número é menor que o número sorteado")
        elif numero < escolha:
            print("Seu número é maior que o número sorteado")
        else:
            print("Você acertou!")
            break

game()
