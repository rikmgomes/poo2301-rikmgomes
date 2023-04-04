
import random

# 4) (como os resultados saem tudo de uma vez do jeito que fiz, é necessário scrolar o terminal pra ver o restante... )

class Competidor:
    def __init__(self, nome):
        self.nome = nome
        self.pos = 0
    
    def atualizar(self):
        n = random.randint(1,6)
        # print(n) -> imprimir número rolado pra verificar se as alterações de posição tão certas...
        self.pos = self.pos + n
        if self.pos == 5 or self.pos == 10 or self.pos == 15 or self.pos == 20:
            self.pos = self.pos - 1
        elif self.pos == 7 or self.pos == 17:
            self.pos = self.pos + 2
        elif self.pos == 13:
            self.pos = 0
        else:
            pass

    def getPos(self):
        return self.pos
    
    def getNome(self):
        return self.nome

if __name__ == '__main__':
    # Instânciações do Item 4.
    c1 = Competidor('Azul')
    c2 = Competidor('Vermelho')
    c3 = Competidor('Verde')
    c4 = Competidor('Amarelo')
    c5 = Competidor('Rosa')

    # Corrida Maluca do Item 4.
    terminarCorrida = False
    rodada = 0
    vencedor = 0
    while not terminarCorrida:
        print("..:: Corrida Maluca - Item 4 ::..\n")
        if rodada == 0:
            print("=========")
            print(f"Rodada {rodada}")
            print("=========\n")
            print(f'Competidor = {c1.getNome()} (posição = {c1.getPos()})')
            print(f'Competidor = {c2.getNome()} (posição = {c2.getPos()})')
            print(f'Competidor = {c3.getNome()} (posição = {c3.getPos()})')
            print(f'Competidor = {c4.getNome()} (posição = {c4.getPos()})')
            print(f'Competidor = {c5.getNome()} (posição = {c5.getPos()})\n')
            rodada+=1
        else:
            print("=========")
            print(f"Rodada {rodada}")
            print("=========\n")
            c1.atualizar()
            if c1.getPos() > 20:
                terminarCorrida = True
                vencedor = c1
            else:
                c2.atualizar()
                if c2.getPos() > 20:
                    terminarCorrida = True
                    vencedor = c2
                else:
                    c3.atualizar()
                    if c3.getPos() > 20:
                        terminarCorrida = True
                        vencedor = c3
                    else:
                        c4.atualizar()
                        if c4.getPos() > 20:
                            terminarCorrida = True
                            vencedor = c4
                        else:
                            c5.atualizar()
                            if c5.getPos() > 20:
                                terminarCorrida = True
                                vencedor = c5
            print(f'Competidor = {c1.getNome()} (posição = {c1.getPos()})')
            print(f'Competidor = {c2.getNome()} (posição = {c2.getPos()})')
            print(f'Competidor = {c3.getNome()} (posição = {c3.getPos()})')
            print(f'Competidor = {c4.getNome()} (posição = {c4.getPos()})')
            print(f'Competidor = {c5.getNome()} (posição = {c5.getPos()})\n')
            if not terminarCorrida:
                rodada+=1
    print("========================================")
    print(f"Vencedor = {vencedor.getNome()} (posição final = {vencedor.getPos()})")
    print("========================================\n")