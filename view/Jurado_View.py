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

    for i in range(1, len(controller.criterios) + 1):

        with st.expander(controller.criterios[i].nombre_criterio):
            identificador_criterio = str(i)
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


