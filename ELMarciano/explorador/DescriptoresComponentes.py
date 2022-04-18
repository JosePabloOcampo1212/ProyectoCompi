from explorador.TipoComponente import TipoComponente


class DescriptoresComponentes:
    # contiene una lista de tuplas de CATEGORIA - Regex.
    descriptores_componentes = [
        (TipoComponente.COMENTARIO, r'^//.*'),
        (TipoComponente.PUNTUACION, r'^([(),])'),
        (TipoComponente.PALABRA_CLAVE, r'^(->|-->|{|}|>>)'),
        (TipoComponente.CONDICIONAL, r'^(\?|\?:|:)'),
        (TipoComponente.REPETICION, r'^(\^)'),
        (TipoComponente.OPERADOR_MATEMATICO, r'^(\+|-|\*|/)'),
        (TipoComponente.COMPARADOR, r'^(=|!=|<|>|<=|>=)'),
        (TipoComponente.AMBIENTE_ESTANDAR, r'^(_|\+\+)'),
        (TipoComponente.VALOR_VERDAD, r'^(T|F)'),
        (TipoComponente.IDENTIFICADOR, r'^([a-z]([a-zA-Z0-9])*)'),
        (TipoComponente.FLOTANTE, r'^(-)?\d\.\d'),
        (TipoComponente.ENTERO, r'^(-)?\d+'),
        (TipoComponente.ERROR_ENCAPSULACION, r'^((})[a-zA-Z- _/])'),
        (TipoComponente.ERRORVARIABLE, r'^([:{}~!@%&|;?"]+)'),
        (TipoComponente.ERRORFLOTANTE, r'^(\.[0-9])'),
        (TipoComponente.ASIGNACION, r'^(>)'),
        (TipoComponente.FUNCION, r'^(->)'),
        (TipoComponente.ESPACIO, r'^(\s)+'),
        (TipoComponente.TEXTO, r'^(.)*'),
        (TipoComponente.ERROR, r'^(\s)*')
    ]
