from datetime import datetime
from trello import TrelloClient

# Inicializar el cliente de Trellaaaaa CAMBIO NUEVA RAMA3 main4git 4
# Inicializar el cliente de Trello
# chanchito feliz

client = TrelloClient(
    api_key='9d1beeb421bfd6779739f4365fb69fc7',
    token='4c1bc7cbd81cb06ef500198852bc30fabdf5618dcd36c48c20635f22455b43fe'
)


# Inicializar un diccionario para almacenar los subtotales por mes
dic_proyectos = {
    "etapa": [],
    "proyecto": [],
    "fecha": [],
    "id_tarjeta": [],
    "presupuesto": []}

proyectos_por_etapa = {}


# llamo al metodo .list_boards() que me devuelve una lista con todos los tableros
all_boards = client.list_boards()

subtotal = 0

# Identifica el tablero que tiene el nombre "PROYECTOS"
tablero_proyectos = next(
    (t for t in client.list_boards() if t.name == "PROYECTOS"), None)


if tablero_proyectos:

    # Lista los nombres de las listas que quieres explorar
    nombres_listas = ["Ante proyecto", "Entregado a Cliente"]

    for nombre_lista in nombres_listas:
        lista = next((l for l in tablero_proyectos.list_lists()
                     if l.name == nombre_lista), None)
        print("esto es del for lista =", nombre_lista)
        if lista:
            print(f"Tarjetas en '{nombre_lista}':")
            dic_proyectos["etapa"].append(nombre_lista)
            tarjetas = lista.list_cards()

            for tarjeta in tarjetas:
                # Cargar los detalles de la tarjeta, incluyendo campos personalizados
                tarjeta.fetch(eager=True)
                fecha_evento = next(
                    (campo.value for campo in tarjeta.custom_fields if campo.name == 'fecha del evento'), None)
                print(f"  - {tarjeta.name}, Fecha: {fecha_evento}")
                dic_proyectos["fecha"].append(fecha_evento)
                dic_proyectos["proyecto"].append(tarjeta.name)

# Iterar sobre los proyectos y agruparlos por etapa
for proyecto, detalles in dic_proyectos.items():
    etapa = detalles["etapa"]
    if etapa in proyectos_por_etapa:
        proyectos_por_etapa[etapa].append((proyecto, detalles))
    else:
        proyectos_por_etapa[etapa] = [(proyecto, detalles)]

# Imprimir los proyectos agrupados por etapa
for etapa, proyectos in proyectos_por_etapa.items():
    print(f"--- Proyectos en la etapa {etapa} ---")
    for proyecto, detalles in proyectos:
        print(f"Proyecto: {proyecto}")
        print(f"  Fecha: {detalles['fecha']}")
        print(f"  Presupuesto: {detalles['presupuesto']}")
