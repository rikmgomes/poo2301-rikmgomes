
class Mago:
    def __init__(self, nome, idade, escola, feitiçoPrincipal, poderDeMagia):
        self.nome = nome 
        self.idade = idade   
        self.escola = escola

        # 1 - Adicione mais 2 atributos à classe Mago.
        self.feitiçoPrincipal = feitiçoPrincipal
        self.poderDeMagia = poderDeMagia
    
    def andar(self):
        print('Estou andando')
    
    def falar(self):
        print('Ola amigue! Meu nome é ',self.nome)
    
    def invocarMagia(self):
        print('Invocando magia!')
    
    # 1 - Adicione mais 2 métodos à classe Mago.
    def qualFeitiçoPrincipal(self):
        print(f'O feitiço principal de {self.nome} é: {self.feitiçoPrincipal}')
    
    def qualPoderDeMagia(self):
        print(f'Competidor: {self.nome} | Poder de Magia: {self.poderDeMagia}')
    
# 2 - Instancie 3 objetos da classe mago...
cc = Mago('Curioso', 29, 'Sei lá', 'Raio de Gelo', 20)
pp = Mago('Perebinha', 12, 'Autodidata', 'Prestidigitação', 1)
gg = Mago('Gigante Furioso', 500, 'Vento Ventosa', 'Mata Dragão', 50)

# 2 - ... e invoque seus métodos.
cc.qualFeitiçoPrincipal()
cc.qualPoderDeMagia()
print()
pp.qualFeitiçoPrincipal()
pp.qualPoderDeMagia()
print()

# 3 - Crie uma classe Data, com os seguintes atributos: dia, mês e ano. Além do construtor padrão, a
#     classe deverá ter um construtor personalizado que recebe dia, mês e ano por parâmetro. Essa classe
#     deve ter também dois métodos: imprimirData, que não recebe parâmetro, e
#     imprimirDataPorExtenso, que recebe o nome de uma cidade por parâmetro. Ambos os métodos
#     não retornam dados.

class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes 
        self.ano = ano

    def imprimirData(self):
        print(f'{self.dia}/{self.mes}/{self.ano}')
        
    def imprimirDataPorExtenso(self, cidade):
        if self.mes == 1:
            mesExtenso = 'janeiro'
        elif self.mes == 2:
            mesExtenso = 'fevereiro'
        elif self.mes == 3:
            mesExtenso = 'março'
        elif self.mes == 4:
            mesExtenso = 'abril'
        elif self.mes == 5:
            mesExtenso = 'maio'
        elif self.mes == 6:
            mesExtenso = 'junho'
        elif self.mes == 7:
            mesExtenso = 'julho'
        elif self.mes == 8:
            mesExtenso = 'agosto'
        elif self.mes == 9:
            mesExtenso = 'setembro'
        elif self.mes == 10:
            mesExtenso = 'outubro'
        elif self.mes == 11:
            mesExtenso = 'novembro'
        elif self.mes == 12:
            mesExtenso = 'dezembro'
        print(f'{cidade}, dia {self.dia} de {mesExtenso} de {self.ano}.')

# Chamadas...
cb = Data(14, 3, 2023)
cidade = 'Carlos Barbosa'
cb.imprimirData()
cb.imprimirDataPorExtenso(cidade)
print()

# 4 - Adapte o exercício de revisão (mini-spotify), propondo uma classe Musica.
#
# Eu tinha pedido no dia se era só enviar isso e você tinha confirmado, mas talvez possa ter ocorrido
# uma falha na comunicação haushua. Não ficou muito claro (pra mim) na explicação do problema se eu precisaria
# copiar o exercício de revisão inteiro ou somente a parte adaptada abaixo.

class Musica:
    def __init__(self, id, nome, artista, genero, ano, duracao):

        # 4 - Quais seriam seus Atributos?
        self.id = id
        self.nome = nome
        self.artista = artista
        self.genero = genero
        self.ano = ano
        self.duracao = duracao

    # 4 - Quais seriam alguns dos seus possíveis Métodos?
    def consultarMusica(self):
        print(f'{self.id} | {self.nome} | {self.artista} | {self.ano} | {self.duracao}')
    
    def consultarGenero(self):
        print(f'O gênero da música {self.nome} é {self.genero}.')

# Chamadas...
mA = Musica(0, 'Fa fe fi fo Funk',	'Anira', 'Funk', 2019, '3:05')
mA.consultarMusica()
mA.consultarGenero()
print()

# 4 - Como poderíamos representar uma playlist?
# 
# Não sei com exatidão qual o impacto de processamento da substituição de Lista por Classe, mas não vejo uma forma
# diferente de organizar/representar a playlist. Todas as músicas precisarão estar dentro de variáveis (pelo menos
# do que vimos até agora) ou sendo recebidas como resposta do usuário.
#
# Talvez uma classe 'Playlist' de elementos de outra classe? Não sei se isso é possível (tipo lista de listas)...