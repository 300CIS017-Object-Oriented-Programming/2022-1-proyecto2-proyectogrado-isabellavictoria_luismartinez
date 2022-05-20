from model.Acta import Acta

def asistente_partial(st, controller):

    st.title("Portal de creacion de Actas")

    numero_acta = st.text_input("Numero del acta")
    fecha = st.date_input("Fecha de creacion del acta")
    id_estudiante = st.text_input("ID del estudiante")
    nombre_estudiante = st.text_input("Nombre del estudiante")
    periodo = st.text_input("Periodo")
    titulo_trabajo = st.text_input("Titulo del trabajo")
    tipo_trabajo = st.text_input("Tipo de trabajo")
    nombre_director = st.text_input("Nombre del director")
    nombre_codirector = st.text_input("Nombre del codirector")
    nombre_jurado1 = st.text_input("Nombre del Jurado 1")
    nombre_jurado2 = st.text_input("Nombre del Jurado 2")

    if st.button("Crear Acta"):
        acta_modelo = Acta(numero_acta, fecha, id_estudiante, nombre_estudiante,
                           periodo, titulo_trabajo, tipo_trabajo, nombre_director,
                           nombre_codirector, nombre_jurado1, nombre_jurado2,
                           controller.criterios, {}, "comentarios_adicionales",
                           0.0, "Por calificar")

        controller.actas[numero_acta] = acta_modelo
        controller.current_length += 1

        if len(controller.actas) == controller.current_length:
            st.success("El acta ha sido creada correctamente")
        else:
            st.error("No se ha podido crear el acta")



