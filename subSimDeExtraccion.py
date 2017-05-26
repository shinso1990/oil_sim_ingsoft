class SubSimDeExtraccion:
	def __init__(self,log,parcelas,politicaDeExtraccion):
		self.parcelas = parcelas
		self.log=log
		self.politicaDeExtraccion=politicaDeExtraccion
		
	def simularExtraccion(self,dia,plantasProcesdoras,tanques):
		#	obtenemos las parcelas que tienen el pozo terminado
		parcelasListasParaExtraer = list(filter(lambda rig: rig.parcela().listoParaExtraer()),self.parcelas))
		#	Elegimos las parcelas a ser utilizadas en base a la politica
		parcelasElegidas = politicaDeExtraccion.elegir(parcelasListasParaExtraer)
		#	abrimos la valvula y procesamos la materia prima	
		ListaEventosDeAperturaDeValvulas =  list(map(lambda parcela: parcela.pozo.abrirValvula(plantaProcesadoras),parcerlasElegidas))
		ListaDeEventosDeAlmacenamento = planteaProcesdora.liberar(tanques)
		return ListaEventosDeAperturaDeValvulas + ListaDeEventosDeAlmacenamento