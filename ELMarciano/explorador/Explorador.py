# - - - [ IMPORT ] - - -

import re
from explorador.DescriptoresComponentes import DescriptoresComponentes
from explorador.TipoComponente import TipoComponente
from explorador.DescripcionComponente import DescripcionComponente
from explorador.AtributosComponente import AtributosComponente
from explorador.ComponenteLéxico import ComponenteLéxico


# - - - [ INICIO ] - - -

class Explorador:
    """
    Clase que se encarga de la exploracion y devuelce la descripcion
    de los tokens 
    """

    def __init__(self, contenido_archivo):
        self.texto = contenido_archivo
        self.componentes = []
        self.tipoErrores = [TipoComponente.ERROR_ENCAPSULACION, TipoComponente.ERROR]
        self.errores = []

    def explorar(self):
        """
        Esta funcion se encarga de separar el texto en lineas procesables.
        Lleva un conteo de linea para el manejo de errores
        una vez procesada cada linea,
        agrego la linea a la lista de tokens(resultado).
        """
        
        contador = 1
        for linea in self.texto:
            resultado = self.procesar_linea(linea ,contador)
            for componente in resultado:
                if componente.tipo in self.tipoErrores:
                    self.errores.append(componente)
            self.componentes = self.componentes + resultado
            contador += 1

    def imprimir_componentes(self):
        for componente in self.componentes:
            print(componente) # Esto funciona por que el print llama al
            # método __str__ de la instancia

    def componentes_get(self):
        return self.componentes

    def tiene_errores(self):
        if len(self.errores) > 0:
            return True
        return False

    def imprimir_errores(self):
        print('Lista de Errores Explorador:')
        for error in self.errores:
            print('\n' ,'Error # ' +str(self.errores.index(error ) +1))
            print(error.atributos_adicionales.descripcion, '. En la fila: ', error.atributos_adicionales.fila, ' y la columna: ', error.atributos_adicionales.columna)
        print('Fin de lista de Errores')

    def procesar_linea(self, linea, numFila):
        ''' ---------------- PROCESAMIENTO DE DATOS ----------------
        # Esta funcion procesa la linea de texto,
        # Se trabajan con los token y se comparan en mis Descriptores de componentes
        # Recibo el resultado del match entre el token y la lista de componentes
        # Revisa si existe dentro del los descriptores de componentes
        # En caso de error, es referente a un parametro.
        '''
        componentes = []
        tamanoLinea = len(linea) - 1
        posicionInicial = 0
        posicionFinal = 0

        # Toma una línea y la va separando en secciones hasta que se acaba
        while(posicionFinal != tamanoLinea):
            pos = linea[posicionFinal:]
            # Separa los descriptores de componente en dos variables

            for tipo_componente, regex in DescriptoresComponentes.descriptores_componentes:

                # Trata de hacer match con el descriptor actual
                respuesta = re.match(regex, pos)

                # Si hay coincidencia se procede a generar el componente léxico final
                if respuesta is not None :
                    posicionFinal += respuesta.end()
                    descripcion = ""

                    # Se declara una descripcion para atributos adicionales y primero se compara con errores
                    if tipo_componente is TipoComponente.ERROR_ENCAPSULACION:
                        descripcion = "ERROR! Se ha generado un error de encapsulacion despues del simbolo " + respuesta.group() + "; favor revisar"

                    elif tipo_componente is TipoComponente.ERROR:
                        if respuesta.end() == 0: posicionFinal += 1
                        descripcion = "Se detecto un error en  " +respuesta.group( ) +" CORREGIR"

                    # Si no coincide a un error y no es un espacio ni comentario, se manda a traer la descripcion de DescripcionComponente
                    elif tipo_componente is not TipoComponente.ESPACIO and \
                            tipo_componente is not TipoComponente.COMENTARIO:
                        descripcion = DescripcionComponente.evaluar_token(respuesta.group() ,tipo_componente)

                    # si la coincidencia corresponde a un ESPACIO o un COMENTARIO se ignora
                    if tipo_componente is not TipoComponente.ESPACIO and \
                            tipo_componente is not TipoComponente.COMENTARIO:

                        # Crea el componente léxico y lo guarda
                        atributos_adicionales = AtributosComponente(numFila ,posicionInicial ,descripcion)
                        nuevo_componente = ComponenteLéxico(tipo_componente, respuesta.group() ,atributos_adicionales)
                        componentes.append(nuevo_componente)

                    break

            posicionInicial = posicionFinal
        return componentes

