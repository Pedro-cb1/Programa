import random

def adivinhe_o_numero():
    numero_secreto = random.randint(1, 20)
    tentativas = 7  
    print("Bem-vindo ao jogo 'hahaahahh, o jogo do anfitriao ")
    print("Tente adivinhar o número que estou pensando entre 1 e 20.")
    
    while tentativas > 0:
        print(f"\nVocê tem {tentativas} tentativa(s) restante(s).")
        try:
            palpite = int(input("Digite seu palpite: "))
        except ValueError:
            print("Por favor,brinque direito seu @@@@")
            continue

        if palpite == numero_secreto:
            print("Parabéns!voce podera ficar vivo ")
            break
        elif palpite < numero_secreto:
            print("O número é maior!")
        else:
            print("O número é menor!")
        
        tentativas -= 1

    if tentativas == 0:
        print(f"\nVocê perdeu!, ate nunca mais. O número secreto era {numero_secreto}.")
    print("Fim de jogo!")


adivinhe_o_numero()
