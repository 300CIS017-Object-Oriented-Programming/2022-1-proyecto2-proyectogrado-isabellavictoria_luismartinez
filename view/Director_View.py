from model.Criterio import *


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
        nombre_criterio = st.text_input("Nombre del criterio:")
        descripcion = st.text_area("Descripción del criterio:")
        ponderado = st.number_input("Porcentaje de ponderación del criterio:", 5, 100)

        if st.button("Crear criterio"):
            criterio = Criterio(len(controller.criterios) + 1, nombre_criterio, descripcion, ponderado/100)
            controller.criterios[criterio.identificador] = criterio
            controller.current_length_criterios += 1
            st.success("Se ha agregado con éxito el criterio")

            st.subheader("Criterios actuales")
            for i in range(1, len(controller.criterios) + 1):
                controller.mostrar_criterio(i)

    elif opcion == "Eliminar criterio":

        criterio_eliminar = st.selectbox("Seleccione el criterio que desea eliminar", list(criterios))
        controller.mostrar_criterio(criterio_eliminar)
        if st.button("Eliminar criterio"):
            del controller.criterios[criterio_eliminar]
            controller.current_length_criterios -= 1
            st.success("Se ha eliminado correctamente el criterio")

            st.subheader("Criterios actuales")
            for i in range(1, len(controller.criterios) + 1):
                controller.mostrar_criterio(i)
