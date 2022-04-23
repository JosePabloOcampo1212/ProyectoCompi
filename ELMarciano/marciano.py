#Compilador para El Marciano

# - - - [ Imports ] - - -
from utils import archivos as utils
from explorador.Explorador import Explorador
import argparse


# - - - [ Parser ] - - -
from utils.archivos import readText

parser = argparse.ArgumentParser(description= 'Compilador Marciano')

parser.add_argument('-explorar', dest='explorador', action='store_true', help='ejecuta el explorador y retorna los componentes lexicos')

parser.add_argument('-analizar', dest='analizador', action='store_true', help='ejecuta el analizador y hace algo')

parser.add_argument('archivo', help='Archivo con el codigo fuente')


# - - - [ Funcionalidad ] - - -
def marciano():
	args = parser.parse_args()

	if args.explorador:
		archivo = open(args.archivo,"r")
		exp = Explorador(archivo)
		exp.explorar()
		if exp.tiene_errores():
			exp.imprimir_errores()
		else:
			exp.imprimir_componentes()

	elif args.analizador:
		print('SE ESTA EJECUTANDO EL ANALIZADOR')

# Llamada al programa
if __name__ == '__main__':
	marciano()