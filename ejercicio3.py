producto = [
    {
        "ID": 123,
        "nombre": "libreta",
        "precio": 12.500,
        "ID_cat": 1
    },
    {
        "ID": 345,
        "nombre": "Jabón",
        "precio": 10.500,
        "ID_cat": 2
    }
]

categoria = [
    {
        "ID_cat": 1,
        "nombre": "Utiles escolares"
    },
    {
        "ID_cat": 2,
        "nombre": "Aseo"
    }
]
new_diccionario = [
    {
        "ID": p["ID"],
        "nombre": p["nombre"],
        "Categoria": c["nombre"]
    }
    for p in producto
    for c in categoria
    if p["ID_cat"] == c["ID_cat"]
]

for dic in new_diccionario:
    print("Nuevo diccionario: ", dic)