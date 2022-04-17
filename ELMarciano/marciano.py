#Compilador para El Marciano

# - - - [ Imports ] - - -
from utils import archivos as utils
from explorador.Explorador import Explorador
import argparse


# - - - [ Parser ] - - -
parser = argparse.ArgumentParser(descrtiption= 'Compilador Marciano')

parser.add_argument('-explorar', dest='explorador', action='store_true', help='ejecuta el explorador y retorna los componentes lexicos')

parser.add_argument('archivo', help='Archivo con el codigo fuente')


# - - - [ Funcionalidad ] - - -
def marciano():
	args = parser.parse_args()

	if args.explorador:
		texto = utils.cargar_archivo(args.archivo)
		exp = Explorador(texto)
		exp.explorar()

		if exp.tiene_errores():
			exp.imprimir_errores()
		else:
			exp.imprimir_componentes()