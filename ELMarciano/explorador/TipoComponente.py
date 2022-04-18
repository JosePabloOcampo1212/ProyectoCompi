from enum import Enum, auto

# Esta clase sirve de enumeracion para los componentes lexicos
class TipoComponente(Enum):
    PROGRAMA = auto()
    COMENTARIO = auto()
    ASIGNACION = auto()
    IDENTIFICADOR = auto()
    TEXTO = auto()
    ENTERO = auto()
    FLOTANTE = auto()
    EXPRESION_MATE = auto()
    LITERAL = auto()
    FUNCION = auto()
    INSTRUCCION = auto()
    REPETICION = auto()
    CONDICIONAL = auto()
    COMPARACION = auto()
    COMPARADOR = auto()
    VALOR_VERDAD = auto()
    OPERADOR_LOGICO = auto()
    O = auto()
    Y = auto()
    OPERADOR_MATEMATICO = auto()
    PALABRA_CLAVE = auto()
    BIFURCACION = auto()
    SI = auto()
    TALVEZ = auto()
    SINO = auto()
    RETORNO = auto()
    ERROR = auto()
    PUNTUACION = auto() #<{> <}> <,> <(> <)>
    AMBIENTE_ESTANDAR = auto() #Convertir / Print / Concatenar / Ingresar ::= <<
    ERROR_ENCAPSULACION = auto()
    ESPACIO = auto()
    CambioDeLinea = auto()
    ERRORVARIABLE =auto()
    ERRORFLOTANTE = auto()