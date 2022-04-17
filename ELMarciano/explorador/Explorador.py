from explorador import DescriptoresComponentes, TipoComponente, DescripcionComponente
from explorador.AtributosComponente import AtributosComponente
from explorador.ComponenteLéxico import ComponenteLéxico


class Explorador:
    """
    Clase que lleva el proceso principal de exploración y deja listos los
    los componentes léxicos usando para ello los descriptores de
    componente.
    """

    def __init__(self, contenido_archivo):
        self.texto = contenido_archivo
        self.componentes = []
        self.tipoErrores = [TipoComponente.ERROR]
        self.errores = []

    def explorar(self):
        ''' Esta funcion se encarga de separar el texto en lineas procesables.
        conteo de linea, para manejo de errores
        cojo el texto y le saco todas las lineas
        tengo la linea, pues la proceso.
        agrego la linea procesada a la lista de tokens(resultado).
        '''
        contador = 1
        for linea in self.texto:
            resultado = self.procesar_linea(linea ,contador)
            for componente in resultado:
                if componente.tipo in self.tipoErrores:
                    self.errores.append(componente)
            self.componentes = self.componentes + resultado
            contador += 1

    def imprimir_componentes(self):
        ''' Funcion para imprimir los componentes o resultado o lista de tokens.
        recorro la lista
        imprimo :)
        '''
        for componente in self.componentes:
            print(componente) # Esto funciona por que el print llama al
            # método __str__ de la instancia

    def tiene_errores(self):
        ''' Funcion para determinar si el explorador detectó errores
            en el archivo.
        '''
        if len(self.errores) > 0:
            return True
        return False

    def imprimir_errores(self):
        ''' Funcion para imprimir los errores que detectó el explorador
        '''
        print('Lista de Errores Explorador:')
        for error in self.errores:
            print('\n' ,'Error # ' +str(self.errores.index(error ) +1))
            print(error.atributos_adicionales.descripcion, '. En la fila: ', error.atributos_adicionales.fila, ' y la columna: ', error.atributos_adicionales.columna)
        print('Fin de lista de Errores')

    def procesar_linea(self, linea, numFila):
        ''' ---------------- PROCESAMIENTO DE DATOS ----------------
        # Esta funcion procesa la linea de texto,
        # Agarro los token y los comparo en mis Descriptores de componentes
        # Recibo el resultado del match entre token y lista
        # Si existe dentro del los descriptores de componentes
        # el error es referente a un parametro.
        '''
        componentes = []
        tamanoLinea = len(linea)
        posicionInicial = 0
        posicionFinal = 0

        # Toma una línea y le va cortando pedazos hasta que se acaba
        while(posicionFinal != tamanoLinea):
            pos = linea[posicionFinal:]
            # Separa los descriptores de componente en dos variables

            for tipo_componente, regex in DescriptoresComponentes.descriptores_componentes:

                # Trata de hacer match con el descriptor actual
                respuesta = re.match(regex, pos)
                # Si hay coincidencia se procede a generar el componente
                # léxico final
                if respuesta != None :
                    posicionFinal += respuesta.end()

                    descripcion = ""

                    # Se declara una descripcion para atributos adicionales y primero se compara con errores
                    if  tipo_componente is TipoComponente.LACTEO:
                        descripcion = ">>Error: Se fue en kk por usar  " +respuesta.group()

                    elif tipo_componente is TipoComponente.ERRORFLOTANTE :
                        descripcion = ">>Error: El flotante  " +respuesta.group( ) +" esta mal escrito"

                    elif tipo_componente is TipoComponente.ERRORVARIABLE :
                        descripcion = ">>Error: El simbolo  " +respuesta.group( ) +" no se acepta"

                    elif tipo_componente is TipoComponente.ERRORENCAPSULACION :
                        descripcion = ">>Error: No se aceptan caracteres después de simbolo  " +respuesta.group( ) +" en la misma linea"

                    elif tipo_componente is TipoComponente.ERROR:
                        if respuesta.end() == 0: posicionFinal += 1
                        descripcion = "Se detecto un error en  " +respuesta.group( ) +" CORREGIR"

                    # Si no coincide a un error y no es un blanco ni comentario, se manda a traer la descripcion de DescripcionComponente
                    elif tipo_componente is not TipoComponente.BLANCOS and \
                            tipo_componente is not TipoComponente.COMENTARIO:
                        descripcion = DescripcionComponente.evaluar_token(respuesta.group() ,tipo_componente)

                    # si la coincidencia corresponde a un BLANCO o un
                    # COMENTARIO se ignora por que no se ocupa
                    if tipo_componente is not TipoComponente.BLANCOS and \
                            tipo_componente is not TipoComponente.COMENTARIO:

                        # Crea el componente léxico y lo guarda
                        atributos_adicionales = AtributosComponente(numFila ,posicionInicial ,descripcion)
                        nuevo_componente = ComponenteLéxico(tipo_componente, respuesta.group() ,atributos_adicionales)
                        componentes.append(nuevo_componente)

                    break;

            posicionInicial = posicionFinal
        return componentes

