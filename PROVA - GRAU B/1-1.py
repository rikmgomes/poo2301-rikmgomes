
class CorpoCeleste:
    def __init__(self, nome=None, diametro=None, composicao=None):
        self._nome = nome #string
        self._diametro = diametro #float
        self._composicao = composicao #string
    
    def exibirInformacoes(self):
        print("----------Informacoes do Corpo Celeste----------")
        print(f"Nome = {self._nome}")
        print(f"Diametro (km) = {self._diametro}")
        print(f"Composicao = {self._composicao}")

class Planeta(CorpoCeleste):
    def __init__(self, nome=None, diametro=None, composicao=None, luas=None, atmosfera=None):
        super().__init__(nome, diametro, composicao)
        self._luas = luas
        self._atmosfera = atmosfera
    
    def exibirInformacoes(self):
        super().exibirInformacoes()
        print(f"Numero de Luas = {self._luas}")
        print(f"Tipo de atmosfera = {self._atmosfera}")

class Satelite(CorpoCeleste):
    def __init__(self, nome=None, diametro=None, composicao=None, planetaOrbita=None, periodoOrbita=None):
        super().__init__(nome, diametro, composicao)
        self._planetaOrbita = planetaOrbita
        self._periodoOrbita = periodoOrbita
    
    def exibirInformacoes(self):
        super().exibirInformacoes()
        print(f"Planeta de orbita = {self._planetaOrbita}")
        print(f"Periodo de orbita (Dias) = {self._periodoOrbita}")

class Estrela(CorpoCeleste):
    def __init__(self, nome=None, diametro=None, composicao=None, temperatura=None, tipoEspectral=None):
        super().__init__(nome, diametro, composicao)
        self._temperatura = temperatura
        self._tipoEspectral = tipoEspectral
    
    def exibirInformacoes(self):
        super().exibirInformacoes()
        print(f"Temperatura (K) = {self._temperatura}")
        print(f"Tipo Espectral = {self._tipoEspectral}")

corposCelestes = []
planetaUm = Planeta("Terra", 12742.0, "A crosta, o manto, o núcleo, a litosfera e a mesosfera compõem a estrutura terrestre.", 1, "É composta basicamente de uma mistura percentual de gases, sendo 78 de Nitrogênio, 21 de Oxigênio e 1 de Argônio.")
sateliteUm = Satelite("Lua", 3474.8, "Na crosta lunar encontramos oxigênio, silício, magnésio, ferro, cálcio, alumínio e pequenas quantidades de titânio, urânio, tório, potássio e hidrogênio.", "Terra", 27.32)
estrelaUm = Estrela("Sol", 1392700.0, "Os gases hélio e hidrogênio representam, em conjunto, 98 por cento da composição do Sol, sendo o restante formado por metais e outros elementos químicos como o carbono e oxigênio.", 5772.0,"G2V")
corposCelestes.append(planetaUm)
corposCelestes.append(sateliteUm)
corposCelestes.append(estrelaUm)

for i in corposCelestes:
    print()
    i.exibirInformacoes()
print()