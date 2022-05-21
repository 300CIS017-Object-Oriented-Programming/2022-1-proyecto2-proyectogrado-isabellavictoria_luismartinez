


def director_partial(st, controller):

    st.title("Portal de modificación de criterios")

    opcion = st.selectbox("Seleccione la opcion que desea realizar", ["Modificar criterio",
                                                             "Agregar criterio",
                                                             "Eliminar criterio"])

    criterios = controller.criterios.keys()

    if opcion == "Modificar criterio":
        criterio_modificar = st.selectbox("Seleccione el identificador del criterio que desea modificar",
                                          list(criterios))
        controller.mostrar_criterio(criterio_modificar)
        controller.recolectar_datos_criterio(criterio_modificar)
    elif opcion == "Agregar criterio":
        pass
    elif opcion == "Eliminar criterio":
        pass