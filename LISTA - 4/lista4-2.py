
class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.__marca = ''
        self.__modelo = ''
        self._ano = 0
    
    def acelerar(self):
        print("Acelerando o veículo!")

    def freiar(self):
        print("Freando o veículo!")

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, cor):
        self.__cor = ''
        super().__init__(marca, modelo, ano)
    
    def ligar_radio(self):
        print("Ligando o rádio do carro!")
    
    def abrir_porta(self):
        print("Abrindo a porta do carro!")

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindrada):
        self.__cilindrada = ''
        super().__init__(marca, modelo, ano)
    
    def empinar(self):
        print("Empinando a moto!")

    def buzinar(self):
        print("Buzinando a moto!")

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, ano, carga_maxima):
        self.__carga_maxima = ''
        super().__init__(marca, modelo, ano)
    
    def carregar(self):
        print("Carregando o caminhão!")
    
    def descarregar(self):
        print("Descarregando o caminhão!")