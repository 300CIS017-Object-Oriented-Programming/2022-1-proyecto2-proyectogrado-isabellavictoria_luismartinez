

def jurado_partial(st):

    st.title("Portal de calificacion de actas")
    nombre_jurado1 = st.text_input("Nombre del Jurado 1")

    criterio = st.selectbox("Elija criterio por calificar", ["Desarrollo y profundidad en el tratamiento del tema",
                                                             "Desafío académico y científico del tema",
                                                             "Cumplimiento de los objetivos propuestos",
                                                             "Creatividad e innovación de las soluciones y desarrollos propuestos",
                                                             ""])

    calificacion1 = st.text_input("Calificacion 1")
    choice1 = st.radio("Desea utilizar un comentario predeterminado basado en la nota del estudiante", ["Si", "No"])

    if choice1 == "Si":
        predeterminado = st.selectbox("Elija la opcion predeterminada", [""])

    comentario1 = st.text_input("Comentarios Jurado 1")
    nombre_jurado2 = st.text_input("Nombre del Jurado 2")
    calificacion2 = st.text_input("Calificacion 2")
    choice2 = st.radio("Desea utilizar un comentario predeterminado basado en la nota del estudiante", ["Si", "No"])
    comentario2 = st.text_input("Comentarios del Jurado 2")

