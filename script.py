import os
import requests
import sys


def descargar_input(dia, sesion):
    url = f"https://adventofcode.com/2022/day/{dia}/input"
    respuesta = sesion.get(url)
    if respuesta.status_code == 200:
        return respuesta.text
    else:
        raise Exception(f"Error al descargar el input: HTTP {respuesta.status_code}")


def crear_main_py(dia):
    ruta_template = "template.py"
    ruta_destino = f"day{dia}/main.py"

    with open(ruta_template, 'r') as file:
        contenido = file.read()

    contenido = contenido.replace("Day:", f"Day: {dia}")

    with open(ruta_destino, 'w') as file:
        file.write(contenido)


def main(dia, sesion):
    carpeta_dia = f"day{dia}"
    if not os.path.exists(carpeta_dia):
        os.makedirs(carpeta_dia)

    crear_main_py(dia)

    archivo_input = os.path.join(carpeta_dia, "input.txt")
    with open(archivo_input, "w") as f:
        f.write(descargar_input(dia, sesion))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <dia>")
        sys.exit(1)

    dia = sys.argv[1]
    sesion = requests.Session()

    # Aquí agregas la cookie de sesión
    sesion.cookies.set('session',
                       '53616c7465645f5f7fe382be6c2e13ace12f1d0d0c5e7ace52f1ef470b14ffe1066c40f1a3714daf2dcfe9e0da8cf117e07e384b5d77797d77852109d8ea0098')

    main(dia, sesion)
