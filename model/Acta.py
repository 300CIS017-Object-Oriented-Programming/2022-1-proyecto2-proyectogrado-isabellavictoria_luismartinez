
class Acta:
    def __init__(self, numero_acta, fecha, id_estudiante, nombre_estudiante,
                       periodo, titulo_trabajo,enfasis, tipo_trabajo, nombre_director,
                       nombre_codirector, nombre_jurado1, nombre_jurado2,
                       criterios, detalles_criterio, comentarios_adicionales,
                       nota_trabajo, estado):
        self.numero_acta = numero_acta
        self.fecha = fecha
        self.id_estudiante = id_estudiante
        self.nombre_estudiante = nombre_estudiante
        self.periodo = periodo
        self.titulo_trabajo = titulo_trabajo
        self.enfasis = enfasis
        self.tipo_trabajo = tipo_trabajo
        self.nombre_director = nombre_director
        self.nombre_codirector = nombre_codirector
        self.nombre_jurado1 = nombre_jurado1
        self.nombre_jurado2 = nombre_jurado2
        self.criterios = criterios
        self.detalles_criterio = detalles_criterio
        self.comentarios_adicionales = comentarios_adicionales
        self.nota_trabajo = nota_trabajo
        self.estado = estado

