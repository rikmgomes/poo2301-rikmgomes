
class UnidadeMilitar:
    def __init__(self):
        pass

    def mover(self):
        print("A unidade está movendo!!!")
    
    def atacar(self):
        print("A unidade está atacando!!!")

class Soldado(UnidadeMilitar):
    def __init__(self):
        super().__init__()
    
    def mover(self):
        print("A unidade está se movendo a pé!")

    def atacar(self):
        print("A unidade está atacando com espada!")

class Arqueiro(UnidadeMilitar):
    def __init__(self):
        super().__init__()
    
    def mover(self):
        print("A unidade está parada longe do confronto!")

    def atacar(self):
        print("A unidade está atacando de longe com uma saraivada de flechas!")

class Cavaleiro(UnidadeMilitar):
    def __init__(self):
        super().__init__()
    
    def mover(self):
        print("A unidade está se movendo a cavalo!")

    def atacar(self):
        print("A unidade está atacando com uma lança montada!")

soldado_um = Soldado()
arqueiro_um = Arqueiro()
cavaleiro_um = Cavaleiro()

unidades = []
unidades.append(soldado_um)
unidades.append(arqueiro_um)
unidades.append(cavaleiro_um)

for i in unidades:
    i.mover()
    i.atacar()