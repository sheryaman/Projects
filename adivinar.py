import random

Movimientos = ["piedra","tijera","papel"]



puntos_ia = 0
puntos_usuario = 0



while puntos_usuario < 3 and puntos_ia < 3:
      
 Movimiento_IA = random.choice(Movimientos)
 Movimiento_Usuario = input("Introduce Piedra , Papel y Tijera ").lower()

      






 if Movimiento_Usuario.lower() not in Movimientos:
    print("Movimiento no permitido")
    quit()

 print(f"Sacastes {Movimiento_Usuario}")
 print(f"IA Saco {Movimiento_IA}")

 if Movimiento_Usuario == "piedra":
    if Movimiento_IA == "piedra":
        print("Empate")
    elif Movimiento_IA == "tijera":
        print("Has Ganado")
        puntos_usuario += 1
    elif Movimiento_IA == "papel":
        print("Perdistes")
        puntos_ia += 1
 elif  Movimiento_Usuario == "tijera":
    if Movimiento_IA == "tijera":
        print("Empate")
    elif Movimiento_IA =="piedra":
        print("Perdistes")
        puntos_ia += 1
    elif Movimiento_IA == "papel":
        print("Ganastes")
        puntos_usuario += 1
 elif Movimiento_Usuario == "papel":
    if Movimiento_IA == "papel":
        print("Empate")
    elif Movimiento_IA == "tijera":
        print("Perdistes")
        puntos_ia += 1
    elif Movimiento_IA == "piedra":
        print("Ganastes")
        puntos_usuario += 1
 print(f"Marcador:{puntos_usuario}-{puntos_ia}")




if puntos_ia > puntos_usuario:
    print("Perdistes Ante Una IA ")
elif puntos_ia < puntos_usuario:
    print("Ganastes sientete orgulloso")


