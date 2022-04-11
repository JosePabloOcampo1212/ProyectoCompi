from explorador import TipoComponente


class DescriptoresComponentes:
    # contiene una lista de tuplas de CATEGORIA - Regex.
    descriptores_componentes = [
        (TipoComponente.COMENTARIO, r'^Nota:.*'),
        (TipoComponente.PUNTUACION, r'^([#(),])'),
        (TipoComponente.PALABRA_CLAVE, r'^(inicio_Receta|inicio|fin|caracoles|monchar|ponga|llamese)'),
        (TipoComponente.CONDICIONAL, r'^(si_pasa|tal_vez)'),
        (TipoComponente.REPETICION, r'^(sea_necio)'),
        (TipoComponente.OPERADOR, r'^(\+|-|\*|/|agregue|intente_esta)'),
        (TipoComponente.COMPARADOR, r'^(igual|diferente|menor|mayor|menor_igual|mayor_igual)'),
        (TipoComponente.AMBIENTEESTANDAR, r'^(Muestre|Ingrese|Mezclar_ingredientes|Mimir)'),
        (TipoComponente.VALOR_VERDAD, r'^(al_chile|no_invente)'),
        (TipoComponente.LACTEO, r'^((L|l)eche|(Q|q)ueso|(N|n)atilla|(Y|y)ogurt|(H|h)elado|(M|m)antequilla|(C|c)uajada|(N|n)ata)'),
        (TipoComponente.IDENTIFICADOR, r'^([a-zA-Z]([a-zA-Z0-9\_])*)'),
        (TipoComponente.FLOTANTE, r'^(-?[0-9]+\.[0-9]+)'),
        (TipoComponente.ENTERO, r'^(-?[0-9]+)'),
        (TipoComponente.ERRORENCAPSULACION, r'^((fin|#)[a-zA-Z- _/])'),
        (TipoComponente.ERRORVARIABLE, r'^([:{}~!@%&|;?"]+)'),
        (TipoComponente.ERRORFLOTANTE, r'^(\.[0-9])'),
        (TipoComponente.ASIGNACION, r'^(=)'),
        (TipoComponente.TEXTO, r'^(\$.?[^$]*)\$'),
        (TipoComponente.BLANCOS, r'^(\s)+'),
        (TipoComponente.ERROR, r'^(\s)*')
    ]
