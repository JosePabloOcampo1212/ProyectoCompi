from explorador.TipoComponente import TipoComponente

class Analizador:
	def __init__(self, _lista_componentes):
		self.lista_componentes = _lista_componentes
		self.cantidad = len(self.lista_componentes)
		self.pos_actual = 0
		self.componente_actual = self.lista_componentes[0]

	
	def __verificar(self, texto_esperado):

		if self.componente_actual.texto != texto_esperado:
			# AQUI DEBE TIRAR UN ERROR! #

		else:
			self.__avanzar_componente()

	def __verificar_tipo(self, tipo_esperado):
		"""
		Compara el componente acutal con el esperado
		"""
		if self.componente_actual is not tipo_esperado:
			# AQUI DEBE TIRAR UN ERROR!

		else:
			self.__avanzar_componente()


	def __avanzar_componente(self):

		self.pos_actual += 1
		if self.pos_actual < self.cantidad:
			self.componente_actual = self.lista_componentes[self.pos_actual]
			return
		return


	def __siguiente_componente(self, sig=1):
		"""
		Retorna el componente siguiente al componente actual
		Sin adelantar la posicion del componente actual
		"""
		return self.lista_componentes[self.pos_actual+sig]