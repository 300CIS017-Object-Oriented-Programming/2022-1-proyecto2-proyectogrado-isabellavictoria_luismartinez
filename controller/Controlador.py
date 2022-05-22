import streamlit as st

from model.Criterio import Criterio
from model.Detalle_Criterio import DetalleCriterio


class Controlador:
    def __init__(self) -> None:
        super().__init__()
        # Diccionario donde se guardan las actas creadas por el asistente
        self.actas = {}
        # Tamaño actual del diccionario de actas
        self.current_length_actas = 0
        # Diccionario en donde se guardan los criterios actuales para la calificación de las actas
        self.criterios = {1: Criterio("1", "Desarrollo y profundidad en el tratamiento del tema",
                                      "", 0.20),
                          2: Criterio("2", "Desafío académico y científico del tema",
                                      "", 0.15),
                          3: Criterio("3", "Cumplimiento de los objetivos propuestos",
                                      "", 0.10),
                          4: Criterio("4", "Creatividad e innovación de las soluciones y desarrollos propuestos:",
                                      "", 0.10),
                          5: Criterio("5", "Validez de los resultados y conclusiones",
                                      "", 0.10),
                          6: Criterio("6", "Manejo y procesamiento de la información y bibliografía",
                                      "", 0.10),
                          7: Criterio("7", "Calidad y presentación del documento escrito",
                                      "", 0.075),
                          8: Criterio("8", "Presentación oral", "", 0.075)}
        # Cantidad de criterio utilizados en el momento
        self.current_length_criterios = 8
        # Diccionario con las opciones de comentarios predeterminados para cada criterio
        self.predeterminados_criterio = {1: ["Se desarrolló apropiadamente el tema y con la profundidad suficiente para su culminación.",
                                               "Se desarolla adecuadamente el tema sin embargo se puede mejorar en profundidad y detalle.",
                                               "Se necesita mejorar el desarrollo del tema y la profundidad con la que se trata."],
                                         2: ["El trabajo estuvo bien soportado y con rigor científico.",
                                              "El trabajo tiene un soporte y rigor científico promedio.",
                                              "El trabajo no alcanza el nivel suficiente de rigurosidad científica y carece de soporte para los argumentos presentados."],
                                         3: ["Cumplió con todos los objetivos.",
                                              "Cumple con todos los objetivos exceptuando 1 o 2.",
                                              "No cumple con los objetivos propuestos."],
                                         4: ["El trabajo resuelve creativamente a la tesis planteada por medio de diferentes recursos.",
                                              "El trabajo resuelve la tesis planteada con recursos prácticos antes explorados.",
                                              "El trabajo no hace uso o referencia a ninguna solución o idea creativa para desarollar la tesis."],
                                         5: ["Las conclusiones y resultados fueron adecuadas y consistentes con los hallazgos y el desarrollo del trabajo.",
                                              "La mayoría de las conclusiones y resultados son válidos; se puede mejorar en 1 o 2 de ellos.",
                                              "Las conclusiones y resultados no son coherente con el planteamiento y el desarrollo presentado en el trabajo"],
                                         6: ["La información y la bibliografía utilizada corresponde a fuentes confiables y se encuentra adecuadamente citada",
                                              "La información y bibliografía presenta fallas en la citación o validez en 1 de las fuentes",
                                              "La informacióny bibliografía presenta 2 o más citas con una errónea citación o que no cuentan con validación científica"],
                                         7: ["El documento se encuentra adecuadamente presentado, cuenta con buena ortografía, coherencia y cohesión.",
                                              "El documento tiene algunos errores de digitación y algunos apartados necesitan revisión.",
                                              "El documento presenta múltiples errores ortográficos, necesita de revisión en apartados y corregir aspectos de la presentación"],
                                         8: ["La presentación oral es concisa, consistente y expone todos los aspectos relevantes del trabajo",
                                              "La presentación oral es muy extansa y podría abarcar menos aspectos del trabajo",
                                              "La presentación oral es muy breve y no expone los aspectos minímos del trabajo"]}

    # funcion utilizada por la view del jurado para dar la calificación de cada criterio con su respectivo ponderado
    def calcular_nota_criterio(self, calificacion1, calificacion2, identificador_criterio):
        ponderado = self.criterios[int(identificador_criterio)].porcentaje_ponderacion
        nota_criterio = ((float(calificacion1) + float(calificacion2)) / 2) * ponderado

        return nota_criterio

    # funcion utilizada por el view del jurado para sumar
    # la calificación de cada criterio y retornar la nota final del trabajo de grado
    def calcular_nota_trabajo(self, identificador_acta):
        nota_trabajo = 0.0
        for i in range(1, len(self.criterios)):
            nota_trabajo += self.actas[identificador_acta].detalles_criterio[str(i)].nota_criterio
        return nota_trabajo

    # procedimiento utilizado por el view del jurado para recolectar la calificacion y los comentarios de cada criterio.
    # Crea un objeto de clase DetalleCriterio que es luego guardado en la respectiva acta.
    def recolectar_datos_detalle_criterio(self, identificador_criterio, identificador_acta):

        calificacion1 = st.number_input("Calificacion 1_" + str(identificador_criterio), 0, 5)
        calificacion2 = st.number_input("Calificacion 2_" + str(identificador_criterio), 0, 5)
        choice1 = st.radio("¿Desea utilizar un comentario predeterminado para criterio " + str(identificador_criterio) +
                           "?", ["Si", "No"])
        if choice1 == "Si":
            predeterminado = st.selectbox("Elija la opcion predeterminada para criterio " + str(identificador_criterio),
                                          [self.predeterminados_criterio[int(identificador_criterio)][0],
                                           self.predeterminados_criterio[int(identificador_criterio)][1],
                                           self.predeterminados_criterio[int(identificador_criterio)][2]])
            if st.button("Calificar criterio " + str(identificador_criterio)):
                detalle = DetalleCriterio(identificador_criterio, float(calificacion1), float(calificacion2),
                                          predeterminado, 0.0)
                self.actas[identificador_acta].detalles_criterio[identificador_criterio] = detalle
                detalle.nota_criterio = self.calcular_nota_criterio(calificacion1, calificacion2,
                                                                          identificador_criterio)
        else:
            comentario = st.text_area("Comentarios de los jurados para criterio" + str(identificador_criterio))
            if st.button("Calificar criterio " + str(identificador_criterio)):
                detalle = DetalleCriterio(identificador_criterio, float(calificacion1), float(calificacion2),
                                          comentario, 0.0)
                self.actas[identificador_acta].detalles_criterio[identificador_criterio] = detalle
                detalle.nota_criterio = self.calcular_nota_criterio(calificacion1, calificacion2,
                                                                          identificador_criterio)

    # procedimiento utilizado por view del Director para ver los detalles de cada criterio
    def mostrar_criterio(self, identificador_criterio):

        with st.expander("Criterio " + str(identificador_criterio)):
            st.subheader("Nombre del criterio")
            st.write(self.criterios[identificador_criterio].nombre_criterio)

            st.subheader("Descripcion del criterio")
            st.write(self.criterios[identificador_criterio].descripcion_criterio)

            st.subheader("Ponderado del criterio")
            st.write(str(self.criterios[identificador_criterio].porcentaje_ponderacion * 100) + "%")

    # procedimiento utilizado por el view del jurado para recolectar los nuevos datos del criterio que se desea modificar
    def recolectar_datos_criterio(self, identificador_criterio):

        with st.expander("Recolección de datos del Criterio"):
            opcion_nombre = st.radio("¿Desea cambiar el nombre del criterio?", ["Si", "No"])
            if opcion_nombre == "Si":
                nuevo_nombre = st.text_input("Nuevo nombre del criterio:")
                if st.button("Cambiar nombre criterio" + str(identificador_criterio)):
                    self.criterios[identificador_criterio].nombre_criterio = nuevo_nombre

            opcion_descripcion = st.radio("¿Desea cambiar la descripción del criterio?", ["Si", "No"])
            if opcion_descripcion == "Si":
                nueva_descripcion = st.text_area("Nueva descripción del criterio:")
                if st.button("Cambiar descripcion criterio" + str(identificador_criterio)):
                    self.criterios[identificador_criterio].descripcion_criterio = nueva_descripcion

            opcion_ponderado = st.radio("¿Desea cambiar el ponderado del criterio?", ["Si", "No"])
            if opcion_ponderado == "Si":
                nuevo_ponderado = st.number_input("Nuevo porcentaje de ponderación del criterio:", 5, 100)
                nuevo_ponderado /= 100
                if st.button("Cambiar porcentaje de ponderacion del criterio" + str(identificador_criterio)):
                    self.criterios[identificador_criterio].porcentaje_ponderacion = float(nuevo_ponderado)
