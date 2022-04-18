from explorador import TipoComponente, AtributosComponente


class ComponenteLéxico:
    """
    Esta clase guarda la información de un componente léxico

    La cual posee el tipo de lexema, el propio lexema y sus atributos adicionales

    Los cuales son Fila, Columna y Descripcion
    """

    tipo    : TipoComponente
    texto   : str
    atributos_adicionales: AtributosComponente

    def __init__(self, tipo_nuevo: TipoComponente, texto_nuevo: str, _atributos_adicionales: AtributosComponente):
        # Se declaran los atributos de la clase
        self.tipo = tipo_nuevo
        self.texto = texto_nuevo
        self.atributos_adicionales = _atributos_adicionales

    def __str__(self):
        # Da una representación en texto de la instancia actual por medio de un string

        resultado = f'{self.tipo:30} <{self.texto:20}> ({self.atributos_adicionales})'
        return resultado