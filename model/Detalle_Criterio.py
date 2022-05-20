
class DetalleCriterio:
    def __init__(self, identificador_criterio, calificacion1, calificacion2, comentario, nota_criterio):
        self.identificador_criterio = identificador_criterio
        self.calificacion1 = calificacion1
        self.calificacion2 = calificacion2
        self.comentario = comentario
        self.nota_criterio = nota_criterio

    def calcular_nota_criterio(self, calificacion1, calificacion2, identificador_criterio, controller):
        self.nota_criterio = (calificacion1 + calificacion2) * \
                             controller.criterios[identificador_criterio].porcentaje_ponderacion
