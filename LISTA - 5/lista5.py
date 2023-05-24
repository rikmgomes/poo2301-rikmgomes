
faunaBR = [
    #   0           1          2           3        4      5       6
    # [Animal	Amazônia Mata_Atlântica	Cerrado	Caatinga Pampa	Pantanal]
    ['Capivara',	True,	True,	True,	True,	True,	True],              #0
    ['Gralha azul',	False,	True,	False,	False,	True,	False],             #1
    ['Tamanduá-bandeira',	True,	True,	True,	False,	True,	False],     #2
    ['Onça pintada',	True,	True,	False,	True,	False,	True],          #3
    ['Tatu-bola',	False,	False,	False,	True,	False,	False]              #4
]

floraBR = [
    # [Planta	Amazônia Mata_Atlântica	Cerrado	Caatinga Pampa	Pantanal]
    ['Ipê amarelo',	True,	True,	True,	True,	True,	True],
    ['Araucária',	False,	True,	False,	False,	True,	False],
    ['Mandacaru',	False,	False,	True,	True,	False,	False],
    ['Vitória-régia',	True,	False,	False,	False,	False,	True],
    ['Jatobá',	True,	True,	True,	False,	False,	True]

]

class Bioma:
    def __init__(self, nome=None):
        self.__nome = nome
        self.__fauna = [] #lista de animais presentes
        self.__flora = [] #lista de vegetais presentes

    def getNome(self):
        return self.__nome
    
    def adicionarAnimal(self, animal):
        self.__fauna.append(animal) #add animais na lista do bioma...
    
    def adicionarVegetal(self, vegetal):
        self.__flora.append(vegetal) #add vegetais na lista do bioma...

    def exibirFauna(self):
        for i in self.__fauna: #percorre lista de animais e imprime o nome de cada um...
            print(f'- {i.getNome()}')

    def exibirFlora(self):
        for i in self.__flora: #percorre lista de vegetais e imprime o nome de cada um...
            print(f'- {i.getNome()}')

class SerVivo:
    def __init__(self, nome=None):
        self.__nome = nome
        self.__nomeCientifico = ''
        self.__filo = ''
        self.__classe = ''
        self.__familia = ''
        self.__genero = ''
        self.__especie = ''
        self.__estadoConservacao = 0
    
    def getNome(self):
        return self.__nome
    
    # em um exemplo real, eu colocaria os get/set de cada atributo
    # pra poder preencher cada herança além do nome...

# como só uso o nome deles e nada mais, não tem porque criar nada, mas ainda
# assim parece um pouco esquisito...

class Animal(SerVivo):
    def __init__(self, nome=None):
        super().__init__(nome) #espec

class Vegetal(SerVivo):
    def __init__(self, nome=None):
        super().__init__(nome) #espec

if __name__ == '__main__':
    
    amazonia = Bioma('Amazônia')
    mataAtlantica = Bioma('Mata Atlântica')
    cerrado = Bioma('Cerrado')
    caatinga = Bioma('Caatinga')
    pampa = Bioma('Pampa')
    pantanal = Bioma('Pantanal')

    capivara = Animal('Capivara')
    gralhaAzul = Animal('Gralha azul')
    tamanduaBandeira = Animal ('Tamanduá-bandeira')
    onçaPintada = Animal ('Onça pintada')
    tatuBola = Animal ('Tatu-bola')

    ipeAmarelo = Vegetal('Ipê amarelo')
    araucaria = Vegetal('Araucária')
    mandacaru = Vegetal('Mandacaru')
    vitoriaRegia = Vegetal('Vitória-régia')
    jatoba = Vegetal('Jatobá')

                    #  0          1             2       3       4         5
    listaBiomas = [amazonia, mataAtlantica, cerrado, caatinga, pampa, pantanal]
                    #  0          1             2                3         4
    listaAnimais = [capivara, gralhaAzul, tamanduaBandeira, onçaPintada, tatuBola]
                    #     0         1          2            3           4
    listaVegetais = [ipeAmarelo, araucaria, mandacaru, vitoriaRegia, jatoba]

    for i in range(len(faunaBR)):
       for j in range(len(faunaBR[i])):
            if faunaBR[i][j] == True:
                listaBiomas[j-1].adicionarAnimal(listaAnimais[i])

    for i in range(len(floraBR)):
        for j in range(len(floraBR[i])):
            if floraBR[i][j] == True:
                listaBiomas[j-1].adicionarVegetal(listaVegetais[i])

    print()
    print('---- Componentes da FAUNA de cada Bioma Brasileiro ----\n')
    for i in range(len(listaBiomas)):
        print(f'Bioma: {listaBiomas[i].getNome()}')
        print('Lista de Animais:')
        listaBiomas[i].exibirFauna()
        print()
    
    print('---- Componentes da FLORA de cada Bioma Brasileiro ----\n')
    for i in range(len(listaBiomas)):
        print(f'Bioma: {listaBiomas[i].getNome()}')
        print('Lista de Vegetais:')
        listaBiomas[i].exibirFlora()
        print()