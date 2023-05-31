
class Assinatura:
    def __init__(self, tipo, preco=None, detalhes=None):
        self._tipo = tipo
        self._preco = preco
        self._detalhes = detalhes

    def calcular_preco(self):
        return self._preco

    def exibir_detalhes(self):
        print(self._detalhes)

class AssinaturaSimples(Assinatura):
    def __init__(self, tipo, preco=None, detalhes=None):
        super().__init__(tipo, preco, detalhes)

    def calcular_preco(self):
        return "R$ 29.99"

    def exibir_detalhes(self):
        print("Uma assinatura básica que fornece acesso a filmes e séries em qualidade padrão.")

class AssinaturaPremium(Assinatura):
    def __init__(self, tipo, preco=None, detalhes=None):
        super().__init__(tipo, preco, detalhes)
    
    def calcular_preco(self):
        return "R$ 49.99"

    def exibir_detalhes(self):
        print("Uma assinatura avançada que oferece acesso a filmes e séries em qualidade HD e Ultra HD.")

aUm = AssinaturaSimples("Simples")
aDois = AssinaturaPremium("Premium")

assinaturas = []
assinaturas.append(aUm)
assinaturas.append(aDois)

for i in assinaturas:
    print(i._tipo)
    print(i.calcular_preco())
    i.exibir_detalhes()