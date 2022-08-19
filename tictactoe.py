Tabul = {'A1': ' ', 'A2': ' ', 'A3': ' ',
         'B1': ' ', 'B2': ' ', 'B3': ' ',
         'C1': ' ', 'C2': ' ', 'C3': ' '}


Cont = []           # This list is used to acess the dict keys by their separate values
for i in (Tabul):   # Essa lista pode ser usada para acessar as chaves do dicionário por seus valores distintos
    Cont.append(i)


def printTabul(Tabul):
    # Each space on the board is represented by this function// Cada espaço no tabuleiro é representado por essa função
    print(Tabul['A1'] + '|' + Tabul['A2'] + '|' + Tabul['A3'] + '\tA1 A2 A3')
    print('-+-+-')
    print(Tabul['B1'] + '|' + Tabul['B2'] + '|' + Tabul['B3'] + '\tB1 B2 B3')
    print('-+-+-')
    print(Tabul['C1'] + '|' + Tabul['C2'] + '|' + Tabul['C3'] + '\tC1 C2 C3')


plays = 0
m = 0
print('Quem irá jogar primeiro? X ou O')
# The answer registers the first one to play// A resposta registra o primeiro jogador
rodada = input()
lastRodada = None
while plays < 9:    # This loop determines the duration of the game// Esse loop determina a duração do jogo
    printTabul(Tabul)
    try:
        resp = input('É a vez da jogada de ' + rodada +
                     ' Onde quer se posicionar?')   # The input defines the space that will be occupied on the board// O input define o espaço que vai ser ocupado no tabuleiro
        if Tabul[resp] == lastRodada:   # Condition that shows if the space choosen is occupied or not, if not, registers the answer// Condição que mostra se o espaço escolhido está ocupado ou não, senão, registra a resposta
            print('Essa posição já foi ocupada')
        else:
            try:
                Tabul[resp] = rodada
                Cont[(Cont.index(resp))] = rodada
                plays += 1
            except ValueError:
                print('Essa posição já foi ocupada')
    except KeyError:
        print('Essa posição não é válida')

    if rodada == 'X':   # Determines the order of players throughout the game// Determina a ordem de jogadores ao longo do jogo
        rodada = 'O'
        lastRodada = 'X'
    else:
        rodada = 'X'
        lastRodada = 'O'

    if plays > 2:   # This is the minimum amount of plays for someone to win// Esse é o valor mínimo de jogadas para alguém ganhar
        for j in range(0, 9, 3):    # Horizontal win conditions// Condições de vitória horizontal
            for n in range(1, 3):
                if Cont[j] == Cont[j + n]:
                    m += 1
                else:
                    break
            if m == 1:
                m = 0
            elif m == 2:
                break

        for f in range(0, 3):   # Vertical win conditions// Condições de vitória vertical
            for g in range(3, 9, 3):
                if Cont[f] == Cont[f + g]:
                    m += 1
                else:
                    break
            if m == 1:
                m = 0
            elif m == 2:
                break

        # Left diagonal win condition// Condição de vitória da diagonal esquerda
        for l in range(0, 8, 4):
            if Cont[l] == Cont[(l + 4)]:
                m += 1
            else:
                break
        if m == 1:
            m = 0

        # Right diagonal win condition//Condição de vitória da diagonal direita
        for p in range(2, 6, 2):
            if Cont[p] == Cont[(p + 2)]:
                m += 1
            else:
                break
        if m == 1:
            m = 0

    # If any of the win conditions is satisfied, they make m == 2// Se qualquer uma das condições de vitória for satisfeita, elas tornam m == 2
    if m == 2:
        print(lastRodada + ' ganhou!')
        break
printTabul(Tabul)
