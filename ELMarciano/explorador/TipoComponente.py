from enum import Enum, auto

class TipoComponente(Enum):
    """
    Enum con los tipos de componentes disponibles

    Esta clase tiene mayormente un propósito de validación
    """

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
    
"""
    COMENTARIO = auto()
    PALABRA_CLAVE = auto()
    CONDICIONAL = auto()
    REPETICION = auto()
    ASIGNACION = auto()
    OPERADOR = auto()
    COMPARADOR = auto()
    TEXTO = auto()
    IDENTIFICADOR = auto()
    ENTERO = auto()
    FLOTANTE = auto()
    VALOR_VERDAD = auto()
    PUNTUACION = auto()
    BIFURCACION = auto()
    AMBIENTEESTANDAR = auto()
    BLANCOS = auto()
    ERRORENCAPSULACION = auto()
    ERRORFLOTANTE = auto()
    ERRORVARIABLE = auto()
    ERROR = auto()
    """