from model.Detalle_Criterio import *


def jurado_partial(st, controller):
    if len(controller.actas) != 0:
        st.title("Portal de calificación de actas")

        actas = controller.actas.keys()
        identificador_acta = st.selectbox("Seleccione el identificador del acta por calificar", list(actas))

        for i in range(1, len(controller.criterios) + 1):

            with st.expander(controller.criterios[i].nombre_criterio):
                identificador_criterio = str(i)
                controller.recolectar_datos_detalle_criterio(identificador_criterio, identificador_acta)

        with st.expander("Comentarios adicionales"):
            comentarios_adicionales = st.text_area("Ingrese las observaciones para aprobar el trabajo de grado o "
                                               "alguna otra observación fuera de los criterios:")

        if st.button("Enviar calificaciones"):
            if len(controller.actas[identificador_acta].detalles_criterio) != controller.current_length_criterios:
                st.error("Faltan criterios por calificar, no se puede calcular nota del trabajo")
            else:
                nota_trabajo = round(controller.calcular_nota_trabajo(identificador_acta), 2)
                controller.actas[identificador_acta].nota_trabajo = nota_trabajo
                controller.actas[identificador_acta].comentarios_adicionales = comentarios_adicionales
                st.success("Las calificaciones se han agregado exitosamente")
                if nota_trabajo > 3.0:
                    controller.actas[identificador_acta].estado = "Aprobado - Calificada"
                else:
                    controller.actas[identificador_acta].estado = "Reprobado - Calificada"

    else:
        raise ValueError("No hay actas creadas actualmente")

