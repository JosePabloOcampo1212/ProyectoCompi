from explorador import TipoComponente


class DescripcionComponente:
    """
    Clase que funciona como diccionario para dar una descripcion a cada lexema

    Algunos tipos de lexema que pueden ser muy distintos entre si mismos se les da una descripcion generica, mientras que los que siempre son iguales uno especifico
    """
    def evaluar_token(mitoken, mi_componente):
        AtributosComponente = {

            '^': 'equivalente a While',
            '?': 'Si condicional',
            '?:': 'Si Tal Vez',
            ':': 'No condicional',
            '&&': 'equivalente a and',
            '||': 'equivalente a or',
            'T': 'equivalente a True',
            'F': 'equivalente a False',
            '+': 'Operador Matematico de suma + ',
            '-': 'Operador Matematico de resta - ',
            '*': 'Operador Matematico de multiplicacion * ',
            '/': 'Operador Matematico de division / ',
            '->':'Conector de un identificador y un valor',
            '==': 'Igual comparativo ',
            '!=': 'Diferente comparativo',
            '<':'Menor comparativo',
            '>':'Mayor comparativo',
            '<=':'Menor o igual comparativo',
            '>=':'Mayor o igual comparativo',
            '_': 'imprime cualquier variable o texto ',
            '++': 'Este te concatena 2 textos',
            '+--+':'Entrada por medio de consola',
            '>>': 'Retorno un valor',
            '-->': 'Inicio de funcion.',
            'fin': 'Fin de la funcion.',
        }
        """
        Revisa que el token exista en la lista, en caso de ser variables o identificadores
        retorna el mismo mensaje.
        """
        if mitoken not in AtributosComponente:
            if mi_componente is TipoComponente.IDENTIFICADOR:
                return 'Esto es un identificador'
            if mi_componente is TipoComponente.TEXTO:
                return 'Esto es un texto'
            if mi_componente is TipoComponente.ENTERO:
                return 'Esto es un numero entero'
            if mi_componente is TipoComponente.PUNTUACION:
                return 'Esto es un simbolo del sistema'
            if mi_componente is TipoComponente.FLOTANTE:
                return 'Esto es un flotante'
            return 'Identificadores o variables'
        # si el token si existe, busco y traigo el atributo.
        else:
            return AtributosComponente.get(mitoken)
