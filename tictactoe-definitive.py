Tabul = {'A1': ' ', 'A2': ' ', 'A3': ' ',
         'B1': ' ', 'B2': ' ', 'B3': ' ',
         'C1': ' ', 'C2': ' ', 'C3': ' '}


Cont = []           # This list is used to acess the dict keys by their separate values
for i in (Tabul):   # Essa lista pode ser usada para acessar as chaves do dicionário por seus valores distintos
    Cont.append(i)


def printTabul(Tabul):
    # Each space on the board is represented by this function
    print(Tabul['A1'] + '|' + Tabul['A2'] + '|' + Tabul['A3'] + '\tA1 A2 A3')
    # Cada espaço no tabuleiro é representado por essa função
    print('-+-+-')
    print(Tabul['B1'] + '|' + Tabul['B2'] + '|' + Tabul['B3'] + '\tB1 B2 B3')
    print('-+-+-')
    print(Tabul['C1'] + '|' + Tabul['C2'] + '|' + Tabul['C3'] + '\tC1 C2 C3')


i = 0
m = 0
print('Quem irá jogar primeiro? X ou O')
rodada = input()
while i < 9:
    printTabul(Tabul)
    resp = input('É a vez da jogada de ' + rodada +
                 ' Onde quer se posicionar?')
    if Tabul[resp] == lastRodada:
        print('Essa posição já foi ocupada')
    else:
        try:
            Tabul[resp] = rodada
            Cont[(Cont.index(resp))] = rodada
            i += 1
        except ValueError:
            print('Essa posição já foi ocupada')

    if rodada == 'X':
        rodada = 'O'
        lastRodada = 'X'
    else:
        rodada = 'X'
        lastRodada = 'O'

    if i > 2:
        for j in range(0, 9, 3):
            for n in range(1, 3):
                if Cont[j] == Cont[j + n]:
                    m += 1
                else:
                    break
            if m == 1:
                m = 0
            elif m == 2:
                break

        for f in range(0, 2):
            for g in range(3, 9, 3):
                if Cont[f] == Cont[f + g]:
                    m += 1
                else:
                    break
            if m == 1:
                m = 0
            elif m == 2:
                break

        for l in range(0, 8, 4):
            if Cont[l] == Cont[(l + 4)]:
                m += 1
            else:
                break
        if m == 1:
            m = 0

        for p in range(2, 6, 2):
            if Cont[p] == Cont[(p + 2)]:
                m += 1
            else:
                break
        if m == 1:
            m = 0

    if m == 2:
        print(lastRodada + ' ganhou!')
        break
printTabul(Tabul)
