from model.Criterio import *


def director_partial(st, controller):

    st.title("Portal de modificación de criterios")

    # eleccion de la modalidad que se desea implementar: agregar, modificar o eliminar un criterio
    opcion = st.selectbox("Seleccione la opcion que desea realizar", ["Modificar criterio",
                                                             "Agregar criterio",
                                                             "Eliminar criterio"])

    # se obtienen los identificadores de los criterios
    criterios = controller.criterios.keys()

    if opcion == "Modificar criterio":
        # selección del criterio a modificar
        criterio_modificar = st.selectbox("Seleccione el identificador del criterio que desea modificar",
                                          list(criterios))
        # mostrar los datos actuales del criterio
        controller.mostrar_criterio(criterio_modificar)
        # recolectar los nuevos datos del criterio
        controller.recolectar_datos_criterio(criterio_modificar)

    elif opcion == "Agregar criterio":
        # recoleta los datos del nuevo criterio
        nombre_criterio = st.text_input("Nombre del criterio:")
        descripcion = st.text_area("Descripción del criterio:")
        ponderado = st.number_input("Porcentaje de ponderación del criterio:", 5, 100)
        predeterminados = []
        for i in range(0, 3):
            predeterminados.append(st.text_input("Comentario prederminado " + str(i + 1) + ":"))

        if st.button("Crear criterio"):
            # crea un objeto de tipo criterio con los datos recolectados
            criterio = Criterio(len(controller.criterios) + 1, nombre_criterio, descripcion, ponderado/100)
            # se agrega el nuevo criterio al diccionario de criterios del controlador
            controller.criterios[criterio.identificador] = criterio
            controller.predeterminados_criterio[len(controller.criterios)] = predeterminados
            # se suma 1 a la cantidad actual de criterios
            controller.current_length_criterios += 1
            st.success("Se ha agregado con éxito el criterio")

            st.subheader("Criterios actuales")
            # se muestran los detalles de cada criterio disponibles
            for i in range(1, len(controller.criterios) + 1):
                controller.mostrar_criterio(i)

    elif opcion == "Eliminar criterio":

        # seleccion del criterio a eliminar
        criterio_eliminar = st.selectbox("Seleccione el criterio que desea eliminar", list(criterios))
        # se muestran los datos del criterio a eliminar
        controller.mostrar_criterio(criterio_eliminar)
        if st.button("Eliminar criterio"):
            # se elimina el objeto almacenado en la llave indicada
            del controller.criterios[criterio_eliminar]
            # se resta 1 a la cantidad actual de criterios
            controller.current_length_criterios -= 1
            st.success("Se ha eliminado correctamente el criterio")

            # se muestran los datos de los criterios restantes
            st.subheader("Criterios actuales")
            for i in range(1, len(controller.criterios) + 1):
                controller.mostrar_criterio(i)
