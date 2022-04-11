from enum import Enum, auto

class TipoComponente(Enum):
    """
    Enum con los tipos de componentes disponibles

    Esta clase tiene mayormente un propósito de validación
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
