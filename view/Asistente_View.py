def asistente_partial(st, controller):
    st.title("Portal de creacion de Actas")

    numero_acta = st.text_input("Numero del acta")
    fecha = st.date_input("Fecha de creacion del acta")
    id_estudiante = st.text_input("Periodo")
    nombre_estudiante = st.text_input("ID del estudiante")
    periodo = st.text_input("Nombre del estudiante")
    titulo_trabajo = st.text_input("Titulo del trabajo")
    tipo_trabajo = st.text_input("Tipo de trabajo")
    nombre_director = st.text_input("Nombre del director")
    nombre_codirector = st.text_input("Nombre del codirector")
    nombre_jurado1 = st.text_input("Nombre del Jurado 1")
    nombre_jurado2 = st.text_input("Nombre del Jurado 2")

   #if st.button("Crear acta"):
        #controller.crear_acta(numero_acta, fecha, id_estudiante, nombre_estudiante, periodo, titulo_trabajo,
                            # tipo_trabajo, nombre_director, nombre_codirector, nombre_jurado1, nombre_jurado2)



