from Album import Album

class Usuario:
    def __init__(self, nome, senha):
        self.__nome = nome
        self.__senha = senha
        self.__album = []

    def getNomeUsuario(self):
        return self.__nome

    def getSenha(self):
        return self.__senha
    
    def setAlbum(self,album):
        self.__album = album
    
    def imprimir(self):
        print(self.__nome,' ',self.__senha)
    
    def verificar(self,nome,senha):
        if self.__nome == nome:
            if self.__senha == senha:
                return True
            else:
                return False
        else:
            return False
    
    def getAlbum(self):
        return self.__album