
# 1)

class Pais:

    # a) Construtor.
    def __init__(self, codigoIso=None, nome=None, dimensao=None):
        self.__codigoIso = codigoIso
        self.__nome = nome
        self.__dimensao = dimensao
        self.__populacao = 0
        self.__vizinhos = []
    
    # b) Metódos de Acesso.
    def setCodigoIso(self, codigoIso):
        self.__codigoIso = codigoIso
    
    def getCodigoIso(self):
        return self.__codigoIso
    
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
    
    def setVizinhos(self, pais):
        self.__vizinhos.append(pais)
    
    def getVizinhos(self):
        return self.__vizinhos

    def imprimirVizinhos(self):
        vizinhos = []
        for i in self.__vizinhos:
            vizinhos.append(i.getNome())
        return vizinhos
    
    # c) Método de Comparação.
    def mesmoPais(self, pais):
        if self.__codigoIso == pais.getCodigoIso():
            return True #mesmo codigo iso, logo mesmo pais...
        else:
            return False #codigos iso diferentes, logo paises diferentes...
    
    # d) Verificar se é vizinho.
    def verificarSeLimitrofe(self, pais):
        for i in self.__vizinhos:
            if i.mesmoPais(pais) == True:
                return True
        return False
    
    # e) Método que calcula Densidade Populacional.
    def densidadePopulacional(self):
        densidade = self.__populacao / self.__dimensao
        return densidade
    
    # f) Método que retorna Lista de Vizinhos comuns entre 2 países.
    def vizinhosComuns(self, pais):
        vizinhosPais = pais.getVizinhos()
        vizinhosComuns = []
        for i in vizinhosPais:
            if self.verificarSeLimitrofe(i) == True:
                vizinhosComuns.append(i)
        return vizinhosComuns

# Programa Principal com Chamadas Testes.
if __name__ == '__main__':

    # Instânciações SEM get/set.
    angola = Pais('AGO', 'Angola', 1246700)
    namibia = Pais('NAM', 'Namibia', 824292)
    repDemCongo = Pais('COD', 'Republica Democratica do Congo', 2345000)

    egito = Pais('EGY', 'Egito', 1002000)
    libia = Pais('LBY', 'Libia', 1760000)
    sudao = Pais('SUD', 'Sudao', 1886000)

    # Instânciações COM get/set + Chamadas teste.
    sudaoSul = Pais()
    sudaoSul.setCodigoIso('SSD')
    sudaoSul.setNome('Sudao do Sul')
    sudaoSul.setDimensao(644329)
    sudaoSul.setPopulacao(10750000)
    sudaoSul.setVizinhos(sudao)
    sudaoSul.setVizinhos(repDemCongo)

    print('\n--- Informações Sudão do Sul ---\n')
    print(f'Código Iso = {sudaoSul.getCodigoIso()}')
    print(f'Nome = {sudaoSul.getNome()}')
    print(f'Dimensão = {sudaoSul.getDimensao()} km2')
    print(f'População = {sudaoSul.getPopulacao()} habitantes')
    print(f'Vizinhos = {sudaoSul.imprimirVizinhos()}')
    print(f'Densidade Pop. = {sudaoSul.densidadePopulacional():.2f} hab/km2')
    print()

    angola.setVizinhos(namibia)
    angola.setVizinhos(repDemCongo)
    egito.setVizinhos(libia)
    egito.setVizinhos(sudao)

    sudao.setVizinhos(sudaoSul)
    repDemCongo.setVizinhos(sudaoSul)

    print(f'--- Sudão é o Mesmo País que Sudão do Sul? {sudao.mesmoPais(sudaoSul)} ---\n')

    print(f'--- Rep. Dem. do Congo e Angola são Vizinhos? {angola.verificarSeLimitrofe(repDemCongo)} ---\n')

    print('--- Vizinhos Comuns de Sudão do Sul e da Angola são? ---\n')
    vAngolaSudaoSul = angola.vizinhosComuns(sudaoSul)
    for i in vAngolaSudaoSul:
        print(f'- {i.getNome()}')
    print()