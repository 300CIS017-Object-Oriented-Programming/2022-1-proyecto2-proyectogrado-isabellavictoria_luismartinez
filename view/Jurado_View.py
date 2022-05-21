from model.Detalle_Criterio import *


def recolectar_datos_detalle_criterio(st, controller, identificador_criterio, identificador_acta):

    calificacion1 = st.number_input("Calificacion 1_" + str(identificador_criterio), 0, 5)
    calificacion2 = st.number_input("Calificacion 2_" + str(identificador_criterio), 0, 5)
    choice1 = st.radio("¿Desea utilizar un comentario predeterminado para criterio " + str(identificador_criterio) +
                       "?", ["Si", "No"])
    if choice1 == "Si":
        predeterminado = st.selectbox("Elija la opcion predeterminada para criterio " + str(identificador_criterio), [""])
        if st.button("Calificar criterio " + str(identificador_criterio)):
            detalle = DetalleCriterio(identificador_criterio, float(calificacion1), float(calificacion2), predeterminado, 0.0)
            controller.actas[identificador_acta].detalles_criterio[identificador_criterio] = detalle
            detalle.nota_criterio = controller.calcular_nota_criterio(calificacion1, calificacion2,
                                                                      identificador_criterio)
    else:
        comentario = st.text_area("Comentarios de los jurados para criterio" + str(identificador_criterio))
        if st.button("Calificar criterio " + str(identificador_criterio)):
            detalle = DetalleCriterio(identificador_criterio, float(calificacion1), float(calificacion2), comentario, 0.0)
            controller.actas[identificador_acta].detalles_criterio[identificador_criterio] = detalle
            detalle.nota_criterio = controller.calcular_nota_criterio(calificacion1, calificacion2,
                                                                      identificador_criterio)


def jurado_partial(st, controller):

    st.title("Portal de calificación de actas")

    actas = controller.actas.keys()
    identificador_acta = st.selectbox("Seleccione el identificador del acta por calificar", list(actas))

    with st.expander("Desarrollo y profundidad en el tratamiento del tema"):

        identificador_criterio = "1"
        recolectar_datos_detalle_criterio(st, controller, identificador_criterio, identificador_acta)

    with st.expander("Desafío académico y científico del tema"):

        identificador_criterio = "2"
        recolectar_datos_detalle_criterio(st, controller, identificador_criterio, identificador_acta)

    with st.expander("Cumplimiento de los objetivos propuestos"):
        identificador_criterio = "3"

        recolectar_datos_detalle_criterio(st, controller, identificador_criterio, identificador_acta)

    with st.expander("Creatividad e innovación de las soluciones y desarrollos propuestos"):
        identificador_criterio = "4"
        recolectar_datos_detalle_criterio(st, controller, identificador_criterio, identificador_acta)

    with st.expander("Validez de los resultados y conclusiones"):
        identificador_criterio = "5"
        recolectar_datos_detalle_criterio(st, controller, identificador_criterio, identificador_acta)

    with st.expander("Manejo y procesamiento de la información y bibliografía"):
        identificador_criterio = "6"
        recolectar_datos_detalle_criterio(st, controller, identificador_criterio, identificador_acta)

    with st.expander("Calidad y presentación del documento escrito"):
        identificador_criterio = "7"
        recolectar_datos_detalle_criterio(st, controller, identificador_criterio, identificador_acta)

    with st.expander("Presentación oral"):
        identificador_criterio = "8"
        recolectar_datos_detalle_criterio(st, controller, identificador_criterio, identificador_acta)

    with st.expander("Comentarios adicionales"):
        comentarios_adicionales = st.text_area("Ingrese las observaciones para aprobar el trabajo de grado o "
                                               "alguna otra observación fuera de los criterios:")


    if st.button("Enviar calificaciones"):
        if len(controller.actas[identificador_acta].detalles_criterio) != controller.current_length_criterios:
            st.error("Faltan criterios por calificar, no se puede calcular nota del trabajo")
        else:
            controller.calcular_nota_trabajo(identificador_acta)
            controller.actas[identificador_acta].comentarios_adicionales = comentarios_adicionales
            st.success("Las calificaciones se han agregado exitosamente")
            controller.actas[identificador_acta].estado = "Calificada"


