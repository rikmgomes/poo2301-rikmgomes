from Figurinha import Figurinha

class Pagina:
    def __init__(self, titulo=None):
        self.__titulo = titulo
        self.__figurinhas = ["X","X","X","X"]
    
    def setTitulo(self, nome):
        self.__titulo = nome
    
    def getFigurinhas(self):
        return self.__figurinhas
    
    def substituirFigurinha(self,novo, posicao):
        if posicao == 0 or posicao == 4 or posicao == 8 or posicao == 12:
            if self.__figurinhas[0] == "X" or self.__figurinhas[0] == "COLAR":
                self.__figurinhas[0] = novo
        elif posicao == 1 or posicao == 5 or posicao == 9 or posicao == 13:
            if self.__figurinhas[1] == "X" or self.__figurinhas[1] == "COLAR":
                self.__figurinhas[1] = novo
        elif posicao == 2 or posicao == 6 or posicao == 10 or posicao == 14:
            if self.__figurinhas[2] == "X" or self.__figurinhas[2] == "COLAR":
                self.__figurinhas[2] = novo
        else:
            if self.__figurinhas[3] == "X" or self.__figurinhas[3] == "COLAR":
                self.__figurinhas[3] = novo

    def imprimirPagina(self, fator):
        for i in range(len(self.__figurinhas)):
            if self.__figurinhas[i] == "X" or self.__figurinhas[i] == "COLAR":
                print(f"{fator:>2}", ' ', f"{self.__figurinhas[i]:<16}")
            else:
                print(f"{fator:>2}", ' ', f"{self.__figurinhas[i]:<16}", ' ', f"Poder = {fator:<16}")
            fator+=1