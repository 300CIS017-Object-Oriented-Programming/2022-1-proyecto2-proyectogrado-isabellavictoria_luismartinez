
from model.Detalle_Criterio import *

def jurado_partial(st, controller):

    st.title("Portal de calificacion de actas")

    nombre_jurado1 = st.text_input("Nombre del Jurado 1")
    nombre_jurado2 = st.text_input("Nombre del Jurado 2")
    identificador_acta = st.text_input("Ingrese el identificador del acta por calificar")
    if st.button("Buscar acta") and identificador_acta not in controller.actas:
        st.error("El identificador del acta no corresponde a ningún documento guardado en los registros")
    else:
        criterio = st.selectbox("Elija criterio por calificar", ["Desarrollo y profundidad en el tratamiento del tema",
                                                                 "Desafío académico y científico del tema",
                                                                 "Cumplimiento de los objetivos propuestos",
                                                                 "Creatividad e innovación de las soluciones y "
                                                                 "desarrollos propuestos",
                                                                 "Validez de los resultados y conclusiones",
                                                                 "Manejo y procesamiento de la información y bibliografía",
                                                                 "Calidad y presentación del documento escrito",
                                                                 "Presentación oral"])

        if criterio == "Desarrollo y profundidad en el tratamiento del tema":

            identificador_criterio = "1"
            calificacion1 = st.text_input("Calificacion 1")
            calificacion2 = st.text_input("Calificacion 2")
            choice1 = st.radio("¿Desea utilizar un comentario predeterminado?", ["Si", "No"])
            if choice1 == "Si":
                predeterminado = st.selectbox("Elija la opcion predeterminada", [""])
                detalle = DetalleCriterio(identificador_criterio, calificacion1, calificacion2, predeterminado,
                                          controller.calcular_nota_calificacion(calificacion1, calificacion2))
                controller.actas[identificador_acta].detalles_criterio[identificador_criterio] = detalle
            else:
                comentario = st.text_input("Comentarios de los jurados")
                detalle = DetalleCriterio(identificador_criterio, calificacion1, calificacion2, comentario,
                                          controller.calcular_nota_calificacion(calificacion1, calificacion2))
                controller.actas[identificador_acta].detalles_criterio[identificador_criterio] = detalle

        elif criterio == "Desafío académico y científico del tema":

            identificador_criterio = "2"
            calificacion1 = st.text_input("Calificacion 1")
            calificacion2 = st.text_input("Calificacion 2")
            choice1 = st.radio("¿Desea utilizar un comentario predeterminado?", ["Si", "No"])
            if choice1 == "Si":
                predeterminado = st.selectbox("Elija la opcion predeterminada", [""])
                detalle = DetalleCriterio(identificador_criterio, calificacion1, calificacion2, predeterminado,
                                          controller.calcular_nota_calificacion(calificacion1, calificacion2))
                controller.actas[identificador_acta].detalles_criterio[identificador_criterio] = detalle
            else:
                comentario = st.text_input("Comentarios de los jurados")
                detalle = DetalleCriterio(identificador_criterio, calificacion1, calificacion2, comentario,
                                          controller.calcular_nota_calificacion(calificacion1, calificacion2))
                controller.actas[identificador_acta].detalles_criterio[identificador_criterio] = detalle

        elif criterio == "Cumplimiento de los objetivos propuestos":

            identificador_criterio = "3"
            calificacion1 = st.text_input("Calificacion 1")
            calificacion2 = st.text_input("Calificacion 2")
            choice1 = st.radio("¿Desea utilizar un comentario predeterminado?", ["Si", "No"])
            if choice1 == "Si":
                predeterminado = st.selectbox("Elija la opcion predeterminada", [""])
                detalle = DetalleCriterio(identificador_criterio, calificacion1, calificacion2, predeterminado,
                                          controller.calcular_nota_calificacion(calificacion1, calificacion2))
                controller.actas[identificador_acta].detalles_criterio[identificador_criterio] = detalle
            else:
                comentario = st.text_input("Comentarios de los jurados")
                detalle = DetalleCriterio(identificador_criterio, calificacion1, calificacion2, comentario,
                                          controller.calcular_nota_calificacion(calificacion1, calificacion2))
                controller.actas[identificador_acta].detalles_criterio[identificador_criterio] = detalle

        elif criterio == "Creatividad e innovación de las soluciones y desarrollos propuestos":

            identificador_criterio = "4"
            calificacion1 = st.text_input("Calificacion 1")
            calificacion2 = st.text_input("Calificacion 2")
            choice1 = st.radio("¿Desea utilizar un comentario predeterminado?", ["Si", "No"])
            if choice1 == "Si":
                predeterminado = st.selectbox("Elija la opcion predeterminada", [""])
                detalle = DetalleCriterio(identificador_criterio, calificacion1, calificacion2, predeterminado,
                                          controller.calcular_nota_calificacion(calificacion1, calificacion2))
                controller.actas[identificador_acta].detalles_criterio[identificador_criterio] = detalle
            else:
                comentario = st.text_input("Comentarios de los jurados")
                detalle = DetalleCriterio(identificador_criterio, calificacion1, calificacion2, comentario,
                                          controller.calcular_nota_calificacion(calificacion1, calificacion2))
                controller.actas[identificador_acta].detalles_criterio[identificador_criterio] = detalle

        elif criterio == "Validez de los resultados y conclusiones":

            identificador_criterio = "5"
            calificacion1 = st.text_input("Calificacion 1")
            calificacion2 = st.text_input("Calificacion 2")
            choice1 = st.radio("¿Desea utilizar un comentario predeterminado?", ["Si", "No"])
            if choice1 == "Si":
                predeterminado = st.selectbox("Elija la opcion predeterminada", [""])
                detalle = DetalleCriterio(identificador_criterio, calificacion1, calificacion2, predeterminado,
                                          controller.calcular_nota_calificacion(calificacion1, calificacion2))
                controller.actas[identificador_acta].detalles_criterio[identificador_criterio] = detalle
            else:
                comentario = st.text_input("Comentarios de los jurados")
                detalle = DetalleCriterio(identificador_criterio, calificacion1, calificacion2, comentario,
                                          controller.calcular_nota_calificacion(calificacion1, calificacion2))
                controller.actas[identificador_acta].detalles_criterio[identificador_criterio] = detalle

        elif criterio == "Manejo y procesamiento de la información y bibliografía":

            identificador_criterio = "6"
            calificacion1 = st.text_input("Calificacion 1")
            calificacion2 = st.text_input("Calificacion 2")
            choice1 = st.radio("¿Desea utilizar un comentario predeterminado?", ["Si", "No"])
            if choice1 == "Si":
                predeterminado = st.selectbox("Elija la opcion predeterminada", [""])
                detalle = DetalleCriterio(identificador_criterio, calificacion1, calificacion2, predeterminado,
                                          controller.calcular_nota_calificacion(calificacion1, calificacion2))
                controller.actas[identificador_acta].detalles_criterio[identificador_criterio] = detalle
            else:
                comentario = st.text_input("Comentarios de los jurados")
                detalle = DetalleCriterio(identificador_criterio, calificacion1, calificacion2, comentario,
                                          controller.calcular_nota_calificacion(calificacion1, calificacion2))
                controller.actas[identificador_acta].detalles_criterio[identificador_criterio] = detalle

        elif criterio == "Calidad y presentación del documento escrito":

            identificador_criterio = "7"
            calificacion1 = st.text_input("Calificacion 1")
            calificacion2 = st.text_input("Calificacion 2")
            choice1 = st.radio("¿Desea utilizar un comentario predeterminado?", ["Si", "No"])
            if choice1 == "Si":
                predeterminado = st.selectbox("Elija la opcion predeterminada", [""])
                detalle = DetalleCriterio(identificador_criterio, calificacion1, calificacion2, predeterminado,
                                          controller.calcular_nota_calificacion(calificacion1, calificacion2))
                controller.actas[identificador_acta].detalles_criterio[identificador_criterio] = detalle
            else:
                comentario = st.text_input("Comentarios de los jurados")
                detalle = DetalleCriterio(identificador_criterio, calificacion1, calificacion2, comentario,
                                          controller.calcular_nota_calificacion(calificacion1, calificacion2))
                controller.actas[identificador_acta].detalles_criterio[identificador_criterio] = detalle

        elif criterio == "Presentación oral":

            identificador_criterio = "8"
            calificacion1 = st.text_input("Calificacion 1")
            calificacion2 = st.text_input("Calificacion 2")
            choice1 = st.radio("¿Desea utilizar un comentario predeterminado?", ["Si", "No"])
            if choice1 == "Si":
                predeterminado = st.selectbox("Elija la opcion predeterminada", [""])
                detalle = DetalleCriterio(identificador_criterio, calificacion1, calificacion2, predeterminado,
                                          controller.calcular_nota_calificacion(calificacion1, calificacion2))
                controller.actas[identificador_acta].detalles_criterio[identificador_criterio] = detalle
            else:
                comentario = st.text_input("Comentarios de los jurados")
                detalle = DetalleCriterio(identificador_criterio, calificacion1, calificacion2, comentario,
                                          controller.calcular_nota_calificacion(calificacion1, calificacion2))
                controller.actas[identificador_acta].detalles_criterio[identificador_criterio] = detalle
        if st.button("Enviar calificaciones") and len(controller.actas[identificador_acta].detalles_criterio) == 8:
            st.success("Las calificaciones se han agregado exitosamente")
        else:
            st.error("Hace falta por calificar el criterios")
