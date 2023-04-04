
import os
import random

# 3)

class CadastroCliente:
    def __init__(self):
        self.nome = 1
        self.sobrenome = 1
        self.dataDeNascimento = 1
        self.email = 1
        self.CPF = 1
        self.__senha = 1
    
    def cadastrarCliente(self):
        self.nome = input("\nDigite seu nome: ")
        self.sobrenome = input("Digite seu sobrenome: ")
        self.dataDeNascimento = input("Digite sua data de nascimento (XX/XX/XXXX): ")
        self.email = input("Digite seu email (login): ")
        self.CPF = input("Digite seu cpf (XXX.XXX.XXX-XX): ")
        self.__senha = input("Digite sua senha: ")

    def consultarDados(self, liberado):
        if liberado < 3:
            loginCorreto = False
            while not loginCorreto:
                print("\nPara consultar seus dados, faça seu login!")
                log = input("\nDigite seu login (email): ")
                sen = input("Digite sua senha: ")
                if sen != self.__senha:
                    liberado+=1
                    if liberado == 1:
                        print("\nSenha incorreta, tente novamente! (1/3)")
                    elif liberado == 2:
                        print("\nSenha incorreta, tente novamente! (2/3)")
                    else:
                        print("\nSenha incorreta! Tente novamente mais tarde... (3/3)")
                        loginCorreto = True
                        return liberado
                elif log == self.email:
                    print(f"\nNome = {self.nome}")
                    print(f"Sobrenome = {self.sobrenome}")
                    print(f"Data de Nascimento = {self.dataDeNascimento}")
                    print(f"CPF = {self.CPF}")
                    loginCorreto = True
                    return liberado
                else:
                    print("\nLogin incorreto! Tente novamente!")
        else:
            print("\nCadastro Bloqueado! Tente novamente mais tarde...")
            return liberado

if __name__ == '__main__':
    # Pequeno Programa do Item 3.
    terminarExecucao = False
    login = False
    senha = False
    liberado = 0
    while not terminarExecucao:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("..:: Pequeno Programa - Item 2 ::..\n")
        print('1 - Realizar Cadastro')
        print('2 - Consultar Dados')
        print('0 - Sair\n')
        acaoUsuario = input('..:: Escolha uma Opção: ')
        if (acaoUsuario == '1'):
            if not login:
                usuario = CadastroCliente()
                usuario.cadastrarCliente()
                login = True
            else:
                print("\nUsuário já cadastrado!")
        elif (acaoUsuario == '2'):
            if not login:
                print("\nÉ necessário se cadastrar primeiro para Consultar os Dados!")
            else:
                liberado = usuario.consultarDados(liberado)
        elif (acaoUsuario == '0'):
            terminarExecucao = True
        else:
            print('\n..:: Escolha invalida! Tente de novo. ::..\n')
        if acaoUsuario != '0':
            input('\nPressione ENTER para retornar ao menu.')