import os # Biblioteca de sistema operacional do Python

def menuInicial():
    # Limpa a tela - Win/Linux/MacOS 
    os.system('cls') 
    print('----------------TELA INICIAL----------------')
    print('1 - Novo Album')
    print('2 - Acessar Album')
    print('0 - Sair do Aplicativo\n')
    item = input('Escolha uma opcao: ')
    return item

def menuGerenciarAlbum():
    # Limpa a tela - Win/Linux/MacOS 
    os.system('cls') 
    print('----------------GERENCIAR ALBUM----------------')
    print('1 - Ver album')
    print('2 - Gerenciar a colecao')
    print('3 - Abrir Pacote de Figurinhas')
    print('0 - Voltar para a tela inicial\n')
    item = input('Escolha uma opcao: ')
    return item

def menuGerenciarColecao():
    # Limpa a tela - Win/Linux/MacOS 
    os.system('cls') 
    print('----------------GERENCIAR COLECAO----------------')
    print('1 - Colar figurinha')
    print('2 - Disponibilizar para troca')
    print('3 - Propor troca')
    print('4 - Revisar solicitacoes')
    print('0 - Voltar para a tela Gerenciar Album\n')
    item = input('Escolha uma opcao: ')
    return item