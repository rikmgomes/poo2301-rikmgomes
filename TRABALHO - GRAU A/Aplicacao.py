from Figurinha import Figurinha
from Usuario import Usuario
from Album import Album
from Pagina import Pagina
from Troca import Troca
from Menus import *
import csv
import random

class Aplicacao:
    def __init__(self): #pronto
        self.__tela = 0
        self.__terminou = False
        self.carregarFigurinhas()
        self.carregarUsuarios()
        self.carregarTrocas()

    def executar(self): #pronto
        opcao = -1
        while not self.__terminou:
            if self.__tela == 0: #tela entrada
                self.telaInicial()   
            elif self.__tela == 1: #tela gerenciar album
                self.telaGerenciarAlbum()
            elif self.__tela == 2: #tela gerenciar colecao
                self.telaGerenciarColecao()

    def finalizar(self):
        print('Finalizando a aplicacao!')
        # executar os salvamentos nos arquivos
        pass

    def carregarFigurinhas(self): #pronto
        arqFigurinhas = open('figurinhas.csv')
        leitor = csv.reader(arqFigurinhas,delimiter=';')
        listaFig = list(leitor)
        arqFigurinhas.close()
        self.__listaFigurinhas = []
        for i in range(len(listaFig)):
            figurinha = Figurinha(int(listaFig[i][0]),listaFig[i][1],listaFig[i][2],int(listaFig[i][3]))                        
            self.__listaFigurinhas.append(figurinha)    

    def carregarUsuarios(self):#pronto
        arqUsuarios = open('usuarios.csv')
        leitor = csv.reader(arqUsuarios,delimiter=';')
        listaUsu = list(leitor)
        arqUsuarios.close()
        self.__listaUsuarios = []
        for i in range(0, len(listaUsu), 4):
            usuario = Usuario(listaUsu[i][0],listaUsu[i][1])
            album = Album()
            pagina = Pagina()
            pagina2 = Pagina()
            pagina3 = Pagina()
            pagina4 = Pagina()
            usuario.setAlbum(album)
            album.adicionarPagina(pagina)
            album.adicionarPagina(pagina2)
            album.adicionarPagina(pagina3)
            album.adicionarPagina(pagina4)
            j = 2
            for j in range(18): #2-17
                if j>=2 and j<6:
                    p = pagina
                elif j>=6 and j<10:
                    p = pagina2
                elif j>=10 and j<14:
                    p = pagina3
                elif j>=14 and j<18:
                    p = pagina4
                
                if listaUsu[i+2][j] == '0':
                    p.substituirFigurinha("X", j-2)
                elif listaUsu[i+2][j] == '1':
                    album.adicionarFigurinha(self.__listaFigurinhas[j-2].getNumero(), int(listaUsu[i+1][j]), "=")
                    p.substituirFigurinha("COLAR", j-2)
                elif listaUsu[i+2][j] == '2':
                    album.adicionarFigurinha(self.__listaFigurinhas[j-2].getNumero(), int(listaUsu[i+1][j])-1, "=")
                    p.substituirFigurinha(self.__listaFigurinhas[j-2].getNome(), j-2)

                if listaUsu[i+3][j] == '0':
                    album.adicionarTrocaNaoTroca(self.__listaFigurinhas[j-2].getNumero(), "0")

            self.__listaUsuarios.append(usuario)
    
    def carregarTrocas(self): #pronto
        arqTrocas = open('trocas.csv')
        leitor = csv.reader(arqTrocas,delimiter=';')
        listaTroc = list(leitor)
        arqTrocas.close()
        self.__listaTrocas = []
        for i in range(len(listaTroc)):
                        #de quem             #pra quem          #fig que quer       #fiq que troca por      #status (0-1-2)
            troca = Troca(listaTroc[i][0], listaTroc[i][1], int(listaTroc[i][2]), int(listaTroc[i][3]), int(listaTroc[i][4]))
            for j in range(len(self.__listaUsuarios)):
                if self.__listaUsuarios[j].getNomeUsuario() == listaTroc[i][1]:
                    self.__listaUsuarios[j].getAlbum().adicionarRequisicaoTroca(troca)
            self.__listaTrocas.append(troca)
        
    def msgErro(self, codigo): #pronto
        if codigo == 1:
            print('Opcao invalida!')
            input('Pressione qualquer tecla para continuar')

    def verAlbum(self): #quase pronto (falta implementar passagem de páginas)
        print('\n----------------Ver Album----------------')
        s = self.__usuarioAtual.getAlbum()
        listaPaginas = s.getPaginas()
        j = 0
        for i in listaPaginas:
            i.imprimirPagina(j)
            j+=4
        print()
        input('Pressione qualquer tecla para continuar')

    def abrirPacoteFigurinhas(self): #pronto
        listaSorteio = [random.randint(0,15),random.randint(0,15),random.randint(0,15)]
        b = self.__usuarioAtual.getAlbum()
        c = b.getPaginas()
        p = 0

        for i in listaSorteio:
            if i>=0 and i<4:
                p = c[0]
            elif i>=4 and i<8:
                p = c[1]
            elif i>=8 and i<12:
                p = c[2]
            elif i>=12 and i<16:
                p = c[3]
            p.substituirFigurinha("COLAR", i)
            b.adicionarFigurinha(i, 1, "+")

        print("\nFigurinhas Sorteadas:")
        print(f"1x {self.__listaFigurinhas[listaSorteio[0]].getNome()}")
        print(f"1x {self.__listaFigurinhas[listaSorteio[1]].getNome()}")
        print(f"1x {self.__listaFigurinhas[listaSorteio[2]].getNome()}")
        input('\nPressione qualquer tecla para continuar')

    def colarFigurinha(self): #pronto
        print('\n----------------Colar Figurinha----------------')
        s = self.__usuarioAtual.getAlbum()
        f = s.getFigurinhas()
        print("#", ' ', "Disponíveis")
        g = 0
        while g<16:
              print(f"{g:<2}", ' ', f"{f[g+16]:>2}")
              g+=1
            
        numero = int(input("\nDigite o número da figurinha que deseja colar (0-15): "))
        c = s.getPaginas()
        p = 0
        if numero>=0 and numero<4:
            p = c[0]
        elif numero>=4 and numero<8:
            p = c[1]
        elif numero>=8 and numero<12:
            p = c[2]
        elif numero>=12 and numero<16:
            p = c[3]
        f = p.getFigurinhas()
        if numero == 0 or numero == 4 or numero == 8 or numero == 12:
            if f[0] == "X":
                print("Figurinha inexistente!")
            elif f[0] == "COLAR":
                p.substituirFigurinha(self.__listaFigurinhas[numero].getNome(), numero)
                s.adicionarFigurinha(numero, 1, "-")
                print("\nOperação concluída!")
            else:
                print("Figurinha já colada!")
        elif numero == 1 or numero == 5 or numero == 9 or numero == 13:
            if f[1] == "X":
                print("Figurinha inexistente!")
            elif f[1] == "COLAR":
                p.substituirFigurinha(self.__listaFigurinhas[numero].getNome(), numero)
                s.adicionarFigurinha(numero, 1, "-")
                print("\nOperação concluída!")
            else:
                print("Figurinha já colada!")
        elif numero == 2 or numero == 6 or numero == 10 or numero == 14:
            if f[2] == "X":
                print("Figurinha inexistente!")
            elif f[2] == "COLAR":
                p.substituirFigurinha(self.__listaFigurinhas[numero].getNome(), numero)
                s.adicionarFigurinha(numero, 1, "-")
                print("\nOperação concluída!")
            else:
                print("Figurinha já colada!")
        else:
            if f[3] == "X":
                print("Figurinha inexistente!")
            elif f[3] == "COLAR":
                p.substituirFigurinha(self.__listaFigurinhas[numero].getNome(), numero)
                s.adicionarFigurinha(numero, 1, "-")
                print("\nOperação concluída!")
            else:
                print("Figurinha já colada!")
        input('\nPressione qualquer tecla para continuar')

    def disponibilizarParaTroca(self): #pronto
        print('\n----------------Disponibilizar para Troca----------------')
        s = self.__usuarioAtual.getAlbum()
        f = s.getTrocaNaoTroca()
        e = s.getFigurinhas()
        print("#", ' ', "Disponíveis", ' ', "Trocar?")
        g = 0
        while g<16:
            r = 0
            if f[g+16] == 0:
                r = "Disponível para Troca"
            else:
                r = "Não trocável"
            print(f"{g:<2}", ' ',f"{e[g+16]:>2}", ' ', f"{r:>2}")
            g+=1
        
        numero = int(input("\nDigite o número da figurinha que deseja mudar para 'TROCAR' (0-15): "))
        if e[numero+16] == 0:
            print("Operação inválida! Não existem figurinhas sobrando!")
        elif e[numero+16] >= 1:
            s.adicionarTrocaNaoTroca(numero, "0")
            print("\nOperação concluída!")
        input('\nPressione qualquer tecla para continuar')

    def proporTroca(self): #pronto
        print('\n----------------Propor Troca----------------')
        print("\n-Usuarios-", ' ', f"{0:>2}", ' ', f"{1:>2}", ' ', f"{2:>2}", ' ', f"{3:>2}", ' ', f"{4:>2}", ' ', f"{5:>2}", ' ', f"{6:>2}", ' ', f"{7:>2}", ' ', f"{8:>2}", ' ', f"{9:>2}", ' ', f"{10:>2}", ' ', f"{11:>2}", ' ', f"{12:>2}", ' ', f"{13:>2}", ' ', f"{14:>2}", ' ', f"{15:>2}")
        for i in range(len(self.__listaUsuarios)):
            f = self.__listaUsuarios[i].getAlbum()
            s = f.getTrocaNaoTroca()
            j = 16
            for j in range(len(s)):
                if s[j] == 0:
                    s[j] = "T"
                elif s[j] == 1:
                    s[j] = "NT"
            print(f"{self.__listaUsuarios[i].getNomeUsuario():>10}", ' ', f"{s[16]:>2}", ' ', f"{s[17]:>2}", ' ', f"{s[18]:>2}", ' ', f"{s[19]:>2}", ' ', f"{s[20]:>2}", ' ', f"{s[21]:>2}", ' ', f"{s[22]:>2}", ' ', f"{s[23]:>2}", ' ', f"{s[24]:>2}", ' ', f"{s[25]:>2}", ' ', f"{s[26]:>2}", ' ', f"{s[27]:>2}", ' ', f"{s[28]:>2}", ' ', f"{s[29]:>2}", ' ', f"{s[30]:>2}", ' ', f"{s[31]:>2}")
            f = []
            s = []
        nomeAceitas = input("\nDigite o nome do usuário para propor troca: ")
        nomePropoes = self.__usuarioAtual.getNomeUsuario()
        figurinhaRequerida = int(input("Digite o número da figurinha que deseja: "))
        figurinhaDisponivel = int(input("Digite o número da figurinha que trocará: "))
        novaTroca = Troca(nomePropoes, nomeAceitas, figurinhaRequerida, figurinhaDisponivel, 0)
        for i in range(len(self.__listaUsuarios)):
            if self.__listaUsuarios[i].getNomeUsuario() == nomeAceitas:
                self.__listaUsuarios[i].getAlbum().adicionarRequisicaoTroca(novaTroca)
                print("Operação concluída!")
        input('\nPressione qualquer tecla para continuar')  

    def revisarSolicitacoes(self):
        pass

    def telaInicial(self): #pronto
        opcao = menuInicial()
        if opcao == '0':
            self.__terminou = True
        elif opcao == '1':
            self.cadastrarUsuario()
        elif opcao == '2':
            self.acessarAlbum()
        else:
            self.msgErro(1)
        
    def telaGerenciarAlbum(self): #pronto
        opcao = menuGerenciarAlbum()
        if opcao == '0':
            self.__tela = 0
        elif opcao == '1':
            self.verAlbum()
        elif opcao == '2':
            self.__tela = 2
        elif opcao == '3':
            self.abrirPacoteFigurinhas()
        else:
            self.msgErro(1)

    def telaGerenciarColecao(self): #pronto
        opcao = menuGerenciarColecao()
        if opcao == '0':
            self.__tela = 1
        elif opcao == '1':
            self.colarFigurinha()
        elif opcao == '2':
            self.disponibilizarParaTroca()
        elif opcao == '3':
            self.proporTroca()
        elif opcao == '4':
            self.revisarSolicitacoes()
        else:
            self.msgErro(1)

    def cadastrarUsuario(self): #pronto
        print('\n----------------Cadastrando usuario----------------')
        usuario = input("\nDigite o nome para o usuário: ")
        senha = input("Digite a senha para o usuário: ")
        novo_usuario = Usuario(usuario, senha)
        novo_album = Album()
        nova_pagina = Pagina()
        nova_pagina2 = Pagina()
        nova_pagina3 = Pagina()
        nova_pagina4 = Pagina()
        novo_album.adicionarPagina(nova_pagina)
        novo_album.adicionarPagina(nova_pagina2)
        novo_album.adicionarPagina(nova_pagina3)
        novo_album.adicionarPagina(nova_pagina4)
        novo_usuario.setAlbum(novo_album)
        self.__listaUsuarios.append(novo_usuario)
        print("\nUsuário cadastrado!")
        input('\nPressione qualquer tecla para continuar...')

    def acessarAlbum(self): #pronto
        print('\n----------------Login e Senha----------------')
        podeSeguir = False
        e = 0
        self.__usuarioAtual = 0
        while not podeSeguir:
            if e>0:
                print("Login inválido! Tente novamente!")
            usuario = input("\nDigite seu login: ")
            senha = input("Digite sua senha: ")
            for i in self.__listaUsuarios:
                podeSeguir = i.verificar(usuario,senha)
                if podeSeguir == True:
                    self.__usuarioAtual = i
                    break
                else:
                    e+=1

        print("\nUsuário Verificado!")
        print("Recuperando o album do usuario...")
        self.__tela = 1
        input('\nPressione qualquer tecla para continuar...')

        # DEBUG - ver se as informações puxadas estão sendo puxadas mesmo...
        # for i in range(len(self.__listaFigurinhas)):
        #     self.__listaFigurinhas[i].imprimir()
        # for i in range(len(self.__listaUsuarios)):
        #     self.__listaUsuarios[i].imprimir()
        #     b = self.__listaUsuarios[i].getAlbum()
        #     c = b.getPaginas()
        #     for i in c:
        #         i.imprimirPagina()