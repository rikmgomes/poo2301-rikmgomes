
import os
import random

# 1)
# 
# a. Faça um programa que simule um "dado virtual".
# b. O dado deve ser modelado como uma classe, possuindo apenas o número de faces e o método Rolar, que retorna o valor sorteado.
# c. O número de faces deve ser definido na criação do objeto (construtor com parâmetro).
# d. Deve ser instanciado um dado com 6, 8 e 12 faces no main().
# e. Cada dado deve ser jogado 3 vezes e o resultado de cada jogada deve ser impresso na tela.
# f. Não deve ser usado print dentro da classe.

class Dado:
    def __init__(self, faces):
        self.faces = faces

    def Rolar(self):
        if self.faces == 6:
            return random.randint(1,6)
        elif self.faces == 8:
            return random.randint(1,8)
        elif self.faces == 12:
            return random.randint(1,12)

# 2)
# 
# a. Crie uma classe chamada Calculadora, com os métodos somar, subtrair, multiplicar e dividir dois números.
# b. Cada um destes métodos recebe por parâmetro dois números reais e retorna o resultado da operação com os dois números.
# c. Se houver divisão por zero, imprimir um aviso na execução do método e retornar -1.

class Calculadora:
    def __init__(self):
        pass

    # Testei algumas chamadas dos métodos (tipo "a = Calculadora.SomarDoisNumeros(5,9)") e sempre dava erro
    # até que eu tirei o "self" de dentro dos métodos. Tá certo isso? Lembro de você falando que era obrigatório,
    # mas se eu deixo o "self" ele fica pedindo 3 elementos na passagem de parâmetro.
    #
    # Talvez a intenção do exercício seja criar um objeto já com 2 números reais? Não ficou claro no enunciado pra mim.

    def SomarDoisNumeros(n1, n2):
        soma = n1 + n2
        return soma

    def SubtrairDoisNumeros(n1, n2):
        subtracao = n1 - n2
        return subtracao

    def MultiplicarDoisNumeros(n1, n2):
        multiplicacao = n1 * n2
        return multiplicacao

    def DividirDoisNumeros(n1, n2):
        if n2 == 0:
            print("Não é possível dividir por 0!")
            return (-1)
        else:
            divisao = n1 / n2
            return divisao

# 3)
#
# a. Crie uma classe CadastroCliente com os atributos nome, sobrenome, data de nascimento, email, CPF e senha.
# b. Faça um pequeno programa que permita o cliente se cadastrar e depois consultar seus dados.
# c. Para consultar seus dados, é necessário que ele faça o login com seu email e senha.
# d. Se o cliente errar a senha 3x, o cadastro é bloqueado e ele não pode mais acessar.

class CadastroCliente:
    def __init__(self):
        self.nome = 1
        self.sobrenome = 1
        self.dataDeNascimento = 1
        self.email = 1
        self.CPF = 1
        self.senha = 1
    
    def cadastrarCliente(self):
        self.nome = input("\nDigite seu nome: ")
        self.sobrenome = input("Digite seu sobrenome: ")
        self.dataDeNascimento = input("Digite sua data de nascimento (XX/XX/XXXX): ")
        self.email = input("Digite seu email (login): ")
        self.CPF = input("Digite seu cpf (XXX.XXX.XX-XX): ")
        self.senha = input("Digite sua senha: ")

    def consultarDados(self, liberado):
        if liberado == 0:
            loginCorreto = False
            erro = 0
            while not loginCorreto:
                print("\nPara consultar seus dados, faça seu login!")
                log = input("\nDigite seu login (email): ")
                sen = input("Digite sua senha: ")
                if sen != self.senha:
                    erro+=1
                    if erro == 1:
                        print("\nSenha incorreta, tente novamente! (1/3)")
                    elif erro == 2:
                        print("\nSenha incorreta, tente novamente! (2/3)")
                    else:
                        print("\nSenha incorreta! Tente novamente mais tarde... (3/3)")
                        loginCorreto = True
                        return 1
                elif log == self.email:
                    print(f"\nNome = {self.nome}")
                    print(f"Sobrenome = {self.sobrenome}")
                    print(f"Data de Nascimento = {self.dataDeNascimento}")
                    print(f"CPF = {self.CPF}")
                    loginCorreto = True
                    return 0
                else:
                    print("\nLogin incorreto! Tente novamente!")
        else:
            print("\nCadastro Bloqueado! Tente novamente mais tarde...")

# 4)
#
# Corrida maluca. Vamos simular uma corrida com 5 competidores. A classe para representar cada competidor é dada abaixo.
# A corrida ocorre como se fosse em um tabuleiro de 20 posicoes, como o mostrado abaixo.
#
# a. Para isso, você deve inicializar cada competidor com seu nome (a posição de todos começa em zero).
# b. A corrida acontece enquanto nenhum dos competidores tiver vencido - chegado ao fim (pos > 20).
# c. A cada ciclo, deve-se chamar o método atualizar de cada competidor.
# 
# Neste método, a posição do competidor é atualizada da seguinte maneira:
# 
# • Sorteia-se um número de 1 a 6 (simulando um dado)
# • A posição do competidor avança o número sorteado de casas no tabuleiro, respeitando as seguintes regras:
#   o Se cair em uma casa com número múltiplo de 5, deve-se recuar 1 casa
#   o Se cair nas casas de número 7 ou 17, avança 2 casas
#   o Se cair na casa de número 13, volta ao início (pos = 0)
#   o Se passar de 20, não tem problema (deve-se sinalizar que a corrida terminou e guardar o índice do competidor vencedor)
# 
# d. Após chamar o método atualizar de um competidor, deve-se em seguida verificar se ele venceu a corrida.
# - Se positivo, a corrida termina imediatamente (termina a rodada).
# 
# e. Ao fim de cada rodada, deve-se imprimir o nome e posição atual de cada jogador.
# f. Ao final da corrida, deve-se imprimir o nome do vencedor.

class Competidor:
    def __init__(self, nome):
        self.nome = nome
        self.pos = 0
    
    def atualizar(self):
        n = random.randint(1,6)
        # print(n)
        self.pos = self.pos + n
        if self.pos == 5 or self.pos == 10 or self.pos == 15 or self.pos == 20:
            self.pos = self.pos - 1
        elif self.pos == 7 or self.pos == 17:
            self.pos = self.pos + 2
        elif self.pos == 13:
            self.pos = 0
        else:
            pass

    def getPos(self):
        return self.pos
    
    def getNome(self):
        return self.nome

if __name__ == '__main__':

    # Instânciações do Item 1.
    seisfaces = Dado(6)
    oitofaces = Dado(8)
    dozefaces = Dado(12)

    # Impressões do Item 1.
    terminarRolagem = False
    while not terminarRolagem:
        print("..:: Resultados Dados - Item 1 ::..\n")
        print(f'Roll 1  (d6): {seisfaces.Rolar()} - Roll 2  (d6): {seisfaces.Rolar()} - Roll 3  (d6): {seisfaces.Rolar()}')
        print(f'Roll 1  (d8): {oitofaces.Rolar()} - Roll 2  (d8): {oitofaces.Rolar()} - Roll 3  (d8): {oitofaces.Rolar()}')
        print(f'Roll 1 (d12): {dozefaces.Rolar()} - Roll 2 (d12): {dozefaces.Rolar()} - Roll 3 (d12): {dozefaces.Rolar()}\n')
        acaoUsuario = input('>>>> Pressione ENTER para ver o próximo Item. ')
        if acaoUsuario != '1000000000000000':
            terminarRolagem = True

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

    # Instânciações do Item 4.
    c1 = Competidor('Azul')
    c2 = Competidor('Vermelho')
    c3 = Competidor('Verde')
    c4 = Competidor('Amarelo')
    c5 = Competidor('Rosa')

    # Corrida Maluca do Item 4.
    terminarCorrida = False
    rodada = 0
    vencedor = 0
    while not terminarCorrida:
        print("..:: Corrida Maluca - Item 4 ::..\n")
        if rodada == 0:
            print("=========")
            print(f"Rodada {rodada}")
            print("=========\n")
            print(f'Competidor = {c1.getNome()} (posição = {c1.getPos()})')
            print(f'Competidor = {c2.getNome()} (posição = {c2.getPos()})')
            print(f'Competidor = {c3.getNome()} (posição = {c3.getPos()})')
            print(f'Competidor = {c4.getNome()} (posição = {c4.getPos()})')
            print(f'Competidor = {c5.getNome()} (posição = {c5.getPos()})\n')
            rodada+=1
        else:
            print("=========")
            print(f"Rodada {rodada}")
            print("=========\n")
            c1.atualizar()
            if c1.getPos() > 20:
                terminarCorrida = True
                vencedor = c1
            else:
                c2.atualizar()
                if c2.getPos() > 20:
                    terminarCorrida = True
                    vencedor = c2
                else:
                    c3.atualizar()
                    if c3.getPos() > 20:
                        terminarCorrida = True
                        vencedor = c3
                    else:
                        c4.atualizar()
                        if c4.getPos() > 20:
                            terminarCorrida = True
                            vencedor = c4
                        else:
                            c5.atualizar()
                            if c5.getPos() > 20:
                                terminarCorrida = True
                                vencedor = c5
            print(f'Competidor = {c1.getNome()} (posição = {c1.getPos()})')
            print(f'Competidor = {c2.getNome()} (posição = {c2.getPos()})')
            print(f'Competidor = {c3.getNome()} (posição = {c3.getPos()})')
            print(f'Competidor = {c4.getNome()} (posição = {c4.getPos()})')
            print(f'Competidor = {c5.getNome()} (posição = {c5.getPos()})\n')
            if not terminarCorrida:
                rodada+=1
    print("========================================")
    print(f"Vencedor = {vencedor.getNome()} (posição final = {vencedor.getPos()})")
    print("========================================\n")
