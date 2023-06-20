import random

class Equipe:
    def __init__(self, nome, vitorias):
        self._nome = nome
        self._vitorias = 0
        self._listaCompetidores = []
    
    def adicionarCompetidor(self,competidor):
        self._listaCompetidores.append(competidor)
    
    def getNome(self):
        return self._nome
    
    def getVitorias(self):
        return self._vitorias
    
    def getListaCompetidores(self):
        return self._listaCompetidores
    
    def setVitoria(self):
        self._vitorias+=1
    
class Competidor:
    def __init__(self, nome, vitoriasPessoais):
        self._nome = nome
        self._vitoriasPessoais = vitoriasPessoais
    
    def getNome(self):
        return self._nome
    
    def getVitoriasPessoais(self):
        return self._vitoriasPessoais
    
    def setVitoriaPessoal(self):
        self._vitoriasPessoais+=1

competidores = []
competidorUm = Competidor("C1", 0)
competidorDois = Competidor("C2", 0)
competidorTres = Competidor("C3", 0)
competidorQuatro = Competidor("C4", 0)
competidorCinco = Competidor("C5", 0)
competidorSeis = Competidor("C6", 0)
competidores.append(competidorUm)
competidores.append(competidorDois)
competidores.append(competidorTres)
competidores.append(competidorQuatro)
competidores.append(competidorCinco)
competidores.append(competidorSeis)

equipeUm = Equipe("Equipe 1", 0)
equipeUm.adicionarCompetidor(competidorUm)
equipeUm.adicionarCompetidor(competidorDois)
equipeUm.adicionarCompetidor(competidorTres)

equipeDois = Equipe("Equipe 2", 0)
equipeDois.adicionarCompetidor(competidorQuatro)
equipeDois.adicionarCompetidor(competidorCinco)
equipeDois.adicionarCompetidor(competidorSeis)

terminou = False
indiceEquipeUm = 0 #vai variar 0-1-2 (c1, c2, c3...
indiceEquipeDois = 0 #... ou c4, c5, c6)
rodada = 1
print("\n============Início da Competição!!!============")
while not terminou:
    print(f"\n>>>>>>>> Rodada {rodada}")
    jogadaUm = random.randint(0,2)
    jogadaDois = random.randint(0,2)
    # debug - print(jogadaUm, jogadaDois)
    if jogadaUm == 0:
        jogadaUmPrint = "Pedra"
    elif jogadaUm == 1:
        jogadaUmPrint = "Papel"
    else:
        jogadaUmPrint = "Tesoura"
    
    if jogadaDois == 0:
        jogadaDoisPrint = "Pedra"
    elif jogadaDois == 1:
        jogadaDoisPrint = "Papel"
    else:
        jogadaDoisPrint = "Tesoura"
    print(f"\nCompetidor (Equipe 1) | Nome = {equipeUm.getListaCompetidores()[indiceEquipeUm].getNome()} | {jogadaUmPrint}")
    print(f"Competidor (Equipe 2) | Nome = {equipeDois.getListaCompetidores()[indiceEquipeDois].getNome()} | {jogadaDoisPrint}")
    
    if jogadaUm == jogadaDois: #empate (00 - 11 - 22)
        rodada-=1
        # debug - print("empate")
    elif (jogadaDois == 0) and (jogadaUm == 2): # 20 (e2 ganha)
        # debug - print("20")
        competidorGanhador = equipeDois.getListaCompetidores()[indiceEquipeDois] 
        competidorGanhador.setVitoriaPessoal()
        equipeDois.setVitoria()
        if indiceEquipeUm == 0:
            indiceEquipeUm = 1
        elif indiceEquipeUm == 1:
            indiceEquipeUm = 2
        elif indiceEquipeUm == 2:
            indiceEquipeUm = 0
    elif (jogadaUm == 0) and (jogadaDois == 2): # 02 (e1 ganha)
        # debug - print("02")
        competidorGanhador = equipeUm.getListaCompetidores()[indiceEquipeUm]
        competidorGanhador.setVitoriaPessoal()
        equipeUm.setVitoria()
        if indiceEquipeDois == 0:
            indiceEquipeDois = 1
        elif indiceEquipeDois == 1:
            indiceEquipeDois = 2
        elif indiceEquipeDois == 2:
            indiceEquipeDois = 0
    elif jogadaDois > jogadaUm: # e2 maior (01 - 12)
        # debug - print("dois maior")
        competidorGanhador = equipeDois.getListaCompetidores()[indiceEquipeDois]
        competidorGanhador.setVitoriaPessoal()
        equipeDois.setVitoria()
        if indiceEquipeUm == 0:
            indiceEquipeUm = 1
        elif indiceEquipeUm == 1:
            indiceEquipeUm = 2
        elif indiceEquipeUm == 2:
            indiceEquipeUm = 0
    elif jogadaUm > jogadaDois: # e1 maior (10 - 21)
        # debug - print("um maior")
        competidorGanhador = equipeUm.getListaCompetidores()[indiceEquipeUm]
        competidorGanhador.setVitoriaPessoal()
        equipeUm.setVitoria()
        if indiceEquipeDois == 0:
            indiceEquipeDois = 1
        elif indiceEquipeDois == 1:
            indiceEquipeDois = 2
        elif indiceEquipeDois == 2:
            indiceEquipeDois = 0
    
    if equipeUm.getVitorias() >= 10:
        terminou = True
        equipeGanhadora = equipeUm
    if equipeDois.getVitorias() >= 10:
        terminou = True
        equipeGanhadora = equipeDois
    rodada+=1

competidorVitorioso = Competidor("C0", -1)

for i in competidores:
    if i.getVitoriasPessoais() > competidorVitorioso.getVitoriasPessoais():
        competidorVitorioso = i

print("\n============Final da Competição!!!============")
print(f"\nEquipe Vencedora = {equipeGanhadora.getNome()} | Vitorias = {equipeGanhadora.getVitorias()}")
print(f"Competidor mais Vitorioso = {competidorVitorioso.getNome()} | Vitorias = {competidorVitorioso.getVitoriasPessoais()}")
print()