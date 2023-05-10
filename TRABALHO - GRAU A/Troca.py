class Troca:
    def __init__(self, nomeProponente, nomeAceitante, figurinhaRequerida, figurinhaDisponivel, status):
        self.__nomeProponente = nomeProponente
        self.__nomeAceitante = nomeAceitante
        self.__figurinhaRequerida = figurinhaRequerida
        self.__figurinhaDisponivel = figurinhaDisponivel
        self.__status = status
    
    def getNomeProponente(self):
        return self.__nomeProponente

    def getNomeAceitante(self):
        return self.__nomeAceitante
    
    def getFigReq(self):
        return self.__figurinhaRequerida
    
    def getFigDisp(self):
        return self.__figurinhaDisponivel
    
    def getStatus(self):
        return self.__status
    
    def troca(self,quem,figum,figdois):
        self.__nomeProponente = quem #quem propôs a troca
        self.__figurinhaRequerida = figum #figurinha desejada pelo proponente
        self.__figurinhaDisponivel = figdois #figurinha que ele trocará pela desejada

    def aceitar(self,decisao):
        pass