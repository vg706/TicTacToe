from re import X


Tabul = {'A1': ' ', 'A2': ' ', 'A3': ' ',
         'B1': ' ', 'B2': ' ', 'B3': ' ',
         'C1': ' ', 'C2': ' ', 'C3': ' '}

Cont = []


def printTabul(Tabul):
    print(Tabul['A1'] + '|' + Tabul['A2'] + '|' + Tabul['A3'] + '\tA1 A2 A3')
    print('-+-+-')
    print(Tabul['B1'] + '|' + Tabul['B2'] + '|' + Tabul['B3'] + '\tB1 B2 B3')
    print('-+-+-')
    print(Tabul['C1'] + '|' + Tabul['C2'] + '|' + Tabul['C3'] + '\tC1 C2 C3')


i = 1
print('Quem irá jogar primeiro? X ou O')
rodada = input()
while i < 9:
    printTabul(Tabul)
    lastRodada = rodada
    resp = input('É a vez da jogada de ' + rodada +
                 ' Onde quer se posicionar?')
    if Tabul[resp] == rodada:
        if Tabul[resp] == lastRodada:
            print('Essa posição já foi ocupada')
    else:
        Tabul[resp] = rodada
        i += 1
    if rodada == 'X':
        rodada = 'O'
    else:
        rodada = 'X'

# printTabul(Tabul)
# def Vit():
# print('Você ganhou!')  # + rodada)

'''''
def CondicVit():
    for k in range(9):
        if Cont[0:3]:
            if Cont[k] == Cont[(k + 1)]:
                Vit()
        elif Cont[3:6]:
            if Cont[k] == Cont[(k + 1)]:
                Vit()
        elif Cont[6:8] and Cont[-1] == True:
            if Cont[k] == Cont[(k + 1)]:
                Vit()
        elif(Cont[(k < 7)] == Cont[k + 3]):
            Vit()
    for l in range(0, 9, 4):
        if(Cont[l] == Cont[l + 1]):
            Vit()
    for m in range(2, 9, 2):
        if(Cont[m] == Cont[m + 1]):
            Vit()
'''


# CondicVit()
