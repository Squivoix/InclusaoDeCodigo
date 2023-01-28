from Biblioteca import *

cod = 0
valor = 0

print("Digite um número: \n1 - Área do Círculo \n2 - Perímetro do Círculo \n3 - Área do Quadrado \n4 - Perímetro do Quadrado \n9 - Sair\n")

while cod != 9 :
    cod = int(input("Código: "))
    
    if cod == 1 : # Área do Círculo
        valor = int(input("Digite o raio do círculo: "))
        print("A área do círculo é:", AreaCirculo(valor))
    elif cod == 2 : # Perímetro do Círculo
        valor = int(input("Digite o raio do círculo: "))
        print("O perímetro do círculo é:", PerimetroCirculo(valor))
    elif cod == 3 : # Área do Quadrado
        valor = int(input("Digite o lado do quadrado: "))
        print("A área do quadrado é:", AreaQuadrado(valor))
    elif cod == 4 : # Perímetro do Quadrado
        valor = int(input("Digite o perímetro do quadrado: "))
        print("O perímetro do quadrado é:", PerimetroQuadrado(valor))
    else :
        if cod != 9 : 
            print("Código não existe!")
        else :
            print("Fechando programa!")