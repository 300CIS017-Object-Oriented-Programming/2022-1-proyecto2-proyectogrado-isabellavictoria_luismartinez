

def historial_partial(st, controller):

    st.title("Historial de actas")
    keys = list(controller.actas.keys())
    for i in range(0, len(controller.actas)):
        with st.expander("Acta No. " + keys[i]):
            col1, col2, col3, col4, col5, col6 = st.columns(6)

        with col1:
            st.markdown("**ID Estudiante**")
            st.markdown(controller.actas[keys[i]].id_estudiante)

        with col2:
            st.markdown("**Nombre estudiante**")
            st.markdown(controller.actas[keys[i]].nombre_estudiante)

        with col3:
            st.markdown("**Nombre trabajo**")
            st.markdown(controller.actas[keys[i]].titulo_trabajo)

        with col4:
            st.markdown("**Tipo trabajo**")
            st.markdown(controller.actas[keys[i]].tipo_trabajo)

        with col5:
            st.markdown("**Estado trabajo**")
            st.code(controller.actas[keys[i]].estado)

        with col6:
            st.markdown("**Nota trabajo**")
            st.markdown(controller.actas[keys[i]].nota_trabajo)

