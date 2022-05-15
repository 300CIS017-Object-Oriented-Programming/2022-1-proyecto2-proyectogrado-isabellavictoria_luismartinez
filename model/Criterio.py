
class Criterio:
    def __init__(self, identificador, nombre_criterio, descripcion_criterio, porcentaje_ponderacion, calificacion1,
                 calificacion2, comentario, nota_criterio, observaciones_predeterminadas):
        self.identificador = identificador
        self.nombre_criterio = nombre_criterio
        self.descripcion_criterio = descripcion_criterio
        self.porcentaje_ponderacion = porcentaje_ponderacion
        self.calificacion1 = calificacion1
        self.calificacion2 = calificacion2
        self.comentario = comentario
        self.nota_criterio = nota_criterio
        self.observaciones_predeterminadas = {}
