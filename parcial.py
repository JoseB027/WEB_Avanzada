def distan(p1, p2):
    x = p1[0] - p2[0]
    y = p1[1] - p2[1]
    return (x ** 2 + y ** 2) ** 0.5

def ordenar(puntos):
    for i in range(len(puntos) - 1):
        mini = i
        for j in range(i + 1, len(puntos)):
            if puntos[j][0] < puntos[mini][0]:
                mini = j
        puntos[i], puntos[mini] = puntos[mini], puntos[i]

def pares_mas_cerca(puntos):
    if len(puntos) < 2:
        print("Se necesitan al menos dos puntos")
        return None, None

    ordenar(puntos)
    d_min = distan(puntos[0], puntos[1])
    p_min = [(puntos[0], puntos[1])]

    for i in range(len(puntos) - 1):
        for j in range(i + 1, len(puntos)):
            d_act = distan(puntos[i], puntos[j])
            if d_act < d_min:
                d_min = d_act
                p_min = [(puntos[i], puntos[j])]
            elif d_act == d_min:
                p_min.append((puntos[i], puntos[j]))

    return p_min, d_min

def pares_cercanos(*args):
    puntos = list(args)
    resultado, distan_minima = pares_mas_cerca(puntos)
    return resultado, distan_minima

resultado, distan_minima = pares_cercanos((5, 7), (4, 7), (7, 8), (3, 9), (6, 6), (1, 4))
print("Par más cercano:", resultado)
print("La distancia mínima:", distan_minima)
