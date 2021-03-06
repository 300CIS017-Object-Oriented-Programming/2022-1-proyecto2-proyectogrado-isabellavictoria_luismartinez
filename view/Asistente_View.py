from model.Acta import Acta


def asistente_partial(st, controller):

    st.title("Portal de creación de Actas")

    # Se recolectan datos para la creación del acta
    numero_acta = st.text_input("Numero del acta")
    fecha = st.date_input("Fecha de creacion del acta")
    titulo_trabajo = st.text_input("Titulo del trabajo")
    nombre_estudiante = st.text_input("Nombre del estudiante")
    id_estudiante = st.text_input("ID del estudiante")
    periodo = st.text_input("Periodo")
    nombre_director = st.text_input("Nombre del director")
    existencia_codirector = st.radio("¿Existe codirector para el proyecto?", ["Si", "No"])
    # se pregunta por la existencia de un codirectori
    if existencia_codirector == "Si":
        nombre_codirector = st.text_input("Nombre del codirector")
    enfasis = st.text_input("Enfasis")
    tipo_trabajo = st.selectbox("Tipo de trabajo", ["Investigativo", "Aplicativo"])
    nombre_jurado1 = st.text_input("Nombre del Jurado 1")
    nombre_jurado2 = st.text_input("Nombre del Jurado 2")

    if st.button("Crear Acta"):
        # se crea acta de pendiendo de si tiene o no codirector
        if existencia_codirector == "Si":
            acta_modelo = Acta(numero_acta, fecha, id_estudiante, nombre_estudiante,
                           periodo, titulo_trabajo, enfasis, tipo_trabajo, nombre_director,
                           nombre_codirector, nombre_jurado1, nombre_jurado2,
                           controller.criterios, {}, "comentarios_adicionales",
                           0.0, "Por calificar")
        else:
            acta_modelo = Acta(numero_acta, fecha, id_estudiante, nombre_estudiante,
                               periodo, titulo_trabajo, enfasis, tipo_trabajo, nombre_director,
                               "No aplica", nombre_jurado1, nombre_jurado2,
                               controller.criterios, {}, "comentarios_adicionales",
                               0.0, "Por calificar")

        # se agrega el acta al diccionario en el controlador
        controller.actas[numero_acta] = acta_modelo
        # se suma uno a la cantidad actual de actas
        controller.current_length_actas += 1

        # se verifica que se halla añadido el acta
        if len(controller.actas) == controller.current_length_actas:
            st.success("El acta ha sido creada correctamente")
        else:
            st.error("No se ha podido crear el acta")



