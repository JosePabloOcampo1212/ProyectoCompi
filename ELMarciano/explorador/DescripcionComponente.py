from explorador.TipoComponente import TipoComponente


class DescripcionComponente:
    # Clase que funciona como diccionario para dar una descripcion a cada lexema

    def evaluar_token(mitoken, componente):
        AtributosComponente = {

            '^': 'equivalente a While',
            '?': 'Si condicional',
            '?:': 'Si Tal Vez',
            ':': 'else condicional',
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
            '<<':'Entrada por medio de consola',
            '>>': 'Retorno un valor',
            '-->': 'Declara funcion.',
            '{': 'Inicio de bloque.',
            '}': 'Fin de la bloque.',
        }
        """
        Revisa que el token con el lexema exista dentro del diccionario establecido

        Si no esta dentro del diccionario, se le da una descripcion adicional y especifica
        para cada caso de lexema del que se trate

        En caso de ser un identificador o variable devuelve un mensaje que lo aclara
        """
        
        if mitoken not in AtributosComponente:
            if componente is TipoComponente.IDENTIFICADOR:
                return 'Esto es un identificador'
            if componente is TipoComponente.TEXTO:
                return 'Esto es un texto'
            if componente is TipoComponente.ENTERO:
                return 'Esto es un numero entero'
            if componente is TipoComponente.PUNTUACION:
                return 'Esto es un simbolo del sistema'
            if componente is TipoComponente.FLOTANTE:
                return 'Esto es un flotante'
            return 'Identificadores o variables'

        # Si el token existe dentro del diccionario con los lexemas,
        # se retorna el atributo.
        
        else:
            return AtributosComponente.get(mitoken)
