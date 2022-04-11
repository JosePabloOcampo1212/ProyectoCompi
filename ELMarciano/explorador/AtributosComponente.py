class AtributosComponente:
    """
    Clase que almacena la información de los atributos adicionales de un componente léxico

    Tiene atributos como fila, columna y descripción (el cual guarda una descripcion del atributo o posible error)
    """
    fila: int
    columna: int
    descripcion: str

    def __init__(self, _fila: int, _columna: int, _descripcion: str):
        """
        Declaracion de atributos correspondientes a los atributos del componente
        """
        self.fila = _fila
        self.columna = _columna
        self.descripcion = _descripcion

    def __str__(self):
        """
        Da una representación en texto de la instancia actual usando un
        string de formato de python (ver 'python string formatting' en
        google)
        """
        resultado = f'Fila:{self.fila} ; Columna:{self.columna} ; Descripcion: <{self.descripcion}>'
        return resultado