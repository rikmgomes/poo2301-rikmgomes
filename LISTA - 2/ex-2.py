
import os
import random

# 2)

class Calculadora:
    def __init__(self):
        pass
    
    def SomarDoisNumeros(self, n1, n2):
        soma = n1 + n2
        return soma

    def SubtrairDoisNumeros(self, n1, n2):
        subtracao = n1 - n2
        return subtracao

    def MultiplicarDoisNumeros(self, n1, n2):
        multiplicacao = n1 * n2
        return multiplicacao

    def DividirDoisNumeros(self, n1, n2):
        if n2 == 0:
            print("Não é possível dividir por 0!")
            return (-1)
        else:
            divisao = n1 / n2
            return divisao

if __name__ == '__main__':
    
    # por algum motivo, ele não reconhece apenas o primeiro parâmetro...
    # caso veja antes, irei perguntar sobre em aula.

    a = Calculadora.SomarDoisNumeros(0, 5, 5) 
    b = Calculadora.SubtrairDoisNumeros(0, 5, 5) 
    c = Calculadora.MultiplicarDoisNumeros(0, 5, 5) 
    d = Calculadora.DividirDoisNumeros(0, 5, 5)
    e = Calculadora.DividirDoisNumeros(0, 5, 0) 

    print(a, b, c, d, e)