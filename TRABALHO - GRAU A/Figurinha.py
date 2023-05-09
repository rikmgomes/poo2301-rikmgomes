class Figurinha:
    def __init__(self,nro,nome,conteudo,nroPagina):
        self.__nro = nro
        self.__nome = nome
        self.__conteudo = conteudo
        self.__nroPagina = nroPagina

    def imprimir(self):
        print(self.__nro,' ',self.__nome,' ', self.__conteudo, ' ', self.__nroPagina)
    
    def getNome(self):
        return self.__nome
    
    def getNumero(self):
        return self.__nro
    
    def getConteudo(self):
        return self.__conteudo