def cargar_archivos(ruta):
	with open(ruta) as archivo:
		for linea in archivo:
			yield linea.strip("\n")