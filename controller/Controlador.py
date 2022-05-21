import streamlit as st

from model.Criterio import Criterio


class Controlador:
    def __init__(self) -> None:
        super().__init__()
        self.actas = {}
        self.current_length_actas = 0
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
        self.current_length_criterios = 8
        self.memoria_criterio = {}

    def calcular_nota_criterio(self, calificacion1, calificacion2, identificador_criterio):
        ponderado = self.criterios[int(identificador_criterio)].porcentaje_ponderacion
        nota_criterio = ((float(calificacion1) + float(calificacion2)) / 2) * ponderado

        return nota_criterio

    def calcular_nota_trabajo(self, identificador_acta):
        nota_trabajo = 0.0
        for i in range(1, len(self.criterios)):
            nota_trabajo += self.actas[identificador_acta].detalles_criterio[str(i)].nota_criterio
        return nota_trabajo


    def mostrar_criterio(self, identificador_criterio):

        with st.expander("Detalles del Criterio"):
            st.subheader("Nombre del criterio")
            st.write(self.criterios[identificador_criterio].nombre_criterio)

            st.subheader("Descripcion del criterio")
            st.write(self.criterios[identificador_criterio].descripcion_criterio)

            st.subheader("Ponderado del criterio")
            st.write(str(self.criterios[identificador_criterio].porcentaje_ponderacion * 100) + "%")

    def recolectar_datos_criterio(self, identificador_criterio):

        with st.expander("Recolección de daros del Criterio"):
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
