from explorador import TipoComponente, AtributosComponente


class ComponenteLéxico:
    """
    Clase que almacena la información de un componente léxico

    Posee el tipo de lexema, el lexema propiamente y sus atributos adicionales
    """

    tipo    : TipoComponente
    texto   : str
    atributos_adicionales: AtributosComponente

    def __init__(self, tipo_nuevo: TipoComponente, texto_nuevo: str, _atributos_adicionales: AtributosComponente):
        """
        Declaracion de atributos correspondientes a los atributos del componente
        """
        self.tipo = tipo_nuevo
        self.texto = texto_nuevo
        self.atributos_adicionales = _atributos_adicionales

    def __str__(self):
        """
        Da una representación en texto de la instancia actual usando un
        string de formato de python (ver 'python string formatting' en
        google)
        """

        resultado = f'{self.tipo:30} <{self.texto:20}> ({self.atributos_adicionales})'
        return resultado