
import os
import random

baseDeDados = [ [0, 'Fa fe fi fo Funk',	'Anira', 'Funk', 2019, '3:05'],
                [1, 'Sofrência de programar', 'Ada & Turing',	'Sertanejo', 1998, '2:58' ],
                [2, 'Rock n Rolo', 'The Buns','Rock',	1984, '4:01' ],
                [3, 'Grifinoria Girls', 'Katy Potter', 'Pop',	2017, '2:25' ],
                [4, 'Outra musica', 'Anira', 'Funk', 2019, '3:05'], 
                [5, 'Cuzinho magro', 'Anira', 'Funk', 2020, '5:10'] ]

playlist = []

def EscolherOpcao():
    print('..:: Mini-Spotify Python ::..\n')
    print('1 - Visualizar Base de Dados')
    print('2 - Montar uma Playlist')
    print('3 - Visualizar a Playlist')
    print('4 - Embaralhar a Playlist')
    print('5 - Mostrar a Duração Total da Playlist')
    print('6 - Consultar Música')
    print('7 - Consultar Artista/Banda')
    print('0 - Sair\n')
    resposta = input('..:: Escolha uma Opção: ')
    os.system('cls' if os.name == 'nt' else 'clear')
    return resposta

def ExecutarAcao1():
    print('..:: Opção 1 - Visualizar Base de Dados ::..\n')
    print('Nº - ID - Nome da Música - Artista/Banda - Gênero - Ano - Duração')
    id = 1
    for i in baseDeDados:
        cu = id
        for j in i:
            print(id, j, sep=' - ', end = '')
            id = ''
        id = cu
        id+=1
        print()

def ExecutarAcao2(): 
    print('..:: Opção 2 - Montar uma Playlist ::..\n')
    if playlist == []:
        print('A playlist atual está vazia!')
    else:
        print('A playlist já possui algumas músicas!')
    terminarExecucao2 = False
    while not terminarExecucao2:
        addMusica = int(input('\nInforme o ID da música a ser adicionada: '))
        jaNaPlaylist = False
        for i in range (len(playlist)):
            if playlist[i] == addMusica:
                print('Essa música já está na playlist!')
                jaNaPlaylist = True
                break
        if not jaNaPlaylist and addMusica < len(baseDeDados):
            playlist.append(addMusica)
            print('Música adicionada com sucesso!')
            continuar = ''
            while continuar != 'S' and continuar != 'N':
                continuar = input('\nDeseja adicionar mais músicas (S/N)? ')
                if continuar == 'N':
                    terminarExecucao2 = True
        else:
            print('Música Inválida.')
            continuar = ''
            while continuar != 'S' and continuar != 'N':
                continuar = input('\nDeseja tentar novamente (S/N)? ')
                if continuar == 'N':
                    terminarExecucao2 = True

def ExecutarAcao3(): 
    print('..:: Opção 3 - Visualizar a Playlist ::..\n')
    if playlist == []:
        print('A playlist atual está vazia!')
    else:
        for i in playlist:
            print (baseDeDados[i])

def ExecutarAcao4(): 
    print('..:: Opção 4 - Embaralhar a Playlist ::..\n')
    if playlist == []:
        print('A playlist atual está vazia!')
    else:
        random.shuffle(playlist)
        for i in playlist:
            print(baseDeDados[i])

def ExecutarAcao5(): 
    print('..:: Opção 5 - Mostrar a Duração Total da Playlist ::..\n')
    if playlist == []:
        print('A playlist atual está vazia!')
    else:    
        totalTime = 0
        for i in range(len(playlist)):
            timestr = baseDeDados[playlist[i]][5]
            print(f'Música Nº{i+1} | Tempo = {baseDeDados[playlist[i]][5]}')
            mins = []
            mins =  timestr.split(':')
            m1 = float(mins[0])
            m2 = float(mins[1])
            m2 = m2/60.0
            totalTime += m1 + m2
        print(f'\nTempo total = {totalTime:.2f} minutos.')

def ExecutarAcao6(): 
    print('..:: Opção 6 - Consultar Música ::..\n')
    terminarExecucao6 = False
    while not terminarExecucao6:
        nomeMusica = input('Informe o nome da música: ')
        tem = 0
        for i in range(len(baseDeDados)):
            if nomeMusica == baseDeDados[i][1]:
                print('Essa música CONSTA no Banco de Dados!')
                print(f'{nomeMusica}, ID = {baseDeDados[i][0]}')
                tem+=1
        if tem == 0:
            print('Essa música NÃO CONSTA no Banco de Dados!')
        continuar = ''
        while continuar != 'S' and continuar != 'N':
            continuar = input('\nDeseja consultar outra música (S/N)? ')
            if continuar == 'N':
                terminarExecucao6 = True

def ExecutarAcao7(): 
    print('..:: Opção 7 - Consultar Artista/Banda ::..\n')
    terminarExecucao7 = False
    mesmaBanda = []
    while not terminarExecucao7:
        nomeMusica = input('Informe o nome do(a) Artista/Banda: ')
        tem = 0
        for i in range(len(baseDeDados)):
            if nomeMusica == baseDeDados[i][2]:
                mesmaBanda.append(baseDeDados[i][0])
                tem+=1
        if tem == 0:
            print('Esse(a) artista/banda NÃO CONSTA no Banco de Dados!')
        else:
            print('Esse(a) artista/banda CONSTA no Banco de Dados!')
            print(f'Lista IDs das músicas do(a) Artista/Banda solicitado = {mesmaBanda}')
        continuar = ''
        while continuar != 'S' and continuar != 'N':
            continuar = input('\nDeseja consultar outro(a) Artista/Banda (S/N)? ')
            if continuar == 'N':
                terminarExecucao7 = True
            else:
                mesmaBanda = []

def Executar():
    terminarExecucao = False
    while not terminarExecucao:
        os.system('cls' if os.name == 'nt' else 'clear')
        acaoUsuario = EscolherOpcao()
        if (acaoUsuario == '1'):
            ExecutarAcao1()
        elif (acaoUsuario == '2'):
            ExecutarAcao2()
        elif (acaoUsuario == '3'):
            ExecutarAcao3()
        elif (acaoUsuario == '4'):
            ExecutarAcao4()
        elif (acaoUsuario == '5'):
            ExecutarAcao5()
        elif (acaoUsuario == '6'):
            ExecutarAcao6()
        elif (acaoUsuario == '7'):
            ExecutarAcao7()
        elif (acaoUsuario == '0'):
            terminarExecucao = True
        else:
            print('\n..:: Escolha invalida! Tente de novo. ::..\n')
        if acaoUsuario != '0':
            input('\nPressione ENTER para retornar ao menu.')

def Finalizar():
    print('\n..:: O programa foi encerrado! ::..\n')

if __name__ == '__main__':
    Executar()
    Finalizar()