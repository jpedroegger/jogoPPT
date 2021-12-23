import random

print('Seja Bem Vindo!')

chances = 3  # Número de rodadas do jogo.
pontos_jogador = 0
pontos_programa = 0

while chances > 0:  # Loop para que o jogo volte a rodar até que as chances acabem.
    jogador = input('Faça sua jogada:\nEscolha Pedra(1), Papel(2) ou Tesoura(3) \n')
    programa = random.randint(1, 3)

# Condição para que a escolha do jogador esteja dentro dos parâmetros do jogo.
# de outro modo, o jogo exibe uma mensagem de erro e retorna com pedido de um número válido.
    if jogador.isnumeric() and int(jogador) in range(1, 4):
        jogador = int(jogador)
        chances -= 1  # Se a escolha do jogador for válida, o marcador de chances diminui em 1 ponto.
        if (jogador == 1 and programa == 3) or (jogador == 2 and programa == 1)  \
        or (jogador == 3 and programa == 2):
            pontos_jogador += 1
            print('Você venceu =)')
        elif jogador == programa:  # O impate não gera pontos para nenhum dos jogadores.
            print('Vocês impataram!')
        else:
            pontos_programa += 1
            print('Você perdeu =(')
    else:
        print('Esta não é uma opção válida!')
    # Quando as chances chegam a zero, o programa pergunta se o jogador deseja continuar ou se prefere sair o jogo.
    # Além disso, exibe a pontuação dos jogadores em um f-string.
    if chances == 0:
        print(f'\nFim de Jogo! Pontuação final:\nJogador: {pontos_jogador}\nPrograma:{pontos_programa}')
        parar = input("\nPressione ENTER para outra partida ou N para finalizar.\n")
        if parar.lower() == "n":
            break
        else:
            chances = 3
