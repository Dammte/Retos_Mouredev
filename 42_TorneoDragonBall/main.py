import random

personajes = [
    {"nombre": "Goku", "velocidad": 95, "ataque": 100, "defensa": 90, "salud": 100},
    {"nombre": "Vegeta", "velocidad": 90, "ataque": 98, "defensa": 88, "salud": 100},
    {"nombre": "Piccolo", "velocidad": 75, "ataque": 80, "defensa": 85, "salud": 100},
    {"nombre": "Gohan", "velocidad": 85, "ataque": 95, "defensa": 82, "salud": 100},
    {"nombre": "Krillin", "velocidad": 70, "ataque": 65, "defensa": 60, "salud": 100},
    {"nombre": "Yamcha", "velocidad": 68, "ataque": 60, "defensa": 55, "salud": 100},
    {"nombre": "Tien Shin Han", "velocidad": 72, "ataque": 70, "defensa": 65, "salud": 100},
    {"nombre": "Trunks", "velocidad": 88, "ataque": 92, "defensa": 80, "salud": 100},
    {"nombre": "Goten", "velocidad": 84, "ataque": 85, "defensa": 75, "salud": 100},
    {"nombre": "Androide 18", "velocidad": 85, "ataque": 88, "defensa": 85, "salud": 100},
    {"nombre": "Androide 17", "velocidad": 87, "ataque": 90, "defensa": 88, "salud": 100},
    {"nombre": "Frezzer", "velocidad": 88, "ataque": 95, "defensa": 90, "salud": 100},
    {"nombre": "Cell", "velocidad": 90, "ataque": 98, "defensa": 92, "salud": 100},
    {"nombre": "Majin Buu", "velocidad": 78, "ataque": 92, "defensa": 95, "salud": 100},
    {"nombre": "Kid Buu", "velocidad": 90, "ataque": 95, "defensa": 80, "salud": 100},
    {"nombre": "Bills", "velocidad": 95, "ataque": 100, "defensa": 98, "salud": 100},
    {"nombre": "Whis", "velocidad": 98, "ataque": 100, "defensa": 100, "salud": 100},
    {"nombre": "Broly", "velocidad": 85, "ataque": 100, "defensa": 90, "salud": 100},
    {"nombre": "Jiren", "velocidad": 95, "ataque": 100, "defensa": 100, "salud": 100},
    {"nombre": "Toppo", "velocidad": 85, "ataque": 90, "defensa": 95, "salud": 100}
]

def esquivar():
    return random.random() < 0.2

def calcular_dano(atacante, defensor):
    if esquivar():
        print(f"{defensor['nombre']} esquiva el ataque!")
        return 0

    dano = atacante["ataque"] - defensor["defensa"]

    if defensor["defensa"] > atacante["ataque"]:
        dano = max(dano * 0.1, 0)

    return max(dano, 0)

def combate(p1, p2):
    print(f"\n¡Comienza el combate: {p1['nombre']} vs {p2['nombre']}!")

    if p1["velocidad"] >= p2["velocidad"]:
        atacante, defensor = p1, p2
    else:
        atacante, defensor = p2, p1

    while atacante["salud"] > 0 and defensor["salud"] > 0:
        dano = calcular_dano(atacante, defensor)
        
        if dano > 0:
            defensor["salud"] -= dano
            print(f"{atacante['nombre']} ataca a {defensor['nombre']} infligiendo {dano} de daño.")
        else:
            print(f"{atacante['nombre']} no logra golpear a {defensor['nombre']}.")

        print(f"{defensor['nombre']} tiene {defensor['salud']} de salud restante.")

        atacante, defensor = defensor, atacante

    if defensor["salud"] <= 0:
        print(f"{atacante['nombre']} ha ganado el combate!")
    else:
        print(f"{defensor['nombre']} ha ganado el combate!")

def torneo(luchadores):
    while len(luchadores) > 1:
        print("\n¡Nueva ronda!")
        random.shuffle(luchadores)
        ganadores = []

        for i in range(0, len(luchadores), 2):
            p1 = luchadores[i]
            p2 = luchadores[i + 1]
            combate(p1, p2)
            ganadores.append(p2 if p1["salud"] <= 0 else p1)

        luchadores = ganadores

    print(f"\n¡El ganador del torneo es {luchadores[0]['nombre']}!")

cantParticipantes = int(input("¿Cuántos luchadores participarán en el torneo? (debe ser una potencia de 2, entre 2 y 16): "))

if cantParticipantes < 2 or cantParticipantes > 16 or (cantParticipantes & (cantParticipantes - 1)) != 0:
    print("La cantidad de luchadores debe ser una potencia de 2 entre 2 y 16.")
else:
    luchadores_torneo = random.sample(personajes, cantParticipantes)
    torneo(luchadores_torneo)
