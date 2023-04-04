
import os
import random

# 1)

class Dado:
    def __init__(self, faces):
        self.faces = faces

    def Rolar(self):
        return random.randint(1,self.faces) # anteriormente tinha feito if/else para cada tipo de dado
                                            # mas o jeito que você mostrou na aula definitivamente é melhor hasuhas

if __name__ == '__main__':

    # Instânciações do Item 1.
    seisfaces = Dado(6)
    oitofaces = Dado(8)
    dozefaces = Dado(12)

    # Impressões do Item 1.
    terminarRolagem = False
    while not terminarRolagem:
        print("\n..:: Resultados Dados - Item 1 ::..\n")
        print(f'Roll 1  (d6): {seisfaces.Rolar()} - Roll 2  (d6): {seisfaces.Rolar()} - Roll 3  (d6): {seisfaces.Rolar()}')
        print(f'Roll 1  (d8): {oitofaces.Rolar()} - Roll 2  (d8): {oitofaces.Rolar()} - Roll 3  (d8): {oitofaces.Rolar()}')
        print(f'Roll 1 (d12): {dozefaces.Rolar()} - Roll 2 (d12): {dozefaces.Rolar()} - Roll 3 (d12): {dozefaces.Rolar()}\n')
        acaoUsuario = input('>>>> Pressione 1 para rolar novamente ou 0 para sair! ')
        if acaoUsuario == '0':
            terminarRolagem = True