import csv
import os

catalogoGeral = [] #lista com todas as midias
catalogoEpisodios = [] #lista com todos os episodios
catalogo = [] #guarda o objeto catalogo

class Aplicacao:
    def __init__(self):
        self.__tela = 0
        self.__terminou = False
        self._listaUsuarios = []
        self._listaPerfis = []
        self._usuarioAtual = 'x'
        self._perfilAtual = 'x'
        self._idConsulta = 'x'
        self._midiaAtual = 'x'
        self._temporadaConsulta = 'x'
        self.carregarCatalogoGeral()
        self.carregarUsuarios()
        self.carregarPerfis()
        self.carregarEpisodios()
    
    def carregarCatalogoGeral(self):
        #ID,Tipo,Título,Gênero,Ano,Classificação,Temporadas,Diretor,Produtor,Tema,Estúdio
        #0   1    2       3    4        5          6        7        8        9    10
        arqCatalogo = open('catalogoGeral.csv', encoding="utf-8-sig")
        leitor = csv.reader(arqCatalogo,delimiter=',')
        self.catalogo = Catalogo()
        for linha in leitor:
            if linha[1] == "Serie":
                serie = Serie()
                serie.desserializar(linha)
                self.catalogo.adicionarMidia(serie, 1)
                catalogoGeral.append(serie)
            elif linha[1] == "Filme":
                filme = Filme()
                filme.desserializar(linha)
                self.catalogo.adicionarMidia(filme, 2)
                catalogoGeral.append(filme)
            elif linha[1] == "Documentario":
                doc = Documentario()
                doc.desserializar(linha)
                self.catalogo.adicionarMidia(doc, 3)
                catalogoGeral.append(doc)
            elif linha[1] == "Animacao":
                animacao = Animacao()
                animacao.desserializar(linha)
                self.catalogo.adicionarMidia(animacao, 4)
                catalogoGeral.append(animacao)
            elif linha[1] == "Programa de TV":
                programa = ProgramaDeTv()
                programa.desserializar(linha)
                self.catalogo.adicionarMidia(programa, 5)
                catalogoGeral.append(programa)
        arqCatalogo.close()
        catalogo.append(self.catalogo)

    def carregarEpisodios(self):
        arqEpisodios = open('catalogoEpisodios.csv', encoding="utf-8-sig")
        leitor = csv.reader(arqEpisodios,delimiter=',')
        
        #Nro,Serie,Titulo,Temporada
        # 0   1      2        3
        for linha in leitor:
            novoEpisodio = Episodio()
            novoEpisodio.desserializar(linha)
            catalogoEpisodios.append(novoEpisodio)
        arqEpisodios.close()

        for i in catalogoEpisodios:
            for j in catalogoGeral:
                if i.getTitulo() == j.getTitulo():
                    j.adicionarEpisodio(i)
    
    def carregarUsuarios(self):
        arqUsuarios = open('usuarios.csv', encoding="utf-8-sig")
        leitor = csv.reader(arqUsuarios,delimiter=',')
        for linha in leitor:
            novoUsuario = Usuario()
            novoUsuario.desserializar(linha)
            self._listaUsuarios.append(novoUsuario)
        arqUsuarios.close()

    def carregarPerfis(self):
        #usuario,nome,idade,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,ua1,ua2,ua3,ua4,ua5,ua6,ua7,ua8,ua9,ua10
        #   0     1     2   (3  4  5  6 7  8  9  10 11 12) (13  14 15  16  17  18   19  20 21   22)
        arqPerfis = open('perfis.csv', encoding="utf-8-sig")
        leitor = csv.reader(arqPerfis,delimiter=',')
        for linha in leitor:
            novoPerfil = Perfil()
            novoPerfil.desserializar(linha)
            for j in self._listaUsuarios:
                if j.getNome() == linha[0]:
                    j.adicionarPerfil(novoPerfil)
            self._listaPerfis.append(novoPerfil)
        arqPerfis.close()

    def executar(self):
        opcao = -1
        while not self.__terminou:
            if self.__tela == 0:
                self.telaInicial()   
            elif self.__tela == 1:
                self.telaGerenciarConta()
            elif self.__tela == 2:
                self.telaGerenciarPerfil()
            elif self.__tela == 3:
                self.telaMidia()
            elif self.__tela == 4:
                self.telaEpisodios()
    
    def finalizar(self):
        print('\n----------------SALVANDO E SAINDO...----------------')
        print()
        f = open("usuariosteste.csv", 'w', newline='')
        writer = csv.writer(f)
        for usuario in self._listaUsuarios:
            writer.writerow(usuario.serializar())
            print("Usuário salvo!")
        f.close()

        f = open("perfisteste.csv", 'w', newline='')
        writer = csv.writer(f)
        for perfil in self._listaPerfis:
            writer.writerow(perfil.serializar())
            print("Perfil salvo!")
        f.close()

        input("\nPressione qualquer tecla para continuar")
        
    def msgErro(self, codigo):
        if codigo == 1:
            print('Opcao invalida!')
            input('Pressione qualquer tecla para continuar')

    def menuInicial(self):
        os.system('cls') 
        print('----------------UNIFLIX // TELA INICIAL----------------')
        print('1 - Acessar')
        print('2 - Criar Conta')
        print('0 - Sair\n')
        item = input('Escolha uma opcao: ')
        return item

    def menuGerenciarConta(self):
        os.system('cls') 
        print('----------------GERENCIAR USUARIO----------------')
        print('1 - Alterar Assinatura')
        print('2 - Acessar Perfil')
        print('3 - Editar Perfil')
        print('4 - Adicionar Perfil')
        print('5 - Remover Perfil')
        print('0 - Voltar para a tela inicial\n')
        item = input('Escolha uma opcao: ')
        return item

    def menuGerenciarPerfil(self):
        os.system('cls') 
        print('----------------GERENCIAR PERFIL----------------')
        print('1 - Buscar por Nome')
        print('2 - Últimos Assistidos')
        print('3 - Favoritos')
        print('4 - Filmes')
        print('5 - Series')
        print('6 - Documentarios')
        print('7 - Animacoes')
        print('8 - Programas de TV')
        print('0 - Voltar para o menu anterior\n')
        item = input('Escolha uma opcao: ')
        return item

    def menuMidia(self):
        os.system('cls')
        if self._midiaAtual.getTipo() == "Serie" or self._midiaAtual.getTipo() == "Programa de TV":
            print('----------------MIDIA----------------\n')
            self._midiaAtual.exibirInformacoes()
            print('1 - Listar Episodios')
            print('2 - Favoritar')
            print('3 - Desfavoritar')
            print('0 - Voltar para o menu anterior\n')
            item = input('Escolha uma opcao: ')
        else:   
            print('----------------MIDIA----------------')
            self._midiaAtual.exibirInformacoes()
            print('1 - Assistir')
            print('2 - Favoritar')
            print('3 - Desfavoritar')
            print('0 - Voltar para o menu anterior\n')
            item = input('Escolha uma opcao: ')
        return item
    
    def menuEpisodios(self):
        os.system('cls')
        print('----------------MIDIA----------------\n')
        if self._midiaAtual.getTipo() == "Serie":
            self._midiaAtual.listarEpisodios(self._temporadaConsulta)
        else:
            self._midiaAtual.listarEpisodios()
        print('1 - Assistir')
        print('0 - Voltar para o menu anterior\n')
        item = input('Escolha uma opcao: ')
        return item

    def telaInicial(self): #MENU0
        opcao = self.menuInicial()
        if opcao == '0':
            self.__terminou = True
        elif opcao == '1':
            self.acessarConta()
        elif opcao == '2':
            self.cadastrarUsuario()
        else:
            self.msgErro(1)
    
    def cadastrarUsuario(self):
        print('\n----------------NOVA CONTA----------------')
        login = input("\nDigite o login desejado: ")
        senha = input("Digite a senha desejada: ")
        plano = input("Digite o tipo de plano desejado (Simples ou Premium): ")
        print("\nUsuário sendo criado...")
        novoUsuario = Usuario(login, senha, plano)
        print("Nova conta criada com sucesso!!")
        self._listaUsuarios.append(novoUsuario)
        input("\nPressione qualquer tecla para continuar...")

    def acessarConta(self):
        print('\n----------------ACESSAR CONTA EXISTENTE----------------')
        podeSeguir = False
        e = 0
        while not podeSeguir:
            if e>0:
                print("Login inválido! Tente novamente!")
            usuario = input("\nDigite seu login: ")
            senha = input("Digite sua senha: ")
            for i in self._listaUsuarios:
                podeSeguir = i.verificar(usuario,senha)
                if podeSeguir == True:
                    self._usuarioAtual = i
                    break
                else:
                    e+=1
        print("\nUsuário Verificado!")
        print("Recuperando a conta do usuario...")
        self.__tela = 1
        input('\nPressione qualquer tecla para continuar...')

    def telaGerenciarConta(self): #MENU1
        opcao = self.menuGerenciarConta()
        if opcao == '0':
            self.__tela = 0
        elif opcao == '1':
            decisao = input("Digite para qual plano deseja migrar (Simples ou Premium): ")
            self._usuarioAtual.alterarPlano(decisao)
        elif opcao == '2':
            self.acessarPerfil()
        elif opcao == '3':
            self.editarPerfil()
        elif opcao == '4':
            self.adicionarPerfil()
        elif opcao == '5':
            self.removerPerfil()
        else:
            self.msgErro(1)
    
    def acessarPerfil(self):
        print('\n----------------ACESSAR PERFIL EXISTENTE----------------')
        lista = self._usuarioAtual.getListaPerfis()
        j = 0
        for i in lista:
            print(f"Perfil {j} - {i.getNome()}")
            j+=1
        perfil = int(input("\nDigite o número do perfil que deseja acessar: "))
        self._perfilAtual = lista[perfil]
        print("\nAcessando perfil...")
        print("Perfil acessado com sucesso!")
        self.__tela = 2
        input('\nPressione qualquer tecla para continuar...')

    def editarPerfil(self):
        print('\n----------------EDITAR PERFIL----------------')
        if self._perfilAtual == 'x':
            print("\nNenhum perfil selecionado.")
            print("Acesse um perfil primeiro para depois poder editá-lo.")
            input('\nPressione qualquer tecla para continuar...')
        else:
            print(f"Nome Atual = {self._perfilAtual.getNome()}")
            print(f"Idade Atual = {self._perfilAtual.getIdade()}")
            nome = input("\nDigite o novo nome: ")
            idade = input("Digite a nova idade: ")
            self._perfilAtual.setNome(nome)
            self._perfilAtual.setIdade(idade)
            print("Atualizando perfil...")
            print("Perfil atual atualizado!")
            input('\nPressione qualquer tecla para continuar...')

    def adicionarPerfil(self):
        print('\n----------------ADICIONAR PERFIL----------------')
        nome = input("\nDigite o nome do novo perfil: ")
        idade = input("Digite a idade do novo perfil: ")
        perfil = Perfil(nome,idade)
        self._usuarioAtual.adicionarPerfil(perfil)
        input('\nPressione qualquer tecla para continuar...')

    def removerPerfil(self):
        print('\n----------------REMOVER PERFIL----------------')
        lista = self._usuarioAtual.getListaPerfis()
        j = 0
        for i in lista:
            print(f"Perfil {j} - {i.getNome()}")
            j+=1
        perfil = input("\nDigite o nome do perfil que deseja remover: ")
        self._usuarioAtual.removerPerfil(perfil)
        input('\nPressione qualquer tecla para continuar...')

    def telaGerenciarPerfil(self): #MENU2
        opcao = self.menuGerenciarPerfil()
        if opcao == '0':
            self.__tela = 1
        elif opcao == '1':
            self.buscarPorNome()
        elif opcao == '2':
            self.ultimosAssistidos()
        elif opcao == '3':
            self.favoritos()
        elif opcao == '4':
            self.listarMidias(4)
        elif opcao == '5':
            self.listarMidias(5)
        elif opcao == '6':
            self.listarMidias(6)
        elif opcao == '7':
            self.listarMidias(7)
        elif opcao == '8':
            self.listarMidias(8)
        else:
            self.msgErro(1)
    
    def buscarPorNome(self):
        print('\n----------------BUSCAR POR NOME----------------')
        titulo = input("\nDigite o nome da midia que deseja buscar: ")
        existe = self._perfilAtual.buscarPorTitulo(titulo)
        if existe == None:
            print("Essa mídia não existe no catálogo!")
        else:
            existe.exibirInformacoes()
        input("\nPressione qualquer tecla para continuar...")

    def ultimosAssistidos(self):
        print('\n----------------ULTIMOS ASSISTIDOS----------------')
        print("\nNUMERO - TITULO (ID)")
        lista = self._perfilAtual.getUltimosAssistidos()
        j = 0
        for i in lista:
            print(f"{j} - {i.getTitulo()} ({i.getId()})")
            j+=1
        input("\nPressione qualquer tecla para continuar...")

    def favoritos(self):
        print('\n----------------FAVORITOS----------------')
        print("\nNUMERO - TITULO (ID)")
        lista = self._perfilAtual.getFavoritos()
        j = 0
        for i in lista:
            print(f"{j} - {i.getTitulo()} ({i.getId()})")
            j+=1
        input("\nPressione qualquer tecla para continuar...")

    def listarMidias(self, numero):
        if numero == 4:
            print('\n----------------LISTA DE FILMES----------------')
            midias = self._perfilAtual.listarMidiasApropriadas(2)
        elif numero == 5:
            print('\n----------------LISTA DE SERIES----------------')
            midias = self._perfilAtual.listarMidiasApropriadas(1)
        elif numero == 6:
            print('\n----------------LISTA DE DOCUMENTARIOS----------------')
            midias = self._perfilAtual.listarMidiasApropriadas(3)
        elif numero == 7:
            print('\n----------------LISTA DE ANIMACOES----------------')
            midias = self._perfilAtual.listarMidiasApropriadas(4)
        elif numero == 8:
            print('\n----------------LISTA DE PROGRAMAS DE TV----------------')
            midias = self._perfilAtual.listarMidiasApropriadas(5)

        print("\nID - TITULO DA MIDIA")
        for i in midias:
            print(f"{i.getId()} - {i.getTitulo()}")
        resposta = input("Deseja ver mais informacoes sobre uma midia (S/N)?")
        if resposta == "S":
            self._idConsulta = input("Digite o ID da midia: ")
            for i in catalogoGeral:
                if i.getId() == self._idConsulta:
                    self._midiaAtual = i
            self.__tela = 3
        else:
            input("\nPressione qualquer tecla para continuar...")

    def telaMidia(self): #MENU3
        opcao = self.menuMidia()
        if opcao == '0':
            self.__tela = 2
        elif opcao == '1':
            if self._midiaAtual.getTipo() == "Serie" or self._midiaAtual.getTipo() == "Programa de TV":
                if self._midiaAtual.getTipo() == "Serie":
                    print('\n---------------->>> LISTAR EPISODIOS----------------')
                    t = input("Digite o número da temporada desejada: ")
                self.__tela = 4
            else:
                print('\n----------------ASSISTINDO TRANSMISSÃO----------------')
                self._perfilAtual.assistirMidia(self._midiaAtual)
                input("\nPressione qualquer tecla para continuar...")
        elif opcao == '2':
            print('\n----------------FAVORITAR MIDIA----------------')
            self._perfilAtual.favoritar(self._midiaAtual, True)
            input("\nPressione qualquer tecla para continuar...")
        elif opcao == '3':
            print('\n----------------DESFAVORITAR OBRA----------------')
            self._perfilAtual.favoritar(self._midiaAtual, False)
            input("\nPressione qualquer tecla para continuar...")
        else:
            self.msgErro(1)
    
    def telaEpisodios(self): #MENU4
        opcao = self.menuEpisodios()
        if opcao == '0':
            self.__tela = 3
        elif opcao == '1':
            print('\n----------------ASSISTINDO TRANSMISSÃO----------------')
            self._perfilAtual.assistirMidia(self._midiaAtual)
            input("\nPressione qualquer tecla para continuar...")
        else:
            self.msgErro(1)

class Usuario:
    def __init__(self, nome=None, senha=None, tipo=None):
        self._nome = nome
        self._senha = senha
        self._tipo = tipo
        self._listaPerfis = []

        #tipo simples = até 3 perfis, propagandas, 29.90/mês
        #tipo premium = até 5 perfils, sem propagandas, 49.90/mês
    
    def getNome(self):
        return self._nome

    def getListaPerfis(self):
        return self._listaPerfis
    
    def exibirInformacoes(self):
        print(f'Nome = {self._nome}')
        print(f'Senha = {self._senha}')
        print(f'Tipo de Assinatura = {self._tipo}')
    
    def adicionarPerfil(self,perfil):
        if self._tipo == "Simples":
            if len(self._listaPerfis) < 4:
                self._listaPerfis.append(perfil)
                print("Criando perfil...")
                print("Perfil criado e adicionado a lista de perfis!")
            else:
                print("O número máximo de perfis dessa conta (simples) já foi atingido.")
                print("Remova um perfil existente para poder criar outro.")
        elif self._tipo == "Premium":
            if len(self._listaPerfis) < 6:
                self._listaPerfis.append(perfil)
                print("Criando perfil...")
                print("Perfil criado e adicionado a lista de perfis!")
            else:
                print("O número máximo de perfis dessa conta (premium) já foi atingido.")
                print("Remova um perfil existente para poder criar outro.")

    def removerPerfil(self,perfil):
        contador = 0
        for i in self._listaPerfis:
            if i.getNome() == perfil:
                self._listaPerfis.remove(i)
                contador+=1
        if contador > 0:
            print("Removendo perfil...")
            print("Perfil removido!")
        else:
            print("Nenhum perfil encontrado com este nome.")
            print("Tente novamente mais tarde...")

    def alterarSenha(self,novaSenha):
        self._senha = novaSenha
    
    def alterarPlano(self,novoTipo):
        self._tipo = novoTipo
    
    def verificar(self, login, senha):
        if self._nome == login:
            if self._senha == senha:
                return True
            else:
                return False
        else:
            return False
    
    def serializar(self):
        return(f"{self._nome}",f"{self._senha}",f"{self._tipo}")

    def desserializar(self, dados):
        linha = dados
        self._nome = linha[0]
        self._senha = linha[1]
        self._tipo = linha[2]

class Perfil:
    def __init__(self, usuario=None, nome=None, idade=None):
        self._usuario = usuario
        self._nome = nome
        self._idade = idade
        self._listaFavoritos = [] #classe mídia
        self._listaUltimosAssistidos = [] #classe mídia
    
    def getNome(self):
        return self._nome
    
    def getIdade(self):
        return self._idade
    
    def setNome(self,nome):
        self._nome = nome

    def setIdade(self, idade):
        self._idade = idade

    def getFavoritos(self):
        return self._listaFavoritos

    def getUltimosAssistidos(self):
        return self._listaUltimosAssistidos
    
    def adicionarFavorito(self, midia):
        if len(self._listaFavoritos) < 10:
            self._listaFavoritos.append(midia)
        else:
            self._listaFavoritos.pop(0)
            self._listaFavoritos.append(midia)
    
    def removerFavorito(self, midia):
        self._listaFavoritos.remove(midia)

    def adicionarUltimoAssistido(self, midia):
        if len(self._listaUltimosAssistidos) < 10:
            self._listaUltimosAssistidos.append(midia)
        else:
            self._listaUltimosAssistidos.pop(0)
            self._listaUltimosAssistidos.append(midia)
    
    def listarMidiasApropriadas(self,tipo):
        listaInicial = catalogo[0].obterLista(tipo)
        listaFinal = []
        for i in listaInicial:
            if i.getClassificacao() <= self._idade:
                listaFinal.append(i)
        return listaFinal

    def assistirMidia(self, midia):
        print("A mídia está sendo exibida...")
        for i in self._listaUltimosAssistidos:
            if i.getId() == midia.getId():
                self._listaUltimosAssistidos.remove(i)
        self.adicionarUltimoAssistido(midia)

    def favoritar(self, midia, bool):
        contador = 0
        if bool == True:
            for i in self._listaFavoritos:
                if i.getId() == midia.getId():
                    contador+=1
            if contador == 0:
                self.adicionarFavorito(midia)
                print("Obra adicionada aos favoritos do perfil atual!")
            else:
                print("Obra já está nos favoritos do perfil atual!")
        else:
            contador = 0
            for i in self._listaFavoritos:
                if i.getId() == midia.getId():
                    contador+=1
            if contador != 0:
                self.removerFavorito(midia)
                print("Obra removida dos favoritos do perfil atual!")

    def buscarPorTitulo(self, titulo):
        midia = 'midia'
        for i in catalogoGeral: #guarda midia
            if i.getTitulo() == titulo:
                midia = i
        if midia == 'midia':
            return None
        else:
            return midia
    
    def serializar(self):
        #### faltou apenas mudar as listas pra serializar
        ### favoritos e ultimo assistidos estão com objetos da classe midia
        ### é necessário transformar de volta nos indices pra salvar corretamente
        ### e, se não tiver nada no slot, preencher com ''
        return (f"{self._usuario}",f"{self._nome}",f"{self._idade}",f"{self._listaFavoritos[0]}",f"{self._listaFavoritos[1]}",f"{self._listaFavoritos[2]}",f"{self._listaFavoritos[3]}",f"{self._listaFavoritos[4]}",f"{self._listaFavoritos[5]}",f"{self._listaFavoritos[6]}",f"{self._listaFavoritos[7]}",f"{self._listaFavoritos[8]}",f"{self._listaFavoritos[9]}",f"{self._listaUltimosAssistidos[0]}",f"{self._listaUltimosAssistidos[1]}",f"{self._listaUltimosAssistidos[2]}",f"{self._listaUltimosAssistidos[3]}",f"{self._listaUltimosAssistidos[4]}",f"{self._listaUltimosAssistidos[5]}",f"{self._listaUltimosAssistidos[6]}",f"{self._listaUltimosAssistidos[7]}",f"{self._listaUltimosAssistidos[8]}",f"{self._listaUltimosAssistidos[9]}")
    
    def desserializar(self,dados):
        #usuario,nome,idade,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,ua1,ua2,ua3,ua4,ua5,ua6,ua7,ua8,ua9,ua10
        #   0     1     2   (3  4  5  6 7  8  9  10 11 12) (13  14 15  16  17  18   19  20 21   22)
        linha = dados
        self._usuario = linha[0]
        self._nome = linha[1]
        self._idade = linha[2]
        for j in range(3,13):
            if linha[j] != '':
                indice = int(linha[j])
                self._listaFavoritos.append(catalogoGeral[indice])
        for j in range(13,23):
            if linha[j] != '':
                indice = int(linha[j])
                self._listaUltimosAssistidos.append(catalogoGeral[indice])

class Midia:
    def __init__(self, id=None, tipo=None, titulo=None, genero=None, ano=None, classificacao=None):
        self._id = id
        self._tipo = tipo
        self._titulo = titulo
        self._genero = genero
        self._ano = ano
        self._classificacao = classificacao #livre,10,14,18 (???)
    
    def exibirInformacoes(self):
        print(f'ID = {self._id}')
        print(f'Tipo = {self._tipo}')
        print(f'Título = {self._titulo}')
        print(f'Gênero = {self._genero}')
        print(f'Ano = {self._ano}')
        print(f'Classificação = {self._classificacao}')
    
    def getClassificacao(self):
        return self._classificacao

    def getId(self):
        return self._id

    def getTitulo(self):
        return self._titulo
    
    def getTipo(self):
        return self._tipo
    
    def serrializar(self):
        pass

    #ID,Tipo,Título,Gênero,Ano,Classificação,Temporadas,Diretor,Produtor,Tema,Estúdio,Episodios
    #0   1    2       3    4        5          6        7        8        9    10         11

    def desserializar(self, dados):
        self._id = dados[0]
        self._tipo = dados[1]
        self._titulo = dados[2]
        self._genero = dados[3]
        self._ano = dados[4]
        self._classificacao = dados[5]

class Episodio:
    def __init__(self, numero=None, fonte=None, titulo=None, temporada=None):
        self._numero = numero
        self._fonte = fonte
        self._titulo = titulo
        self._temporada = temporada
    
    def getTemporada(self):
        return self._temporada

    def getTitulo(self):
        return self._titulo
    
    #Nro,Serie,Titulo,Temporada
    # 0   1      2        3
    def desserializar(self, dados):
        linha = dados
        self._numero = linha[0]
        self._fonte = linha[1]
        self._titulo = linha[2]
        self._temporada = linha[3]

class Serie(Midia):
    def __init__(self, id=None, tipo=None, titulo=None, genero=None, ano=None, classificacao=None, temporadas=None):
        super().__init__(id, tipo, titulo, genero, ano, classificacao)
        self._temporadas = temporadas
        self._listaEpisodiosPorTemporada = [] #classe episodio
    
    def getTitulo(self):
        return self._titulo

    def adicionarEpisodio(self,episodio):
        self._listaEpisodiosPorTemporada.append(episodio)
    
    def exibirInformações(self):
        super().exibirInformacoes()
        print(f'Nº Temporadas = {self._temporadas}')
    
    def listarEpisodios(self, numeroTemporada):
        print(f"Listando episódios da temporada {numeroTemporada}\n")
        for i in self._listaEpisodiosPorTemporada:
            if i.getTemporada() == numeroTemporada:
                print(i.getTitulo())
    
    def desserializar(self, dados):
        super().desserializar(dados)
        self._temporadas = dados[6]

class Filme(Midia):
    def __init__(self, id=None, tipo=None, titulo=None, genero=None, ano=None, classificacao=None, diretor=None, produtor=None):
        super().__init__(id, tipo, titulo, genero, ano, classificacao)
        self._diretor = diretor
        self._produtor = produtor
    
    def getTitulo(self):
        return self._titulo

    def exibirInformacoes(self):
        super().exibirInformacoes()
        print(f'Diretor/a/e = {self._diretor}')
        print(f'Produtor/a/e = {self._produtor}')
    
    def desserializar(self, dados):
        super().desserializar(dados)
        self._diretor = dados[7]
        self._produtor = dados[8]

class Documentario(Midia):
    def __init__(self, id=None, tipo=None, titulo=None, genero=None, ano=None, classificacao=None, tema=None):
        super().__init__(id, tipo, titulo, genero, ano, classificacao)
        self._tema = tema
    
    def getTitulo(self):
        return self._titulo

    def exibirInformacoes(self):
        super().exibirInformacoes()
        print(f'Tema = {self._tema}')
    
    def desserializar(self, dados):
        super().desserializar(dados)
        self._tema = dados[9]

class Animacao(Midia):
    def __init__(self, id=None, tipo=None, titulo=None, genero=None, ano=None, classificacao=None, estudio=None):
        super().__init__(id, tipo, titulo, genero, ano, classificacao)
        self._estudio = estudio
    
    def getTitulo(self):
        return self._titulo

    def exibirInformacoes(self):
        super().exibirInformacoes()
        print(f'Estúdio = {self._estudio}')
    
    def desserializar(self, dados):
        super().desserializar(dados)
        self._estudio = dados[10]

class ProgramaDeTv(Midia):
    def __init__(self, id=None, tipo=None, titulo=None, genero=None, ano=None, classificacao=None, episodios=None):
        super().__init__(id, tipo, titulo, genero, ano, classificacao)
        self._episodios = episodios
        self._listaEpisodios = []
    
    def getTitulo(self):
        return self._titulo

    def adicionarEpisodio(self,episodio):
        self._listaEpisodios.append(episodio)
    
    def exibirInformacoes(self):
        super().exibirInformacoes()
        print(f'Nº Episódios = {self._episodios}')
    
    def listarEpisodios(self):
        for i in self._listaEpisodios:
            print(i.getTitulo())
    
    def desserializar(self, dados):
        super().desserializar(dados)
        self._episodios = dados[11]

class Catalogo:
    def __init__(self):
        self._listaSeries = []
        self._listaFilmes = []
        self._listaDocumentarios = []
        self._listaAnimacoes = []
        self._listaProgramasTv = []
    
    def adicionarMidia(self, midia, tipo):
        if tipo == 1:
            self._listaSeries.append(midia)
        elif tipo == 2:
            self._listaFilmes.append(midia)
        elif tipo == 3:
            self._listaDocumentarios.append(midia)
        elif tipo == 4:
            self._listaAnimacoes.append(midia)
        elif tipo == 5:
            self._listaProgramasTv.append(midia)

    def obterLista(self, tipo):
        if tipo == 1:
            return self._listaSeries
        elif tipo == 2:
            return self._listaFilmes
        elif tipo == 3:
            return self._listaDocumentarios
        elif tipo == 4:
            return self._listaAnimacoes
        elif tipo == 5:
            return self._listaProgramasTv

aplicacao = Aplicacao()
aplicacao.executar()
aplicacao.finalizar()