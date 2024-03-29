''''/*******************************************************************************
Autor: Carlos Arthur Batista Nunes
Componente Curricular: MI de Algoritimos
Concluido em: 30/04/2023
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
******************************************************************************************/'''

import random
import time


navios = [4, 3, 3, 2, 2, 2] #tamanho dos navios

#construção das matrizes
matriz_cpu = [['~' for i in range(10)] for j in range(10)]
matriz_player = [['~' for i in range(10)] for j in range(10)]
matriz_agua_cpu = [['~' for i in range(10)] for j in range(10)]
matriz_agua_player = [['~' for j in range(10)] for j in range(10)]

def print_matriz(matriz): #função usada para mostrar a matriz de forma organizada
    linha = 0
    print('  0 1 2 3 4 5 6 7 8 9')
    for linhas in matriz:
        print(linha, ' '.join(linhas))
        linha += 1

def verificar_se_navio_cabe(orientacao, linha, coluna, tamanho_navil): #verifica se o navio cabe na matriz antes de coloca-lo
    if orientacao == 'H':
        if linha + tamanho_navil > 10:
            return False
        else:
            return True
    else:
        if coluna + tamanho_navil > 10:
            return False
        else:
            return True

def nao_sobrepor_navio(orientacao, linha, coluna, tamanho_navio, matriz): #essa funçao não permite que se coloque um navio onde já existe
    if orientacao == 'H':
        for i in range(coluna, coluna + tamanho_navio):
            if matriz[linha][i] == 'n':
                return False
    else:
        for i in range(linha, linha + tamanho_navio):
            if matriz[i][coluna] == 'n':
                return False
    return True

def colocar_navio_CPU(matriz): #adciona os navios na matriz do computador
        for tamanho_navio in navios:
            while True:
                if matriz == matriz_cpu:
                    orientacao, linha, coluna = random.choice(['H', 'V']), random.randint(0, 9), random.randint(0, 9) #escolha randomica dos valores
                    try:
                        #verificações:
                        if verificar_se_navio_cabe(orientacao, linha, coluna, tamanho_navio):
                            if nao_sobrepor_navio(orientacao, linha, coluna, tamanho_navio, matriz) == True:
                                #posicionamento dos navios:
                                if orientacao == 'H':
                                    for i in range(coluna, coluna + tamanho_navio):
                                        matriz[linha][i] = 'n'
                                else:
                                    for i in range(linha, linha + tamanho_navio):
                                        matriz[i][coluna] = 'n'
                                break
                    except IndexError:
                        continue

def colocar_navil_player(matriz, decisao): #adciona os navios do jogador
        for tamanho_navio in navios:
            if matriz == matriz_player:
                colocar_navio = True
                while True:
                    print_matriz(matriz_player)
                    try:
                        orientacao, linha, coluna = inputs_usuario(tamanho_navio, colocar_navio, decisao) #chamada da função dos inputs do usuário
                        #verificações:
                        if verificar_se_navio_cabe(orientacao, linha, coluna, tamanho_navio):
                            if nao_sobrepor_navio(orientacao, linha, coluna, tamanho_navio, matriz_player) == True:
                                #poicionamento:
                                if orientacao == 'H':
                                    for i in range(coluna, coluna + tamanho_navio):
                                        matriz[linha][i] = 'n'
                                else:
                                    for i in range(linha, linha + tamanho_navio):
                                        matriz[i][coluna] = 'n'
                                break
                            else:
                                print('Seu navio está sobrepondo a posição de outro. Escolha outra posição')
                    except IndexError:
                        print('Você ultrapassou o tabuleiro. digite novamente.')
                        continue

def inputs_usuario(tamanho_navil, colocar_navio, decisao): #fução para pedir os valores de orientação, posição da linha e coluna
    if colocar_navio == True:
        #bloco para pedir a orientação:
        while True:
            #caso o usuário tenha colocado no modo normal:
            if decisao == 'N':
                orientacao = input(f'qual orientação deseja posicionar o navio de tamanho {tamanho_navil} (H = HORIZONTAL/V = VERTICAL)? ').upper()
                if orientacao == 'H' or orientacao == 'V':
                    break
                else:
                    print('Digite uma valor valido para a orientação')
            #no modo altomático:
            if decisao == 'S':
                orientacao = random.choice(['H', 'V'])
                break
        #bloco para pedir a posição da linha:
        while True:
            try:
                # no modo altomático:
                if decisao == 'S':
                    linha = random.randint(0, 9)
                    break
                # caso o usuário tenha colocado no modo normal:
                else:
                    linha = int(input('Digite um valor para a linha entre 0 e 9: '))
                    if 0 <= linha <= 9:
                        break
                    else:
                        print('digite um valor valido para a linha')
            except:
                print('digite um valor valido para a linha')
                continue
        #bloco para pedir a posição da coluna:
        while True:
            try:
                # no modo altomático:
                if decisao == 'S':
                    coluna = random.randint(0, 9)
                    break
                # caso o usuário tenha colocado no modo normal:
                else:
                    coluna = int(input('Digite um valor para a coluna entre 0 e 9: '))
                    if 0 <= coluna <= 9:
                        break
                    else:
                        print('digite um valor valido para a linha')
            except:
                print('digite um valor valido para a linha')
                continue
        return orientacao, linha, coluna
    if colocar_navio == False:
        # bloco para pedir a posição da linha:
        while True:
            try:
                # no modo altomático:
                if decisao == 'S':
                    linha = random.randint(0, 9)
                    break
                # caso o usuário tenha colocado no modo normal:
                else:
                    linha = int(input('Digite um valor para a linha entre 0 e 9: '))
                    if 0 <= linha <= 9:
                        break
                    else:
                        print('digite um valor valido para a linha')
            except:
                print('digite um valor valido para a linha')
                continue
        # bloco para pedir a posição da coluna:
        while True:
            try:
                # no modo altomático:
                if decisao == 'S':
                    coluna = random.randint(0, 9)
                    break
                # caso o usuário tenha colocado no modo normal:
                else:
                    coluna = int(input('Digite um valor para a coluna entre 0 e 9: '))
                    if 0 <= coluna <= 9:
                        break
                    else:
                        print('digite um valor valido para a coluna')
            except:
                print('digite um valor valido para a coluna')
                continue
        return linha, coluna

def contador_de_pontos(matriz): #função para marcar a puntuação
    if matriz == matriz_agua_player:
        pontos_player = 0
        for i in matriz:
            for j in i:
                if j == 'X':
                    pontos_player += 1
        return pontos_player
    else:
        pontos_CPU = 0
        for i in matriz:
            for j in i:
                if j == 'X':
                    pontos_CPU += 1
        return pontos_CPU

def turno(matriz_turno): #função para fazer os turnos
    #bloco para o tuno do computador:
    if matriz_turno == matriz_agua_cpu:
        linha, coluna = random.randint(0, 9), random.randint(0, 9) # gerar valores randômicos para linha e coluna
        #bloco para evitar repetição:
        if matriz_turno[linha][coluna] == 'O':
            turno(matriz_turno)
        #bloco para evitar repetição:
        if matriz_turno[linha][coluna] == 'x':
            turno(matriz_turno)
        if matriz_player[linha][coluna] == 'n': # caso nessa posição seja um navio, careta-lo troca o símbolo para "X"
            matriz_turno[linha][coluna] = 'X'
            matriz_player[linha][coluna] = 'X'
            contador_de_pontos(matriz_agua_cpu) # chamada da função paraa calcular os pontos
            print('O computador acertou! Ele vai jogar novamente.')
            turno(matriz_turno) # acertando tem ouro tiro
        if matriz_player[linha][coluna] == '~':
            matriz_turno[linha][coluna] = 'O'
            matriz_player[linha][coluna] = 'O'
    #bloco para o turno do jogador:
    if matriz_turno == matriz_agua_player:
        colocar_navio = False
        linha, coluna = inputs_usuario(matriz_agua_player, colocar_navio, decisao) # chamada da fução para pedir a linha e a coluna para o usuário
        if matriz_turno[linha][coluna] == 'O':
            print('Você já atingio este ponto. Escolha outro.')
            turno(matriz_turno)
        #bloco para evitar repetição:
        elif matriz_turno[linha][coluna] == 'n':
            print('Você já atingio este ponto. Escolha outro.')
            turno(matriz_turno)
        #bloco caso ocorra um acerto:
        elif matriz_cpu[linha][coluna] == 'n':
            matriz_turno[linha][coluna] = 'X'
            if matriz_cpu[linha][coluna] == 'n':
                if contador_de_pontos(matriz_agua_player) == 16:
                    pass
                else:
                    print('Você acertou! Atire novamente.')
                    print_matriz(matriz_agua_player)
                    turno(matriz_turno)
        else:
            matriz_turno[linha][coluna] = 'O'



#programa principal:

#mensagem de boas vindas!
print('=-'*60)
print('''Olá, capitão! É uma honra tê-lo a bordo neste emocionante jogo de batalha naval.
Prepare-se para desafiar seus oponentes em uma batalha estratégica no mar, 
onde sua habilidade e inteligência serão treinadas ao máximo.''')
print('=-'*60)
print()
print('=-'*60)
print('''Queremos te apresentar primeiro as regras do jogo:
-> O objetivo do jogo é destruir todos os navios do adversário antes que ele destrua todos os seus navios.
-> Cada jogador terá uma tabuleiro para posicionar os seus navios e outro para atirar.
-> A cada acerto no tabuleiro do oponete você terá direito a um tiro extra.
-> Você terá que posicionar 6 navios, sendo um grande de tamanho 4x1 ou 1x4, dois médios de tamanho 3x1 ou 1x3
e três navios pequenos de tamanho 2x1 ou 1x2.''')
print('=-'*60)
print()
#modo de jogo:
print('=-'*60)
print('''Antes de começarmos gostaria que selecionasse o modo de jogo. sendo o automático (você ira somente
vizualisar o jogo) e o modo normal (onde você realmente joga)''')
print('=-'*60)
print()
while True:
    decisao = input('Você deseja iniciar no modo de jogo altomático?(S = Sim / N = Não. \n').upper()
    if decisao != 'S' and decisao != 'N':
        print('Digite um valor válido.')
        continue
    else:
        break
if decisao == 'S':
    print('Ok!')
    time.sleep(1)
else:
    print('Vamos começar, Capitão!')

#inicia o posicionamento dos navios
colocar_navio_CPU(matriz_cpu)
print('\nPosicione seu navios!\n')
colocar_navil_player(matriz_player, decisao)
print_matriz(matriz_player)

#começo dos turnos
while True:
    #turno do computador:
    print('\nVez do computador!\n')
    while True:
        turno(matriz_agua_cpu) # chamada da função para iniciar o turno do computador
        print(f'\nPontuação do computador: {contador_de_pontos(matriz_agua_cpu)}')
        #time.sleep(1)
        break
    if contador_de_pontos(matriz_agua_cpu) == 16: #condição para terminar o jogo
        print('Você perdeu!\n ')
        break
    #turno do player:
    print('\nSua vez!\n')
    while True:
        print('\nVisão do seu tabuleiro sendo atingido pela CPU.')
        print_matriz(matriz_player) # chamada da função para mostrar a matriz com os navios do jogador
       # time.sleep(1)
        print('\nEscolha a posição para atirar.')
        print_matriz(matriz_agua_player) # chamada da função para mostrar a matriz com água que o jogador está acertando
        turno(matriz_agua_player) # chamada da função para iniciar o turno do jogador
        print(f'\nSua pontuação é: {contador_de_pontos(matriz_agua_player)}\n')
        #time.sleep(1)
        break
    if contador_de_pontos(matriz_agua_player) == 16: #condição para terminar o jogo
        print_matriz(matriz_agua_player)
        print('Parabens! Você ganhou!\n')
        break
