#Compilador para El Marciano

# - - - [ Imports ] - - -
import argparse

parser = argparse.ArgumentParser(descrtiption= 'Compilador Marciano')

parser.add_argument('-explorar', dest='explorador', action='store_true', help='ejecuta el explorador y retorna los componentes lexicos')

def marciano():
	args = parser.parse_args()

	if args.explorador:
		