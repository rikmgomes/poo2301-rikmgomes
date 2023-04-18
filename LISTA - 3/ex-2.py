
# 2)

class Continente:

    # a) Construtor que inicialize o nome do continente.
    def __init__(self, nome=None):
        self.__nome = nome
        self.__paises = []

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome
    
    def getPaises(self):
        return self.__paises
    
    # b) Um método que permita adicionar países aos continentes.
    def setPais(self, pais):
        self.__paises.append(pais)

    # c) Um método que retorne a dimensão total do continente.
    def dimensaoTotal(self):
        dtotal = 0
        for i in self.__paises:
            dtotal = dtotal + i.getDimensao()
        return dtotal

    # d) Um método que retorne a população total do continente.
    def popTotal(self):
        ptotal = 0
        for i in self.__paises:
            ptotal = ptotal + i.getPopulacao()
        return ptotal

    # e) Um método que retorne a densidade populacional do continente.
    def denPop(self):
        densidade = self.popTotal() / self.dimensaoTotal()
        return densidade

    # f) Um método que retorne o país com maior população no continente.
    def paisMaiorPop(self):
        maiorPais = 'x'
        maiorPop = 0
        popAtual = 0
        for i in self.__paises:
            popAtual = i.getPopulacao()
            if popAtual > maiorPop:
                maiorPop = popAtual
                maiorPais = i
        return maiorPais

    # g) Um método que retorne o país com menor população no continente.
    def paisMenorPop(self):
        menorPais = 'x'
        menorPop = 100000000000000
        popAtual = 0
        for i in self.__paises:
            popAtual = i.getPopulacao()
            if popAtual < menorPop:
                menorPop = popAtual
                menorPais = i
        return menorPais

    # h) Um método que retorne o país de maior dimensão territorial no continente.
    def paisMaiorDim(self):
        maiorPais = 'x'
        maiorDim = 0
        dimAtual = 0
        for i in self.__paises:
            dimAtual = i.getDimensao()
            if dimAtual > maiorDim:
                maiorDim = dimAtual
                maiorPais = i
        return maiorPais

    # i) Um método que retorne o país de menor dimensão territorial no continente.
    def paisMenorDim(self):
        menorPais = 'x'
        menorDim = 100000000000000
        dimAtual = 0
        for i in self.__paises:
            dimAtual = i.getPopulacao()
            if dimAtual < menorDim:
                menorDim = dimAtual
                menorPais = i
        return menorPais

    # j) Um método que retorne a razão territorial do maior país em relação ao menor país.
    # Aqui não sei se resolvi o problema correto. Pesquisei e não encontrei nenhum conceito chamado "razão territorial", então apenas
    # fiz uma divisão dos territórios na ordem pedida.
    def razaoTerritorial(self):
        razao = (self.paisMaiorDim()).getDimensao() / (self.paisMenorDim()).getDimensao() # Quando entendi que eu conseguiria alinhar mais de um método - e de classes diferentes ainda por cima -, pude ouvir um grande estalo ahushas!!
        return razao

class Pais: #mesma classe do ex1 só que enxugada apenas com os atributos e métodos necessários
    def __init__(self, codigoIso=None, nome=None, dimensao=None):
        self.__nome = nome
        self.__dimensao = dimensao
        self.__populacao = 0
    
    def setNome(self, nome):
        self.__nome = nome
    
    def getNome(self):
        return self.__nome
    
    def setDimensao(self, dimensao):
        self.__dimensao = dimensao
    
    def getDimensao(self):
        return self.__dimensao
    
    def setPopulacao(self, valor):
        self.__populacao = valor

    def getPopulacao(self):
        return self.__populacao

if __name__ == '__main__':

    # Algumas instanciações teste de países + pop...
    namibia = Pais('NAM', 'Namibia', 824292)
    namibia.setPopulacao(2053000)
    angola = Pais('AGO', 'Angola', 1246700)
    angola.setPopulacao(34005000)
    repDemCongo = Pais('COD', 'Republica Democratica do Congo', 2345000)
    repDemCongo.setPopulacao(95089000)
    egito = Pais('EGY', 'Egito', 1002000)
    egito.setPopulacao(109003000)
    libia = Pais('LBY', 'Libia', 1760000)
    libia.setPopulacao(6735000)
    sudao = Pais('SUD', 'Sudao', 1886000)
    sudao.setPopulacao(45066000)

    # Algumas instanciações/sets de teste do continente...
    africa = Continente('Africa')
    africa.setPais(namibia)
    africa.setPais(angola)
    africa.setPais(repDemCongo)
    africa.setPais(egito)
    africa.setPais(libia)
    africa.setPais(sudao)

    # Impressões na tela + testes...
    print('\n--- Informações do Continente Africano (incompleto) ---\n') # incompleto pois não settei todos os 54 países do continente...
    print(f'Dimensão Total = {africa.dimensaoTotal()} km2')
    print(f'População Total = {africa.popTotal()} habitantes')
    print(f'Densidade Populacional = {africa.denPop():.2f} hab/km2')
    print(f'País com Maior População = {(africa.paisMaiorPop()).getNome()} | Pop. = {(africa.paisMaiorPop()).getPopulacao()} habitantes')
    print(f'País com Menor População = {(africa.paisMenorPop()).getNome()} | Pop. = {(africa.paisMenorPop()).getPopulacao()} habitantes')
    print(f'País com Maior Dimensão Territorial = {(africa.paisMaiorDim()).getNome()} | Dim. = {(africa.paisMaiorDim()).getDimensao()} km2')
    print(f'País com Menor Dimensão Territorial = {(africa.paisMenorDim()).getNome()} | Dim. = {(africa.paisMenorDim()).getDimensao()} km2')
    print(f'Razão territorial entre o Maior e o Menor país = {africa.razaoTerritorial():.2f}')
    print()