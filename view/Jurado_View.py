from model.Detalle_Criterio import *


def jurado_partial(st, controller):
    if len(controller.actas) != 0: # excepción para verificar que exista al menos 1 acta para calificar
        st.title("Portal de calificación de actas")

        # se llaman todos los identificadores de las actas
        actas = controller.actas.keys()
        # seleccion del identificador del acta a calificar
        identificador_acta = st.selectbox("Seleccione el identificador del acta por calificar", list(actas))

        # ciclo para mostrar cada criterio a calificar
        for i in range(1, len(controller.criterios) + 1):

            with st.expander(controller.criterios[i].nombre_criterio):
                identificador_criterio = str(i)
                # recolecta las calificaciones y comentarios
                controller.recolectar_datos_detalle_criterio(identificador_criterio, identificador_acta)

        # se pide el comentario adicional para cada acta
        with st.expander("Comentarios adicionales"):
            comentarios_adicionales = st.text_area("Ingrese las observaciones para aprobar el trabajo de grado o "
                                                   "alguna otra observación fuera de los criterios:")

        if st.button("Enviar calificaciones"):
            # verificacion de que se hayan calificado todos los criterios
            if len(controller.actas[identificador_acta].detalles_criterio) != controller.current_length_criterios:
                st.error("Faltan criterios por calificar, no se puede calcular nota del trabajo")
            else:
                # se calcula la nota del trabajo
                nota_trabajo = round(controller.calcular_nota_trabajo(identificador_acta), 2)
                # se agrega la nota del trabajo al diccionario de calificaciones del acta guardada en el diccionario de actas del controlador
                controller.actas[identificador_acta].nota_trabajo = nota_trabajo
                # se agregan los comentarios adicionales al respectivo objeto acta dentro del diccionario del controlador
                controller.actas[identificador_acta].comentarios_adicionales = comentarios_adicionales
                # se notifica del éxito del agregado de notas
                st.success("Las calificaciones se han agregado exitosamente")
                # en caso de que el trabajo halla alcanzado una nota igual o mayor a 3 se cambia el estado a aprobado, en caso contrario como reprobado
                if nota_trabajo >= 3.0:
                    controller.actas[identificador_acta].estado = "Aprobado - Calificada"
                else:
                    controller.actas[identificador_acta].estado = "Reprobado - Calificada"

    else:
        raise ValueError("No hay actas creadas actualmente")

