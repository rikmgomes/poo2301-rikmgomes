
import os
import csv

class Usuario:
    def __init__(self, nome=None, sobrenome=None, dataDeNascimento=None, cpf=None, usuario=None, senha=None):
        self._nome = nome
        self._sobrenome = sobrenome
        self._dataDeNascimento = dataDeNascimento
        self._cpf = cpf
        self._usuario = usuario
        self._senha = senha
        self._assinaturas = []
    
    def getCpf(self):
        return self._cpf
    
    def getNome(self):
        return self._nome
    
    def getAssinaturas(self):
        print(self._assinaturas)
    
    def setLogin(self,usuario):
        self._usuario = usuario
    
    def setSenha(self,senha):
        self._senha = senha
    
    def adicionar_assinatura(self, assinatura):
        self._assinaturas.append(assinatura)
    
    def cancelar_assinatura(self):
        if len(self._assinaturas) == 0:
            print('\n----------------Cancelar Assinatura----------------')
            print("\nNão existem assinaturas para este usuário!\n")
            print("\nPressione qualquer tecla para continuar")
        else:
            print('\n----------------Cancelar Assinatura----------------')
            print("\nLista de Assinaturas do Usuario:")
            for i in range(len(self._assinaturas)):
                print(f"{i} | {self._assinaturas[i].serializar()}")
            print()
            num = int(input("Digite o número da assinatura que deseja cancelar: "))
            self._assinaturas[num].setStatus(1)
            print()
            print("Assinatura cancelada!")
            input("\nPressione qualquer tecla para continuar")

    def exibir_dados(self):
        print("----------Dados do Usuário----------")
        print(f"Nome = {self._nome}")
        print(f"Sobrenome = {self._sobrenome}")
        print(f"Data de Nascimento = {self._dataDeNascimento}")
        print(f"CPF = {self._cpf}")
        print(f"Login = {self._usuario}")
        print(f"Senha = {self._senha}")
    
    def serializar(self):
        return (f"{self._nome}",f"{self._sobrenome}",f"{self._dataDeNascimento}",f"{self._cpf}",f"{self._usuario}",f"{self._senha}")

    def desserializar(self, dados):
        linha = dados
        self._nome = linha[0]
        self._sobrenome = linha[1]
        self._dataDeNascimento = linha[2]
        self._cpf = linha[3]
        self._usuario = linha[4]
        self._senha = linha[5]

class Assinatura:
    def __init__(self, tipo=None, preco=None, id=None, status=None):
        self._tipo = tipo
        self._preco = preco
        self._id = id
        self._status = status
    
    def getId(self):
        return self._id

    def setStatus(self,modo):
        if modo == 0:
            self._status = "Ativa"
        elif modo == 1:
            self._status = "Inativa"

    def exibir_dados(self):
        print("----------Dados da Assinatura----------")
        print(f"Tipo = {self._tipo}")
        print(f"Preço = {self._preco}")
        print(f"ID = {self._id}")
        print(f"Status = {self._status}")
    
    def serializar(self):
        return (f"{self._id}",f"{self._tipo}",f"{self._preco}",f"{self._status}")

    def desserializar(self, dados):
        linha = dados
        self._id = linha[0]
        self._tipo = linha[1]
        self._preco = linha[2]
        self._status = linha[3]

class Aplicacao:
    def __init__(self):
        self.__tela = 0
        self.__terminou = False
        self.__usuarios = []
        self.__assinaturas = []
        self.ler_usuarios_csv()
        self.ler_assinaturas_csv()
        for i in self.__assinaturas:
            for j in self.__usuarios:
                if i.getId() == j.getCpf():
                    j.adicionar_assinatura(i)

    def executar(self):
        opcao = -1
        while not self.__terminou:
            if self.__tela == 0:
                self.telaInicial()
    
    def menuInicial(self):
        os.system('cls') 
        print('----------------TELA INICIAL----------------\n')
        print('1 - Adicionar Usuário')
        print('2 - Adicionar Assinatura')
        print('3 - Cancelar Assinatura')
        print('4 - Salvar Alterações')
        print('0 - Sair do Aplicativo\n')
        item = input('Escolha uma opcao: ')
        return item

    def ler_assinaturas_csv(self):
        arqCSV = open('Assinaturas.csv', encoding="utf-8-sig")
        leitor = csv.reader(arqCSV,delimiter=',')
        for linha in leitor:
            assinatura = Assinatura()
            assinatura.desserializar(linha)
            self.__assinaturas.append(assinatura)
        arqCSV.close()

    def ler_usuarios_csv(self):
        arqCSV = open('Usuarios.csv')
        leitor = csv.reader(arqCSV,delimiter=',')
        for linha in leitor:
            usuario = Usuario()
            usuario.desserializar(linha)
            self.__usuarios.append(usuario)
        arqCSV.close()
        
    def msgErro(self, codigo):
        if codigo == 1:
            print('Opcao invalida!')
            input('Pressione qualquer tecla para continuar')

    def telaInicial(self):
        opcao = self.menuInicial()
        if opcao == '0':
            self.__terminou = True
        elif opcao == '1':
            self.adicionarUsuario()
        elif opcao == '2':
            self.adicionarAssinatura()
        elif opcao == '3':
            self.cancelarAssinatura()
        elif opcao == '4':
            self.salvarAlteracoes()
        else:
            self.msgErro(1)
        
    def adicionarUsuario(self):
        print('\n----------------Cadastrando usuario----------------')
        nome = input("\nDigite o nome do novo usuário: ")
        sobrenome = input("Digite o sobrenome do novo usuário: ")
        data = input("Digite a data de nascimento do novo usuário (dd/mm/aaaa): ")
        cpf = input("Digite o CPF do novo usuário (xxx.xxx.xxx-xx): ")
        usuario = input("Digite o login do novo usuário: ")
        senha = input("Digite a senha do novo usuário: ")
        novo_usuario = Usuario(nome,sobrenome,data,cpf,usuario,senha)
        self.__usuarios.append(novo_usuario)
        print("\nUsuário criado!")
        input("\nPressione qualquer tecla para continuar")
    
    def adicionarAssinatura(self):
        print('\n----------------Adicionar Assinatura----------------')
        tipo = input("\nDigite o tipo da nova assinatura: ")
        preco = input("Digite o preço da nova assinatura: ")
        id = input("Digite o ID da nova assinatura: ")
        status = input("Digite o Status da nova assinatura: ")
        nova_assinatura = Assinatura(tipo,preco,id,status)
        self.__assinaturas.append(nova_assinatura)
        print("\nAssinatura criada!")
        i = 0
        for i in self.__usuarios:
            if nova_assinatura.getId() == i.getCpf():
                i.adicionar_assinatura(nova_assinatura)
                print("\nAssinatura adicionada ao respectivo usuário!")
        input("\nPressione qualquer tecla para continuar")

    def cancelarAssinatura(self):
        print('\n----------------Cancelar Assinatura----------------')
        print("\nLista de Usuarios do Sistema:")
        for i in range(len(self.__usuarios)):
            print(f"{i} | {self.__usuarios[i].getNome()}")
        print()
        num = int(input("Digite o número do usuario cujas assinaturas deseja alterar: "))
        self.__usuarios[num].cancelar_assinatura()

    def salvarAlteracoes(self):
        print('\n----------------Salvando Alterações----------------')
        print()
        f = open("Usuarios.csv", 'w', newline='')
        writer = csv.writer(f)
        for usuario in self.__usuarios:
            writer.writerow(usuario.serializar())
            print("Usuário salvo!")
        f.close()

        f = open("Assinaturas.csv", 'w', newline='')
        writer = csv.writer(f)
        for assinatura in self.__assinaturas:
            writer.writerow(assinatura.serializar())
            print("Assinatura salva!")
        f.close()

        input("\nPressione qualquer tecla para continuar")

aplicacao = Aplicacao()
aplicacao.executar()