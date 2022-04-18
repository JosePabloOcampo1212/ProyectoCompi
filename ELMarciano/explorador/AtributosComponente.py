class AtributosComponente:
    
    # Clase que guarda los atributos como fila, columna y descripción
    
    fila: int
    columna: int
    descripcion: str

    def __init__(self, _fila: int, _columna: int, _descripcion: str):
        # Se declaran los atributos
        
        self.fila = _fila
        self.columna = _columna
        self.descripcion = _descripcion

    def __str__(self):
        # Da una representación en texto de la instancia actual por medio de un string

        resultado = f'Fila:{self.fila} ; Columna:{self.columna} ; Descripcion: <{self.descripcion}>'
        return resultado