import os


def seleccionar_archivo():
	return input("Ingrese la ruta del archivo de texto: ")


def leer_archivo(ruta):
	if not os.path.exists(ruta):
		print("El archivo no existe.")
		return None

	with open(ruta, "r", encoding="utf-8") as archivo:
		return archivo.readlines()


def main():
	ruta = seleccionar_archivo()
	lineas = leer_archivo(ruta)

	if lineas is None:
		return

	for linea in lineas:
		print(linea, end="")


if __name__ == "__main__":
	main()
