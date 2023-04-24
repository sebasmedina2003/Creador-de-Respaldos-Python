from os import listdir, mkdir
from os.path import isdir, exists
from shutil import copy2


def lecturaPaths() -> None:
    """
    Funcion principal del programa, pide 2 directorios, el primero es donde se va a buscar los archivos y el segundo es
    donde se van a copiar los de la extension pedida, se valida la entrada de los paths.
    """
    while True:
        extension = input("Ingrese la extension que desea respaldar: ")
        pathInicio = input("Ingrese el path que desea evaluar: ")
        pathDestino = input("Ingrese el path donde desee copiar: ")

        pathInicio = pathInicio.replace("\\\\", "/")
        pathDestino = pathDestino.replace("\\\\", "/")
        print("")

        if isdir(pathInicio) and isdir(pathDestino):
            break
        elif isdir(pathInicio) and not isdir(pathDestino):
            print("La ruta de destino no existe, ingrese direcciones validas\n")
        else:
            print("La ruta de busqueda no existe, ingrese direcciones validas\n")

    directorioPrincipal = listdir(pathInicio)
    evaluacionSubDirectorios(
        listaDirectorios=directorioPrincipal, path=pathInicio, extension=extension, pathDestino=pathDestino)


def evaluarExtension(archivo: str, pathDestino: str, extension: str, pathArchivo: str) -> None:
    """
    Verifica si la extension del archivo leido es el pedido y si la carpeta del directorio donde se esta evaluando existe en el destino,
    en caso de no existir se crea y luego se hace la copia del archivo, si ya existe solo se hace copia del archivo a destino
    """
    aux = pathArchivo.split("/")
    carpeta = aux[len(aux)-1]
    pathArchivo += f"/{archivo}"
    pathDestino += f"/{carpeta}"

    if (extension in archivo) and (exists(pathDestino)):
        print(f"Copiando {archivo} a {pathDestino}")
        copy2(pathArchivo, pathDestino)

    elif (extension in archivo) and (not exists(pathDestino)):
        print(f"Creando carpeta {carpeta}")
        mkdir(pathDestino)
        print(f"Copiando {archivo} a {pathDestino}")
        copy2(pathArchivo, pathDestino)
    else:
        print(f"Error con el archivo {archivo} en la carpeta {carpeta}")


def evaluacionSubDirectorios(listaDirectorios: list, path: str, extension: str, pathDestino: str) -> None:
    """
    Recorre por un ciclo for los elementos de la lista del directorio actual, en caso de ser una carpeta se
    vuelve a llamar a si misma para recorrerla, sino llama a la funcion evaluarExtension que verifica el tipo de archivo
    y si existe la carpeta en el directorio destino, en caso de no existir la carpeta la crea y copia el archivo
    """
    for subDirectorios in listaDirectorios:
        if (isdir(subDirectorios)) and (not "sys" in subDirectorios.lower()):
            newPath = f"{path}/{subDirectorios}"
            if isdir(newPath):
                directorio = listdir(newPath)
                evaluacionSubDirectorios(
                    listaDirectorios=directorio, path=newPath, extension=extension, pathDestino=pathDestino)
        else:
            evaluarExtension(archivo=subDirectorios, pathDestino=pathDestino,
                             extension=extension, pathArchivo=path)


if __name__ == "__main__":
    lecturaPaths()
    print("")
    input("Precione enter para salir del programa")
