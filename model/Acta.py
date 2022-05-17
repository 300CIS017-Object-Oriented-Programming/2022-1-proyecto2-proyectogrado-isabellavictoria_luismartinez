
class Acta:
    def __init__(self, numero_acta, fecha, id_estudiante, nombre_estudiante, periodo,titulo_trabajo, tipo_trabajo,
                 nombre_director, nombre_codirector, nombre_jurado1, nombre_jurado2, criterios, comentarios_adicionales,
                 nota_trabajo, estado):
        self._numero_acta = numero_acta
        self._fecha = fecha
        self._id_estudiante = id_estudiante
        self._nombre_estudiante = nombre_estudiante
        self._periodo = periodo
        self._titulo_trabajo = titulo_trabajo
        self._tipo_trabajo = tipo_trabajo
        self._nombre_director = nombre_director
        self._nombre_codirector = nombre_codirector
        self._nombre_jurado1 = nombre_jurado1
        self._nombre_jurado2 = nombre_jurado2
        self._criterios = {}
        self._comentarios_adicionales = comentarios_adicionales
        self._nota_trabajo = nota_trabajo
        self._estado = estado
