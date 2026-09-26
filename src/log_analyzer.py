import os
from datetime import datetime


def seleccionar_archivo():
	return input("Ingrese la ruta del archivo de texto: ")


def leer_archivo(ruta):
	if not os.path.exists(ruta):
		print("El archivo no existe.")
		return None

	with open(ruta, "r", encoding="utf-8") as archivo:
		return archivo.readlines()


def validar_nivel(nivel):
	return nivel in ("INFO", "WARNING", "ERROR")


def validar_fecha(fecha):
	try:
		fecha_parseada = datetime.strptime(fecha, "%Y-%m-%d")
	except ValueError:
		return False

	return fecha_parseada.strftime("%Y-%m-%d") == fecha


def analizar_linea(linea):
	contenido = linea.strip()
	nivel = None
	fecha = None
	mensaje = None
	estructura_valida = False

	if contenido.startswith("[") and "]" in contenido:
		cierre_nivel = contenido.find("]")
		nivel = contenido[1:cierre_nivel]
		resto = contenido[cierre_nivel + 1:]
		estructura_valida = bool(resto) and resto[0].isspace()
		partes = resto.split(maxsplit=1)

		if partes:
			fecha = partes[0]
		if len(partes) > 1:
			mensaje = partes[1]

	nivel_valido = validar_nivel(nivel) if nivel is not None else False
	fecha_valida = validar_fecha(fecha) if fecha is not None else False
	mensaje_valido = mensaje is not None and bool(mensaje.strip())
	valida = estructura_valida and nivel_valido and fecha_valida and mensaje_valido

	return {
		"nivel": nivel,
		"fecha": fecha,
		"mensaje": mensaje,
		"nivel_valido": nivel_valido,
		"fecha_valida": fecha_valida,
		"mensaje_valido": mensaje_valido,
		"valida": valida,
	}


def main():
	ruta = seleccionar_archivo()
	lineas = leer_archivo(ruta)

	if lineas is None:
		return

	for linea in lineas:
		print(linea, end="")


if __name__ == "__main__":
	main()
