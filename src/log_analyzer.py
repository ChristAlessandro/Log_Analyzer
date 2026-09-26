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


def generar_estadisticas(resultados):
	total_eventos = 0
	total_info = 0
	total_warning = 0
	total_error = 0
	total_malformadas = 0

	for resultado in resultados:
		if resultado["nivel_valido"]:
			total_eventos += 1
			if resultado["nivel"] == "INFO":
				total_info += 1
			elif resultado["nivel"] == "WARNING":
				total_warning += 1
			elif resultado["nivel"] == "ERROR":
				total_error += 1

		if not resultado["valida"]:
			total_malformadas += 1

	return {
		"total_eventos": total_eventos,
		"total_info": total_info,
		"total_warning": total_warning,
		"total_error": total_error,
		"total_malformadas": total_malformadas,
	}


def main():
	ruta = seleccionar_archivo()
	lineas = leer_archivo(ruta)

	if lineas is None:
		return

	for numero, linea in enumerate(lineas, start=1):
		resultado = analizar_linea(linea)
		nivel = resultado["nivel"] if resultado["nivel"] is not None else "No detectado"
		fecha = resultado["fecha"] if resultado["fecha"] is not None else "No detectada"
		nivel_valido = "Si" if resultado["nivel_valido"] else "No"
		fecha_valida = "Si" if resultado["fecha_valida"] else "No"
		mensaje_valido = "Si" if resultado["mensaje_valido"] else "No"
		estado_linea = "Valida" if resultado["valida"] else "Malformada"

		print(f"Linea {numero}:")
		print(f"  Nivel detectado: {nivel}")
		print(f"  Fecha detectada: {fecha}")
		print(f"  Nivel valido: {nivel_valido}")
		print(f"  Fecha valida: {fecha_valida}")
		print(f"  Mensaje valido: {mensaje_valido}")
		print(f"  Estado: {estado_linea}")


if __name__ == "__main__":
	main()
