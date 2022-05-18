
from model.Acta import Acta
from model.Criterio import Criterio

class Controlador:
    def __init__(self) -> None:
        self.actas = {}
        self.criterios = {1: Criterio(1, "Desarrollo y profundidad en el tratamiento del tema", "", 0.20), 2: Criterio(2,"Desafío académico y científico del tema", "", 0,15),
                          3: Criterio(3, "Cumplimiento de los objetivos propuestos", "", 0.10 ), 4: Criterio(4, "Creatividad e innovación de las soluciones y desarrollos propuestos:","",0.10),
                          5: Criterio(5,"Validez de los resultados y conclusiones", "", 0.10), 6: Criterio(6,"Manejo y procesamiento de la información y bibliografía", "", 0.10),
                          7: Criterio(7,"Calidad y presentación del documento escrito", "", 0.075), 8: Criterio(8, "Presentación oral", "", 0.075)}

    def crear_acta(self, numero_acta, fecha, id_estudiante, nombre_estudiante, periodo,titulo_trabajo, tipo_trabajo,
                   nombre_director, nombre_codirector, nombre_jurado1, nombre_jurado2):

        acta_modelo = Acta()
        acta_modelo.numero_acta = numero_acta
        acta_modelo. fecha = fecha
        acta_modelo.id_estudiante = id_estudiante
        acta_modelo.nombre_estudiante = nombre_estudiante
        acta_modelo.periodo = periodo
        acta_modelo.titulo_trabajo = titulo_trabajo
        acta_modelo.tipo_trabajo = tipo_trabajo
        acta_modelo.nombre_director = nombre_director
        acta_modelo.nombre_codirector = nombre_codirector
        acta_modelo.nombre_jurado1 = nombre_jurado1
        acta_modelo.nombre_jurado2 = nombre_jurado2
        acta_modelo.criterios = self.criterios
        acta_modelo.detalles_criterio = {}








    def criterios_predeterminados(self):
        criterio1 = Criterio(1,"Desarrollo y profundidad en el tratamiento del tema"," ", 0.20,)
        criterio2 = Criterio(2,"Desafío académico y científico del tema ", " ", 0.20,)
        criterio3 = Criterio(3,"Cumplimiento de los objetivos propuestos", " ", 0.15, )
        criterio4 = Criterio(4,"Creatividad e innovación de las soluciones y desarrollos propuestos", " ", 0.10,)
        criterio5 = Criterio(5,"Validez de los resultados y conclusiones", " ", 0.20,)
        criterio6 = Criterio(6,"Manejo y procesamiento de la información y bibliografía", " ", 0.10,)
        criterio7 = Criterio(7,"Calidad y presentación del documento escrito", " ", 0.075,)
        criterio8 = Criterio(8,"Presentación oral", " ", 0.075,)








