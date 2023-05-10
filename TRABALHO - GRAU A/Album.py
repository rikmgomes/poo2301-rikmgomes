from Pagina import Pagina
from Troca import Troca

class Album:
    def __init__(self):
        self.__paginas = [] # +16...                              16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31
        self.__figurinhas = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.__trocaNaoTroca = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        self.__requisicoesTrocas = []
    
    def adicionarPagina(self,pagina):
        self.__paginas.append(pagina)

    def getPaginas(self):
        return self.__paginas

    def getFigurinhas(self):
        return self.__figurinhas

    def getTrocaNaoTroca(self):
        return self.__trocaNaoTroca
    
    def adicionarFigurinha(self,f, n, operacao):
        if operacao == "=":
            self.__figurinhas[f+16] = n
        elif operacao == "+":
            self.__figurinhas[f+16]+=n
        elif operacao == "-":
            self.__figurinhas[f+16]-=n
    
    def adicionarTrocaNaoTroca(self, f, n):
        if n == '0': #troca
            self.__trocaNaoTroca[f+16] = 0
        elif n == "1": #não troca
            self.__trocaNaoTroca[f+16] = 1
    
    def adicionarRequisicaoTroca(self,requisicao):
        self.__requisicoesTrocas.append(requisicao)