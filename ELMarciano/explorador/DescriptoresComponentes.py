from explorador import TipoComponente


class DescriptoresComponentes:
    # contiene una lista de tuplas de CATEGORIA - Regex.
    descriptores_componentes = [
        (TipoComponente.COMENTARIO, r'^//.*'),
        (TipoComponente.PUNTUACION, r'^([#(),])'),
        (TipoComponente.PALABRA_CLAVE, r'^(inicio_Receta|inicio|fin|caracoles|monchar|ponga|llamese)'),
        (TipoComponente.CONDICIONAL, r'^(\?|:)'),
        (TipoComponente.REPETICION, r'^(sea_necio)'),
        (TipoComponente.OPERADOR, r'^(\+|-|\*|/|agregue|intente_esta)'),
        (TipoComponente.COMPARADOR, r'^(=|!=|<|>|<=|>=)'),
        (TipoComponente.AMBIENTEESTANDAR, r'^(_|Ingrese|Mezclar_ingredientes|Mimir)'),
        (TipoComponente.VALOR_VERDAD, r'^(al_chile|no_invente)'),
        (TipoComponente.LACTEO, r'^((L|l)eche|(Q|q)ueso|(N|n)atilla|(Y|y)ogurt|(H|h)elado|(M|m)antequilla|(C|c)uajada|(N|n)ata)'),
        (TipoComponente.IDENTIFICADOR, r'^([a-zA-Z]([a-zA-Z0-9\_])*)'),
        (TipoComponente.FLOTANTE, r'^(-?[0-9]+\.[0-9]+)'),
        (TipoComponente.ENTERO, r'^(-?[0-9]+)'),
        (TipoComponente.ERRORENCAPSULACION, r'^((})[a-zA-Z- _/])'),
        (TipoComponente.ERRORVARIABLE, r'^([:{}~!@%&|;?"]+)'),
        (TipoComponente.ERRORFLOTANTE, r'^(\.[0-9])'),
        (TipoComponente.ASIGNACION, r'^(>)'),
        (TipoComponente.TEXTO, r'^(\$.?[^$]*)\$'),
        (TipoComponente.BLANCOS, r'^(\s)+'),
        (TipoComponente.ERROR, r'^(\s)*')
    ]
