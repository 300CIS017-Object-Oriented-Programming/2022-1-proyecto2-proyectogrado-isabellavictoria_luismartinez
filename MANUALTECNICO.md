# MANUAL TÉCNICO

## CLASES Y ATRIBUTOS
Este programa utiliza las siguientes clases principales para su correcto funcionamiento:

* Acta
* Criterio
* Detalle Criterio

Cada una de estas **clases** funcionan de la siguiente manera:
#### ACTA
En esta clase se guardan todos los atributos que contiene el acta:

* Número acta
* Fecha
* ID estudiante
* Nombre estudiante
* Periodo
* Titulo trabajo
* Énfasis
* Tipo trabajo
* Nombre director
* Nombre codirector
* Nombre jurado1
* Nombre jurado2
* Criterios
* Detalles criterio
* Comentarios adicionales
* Nota trabajo
* Estado


Todos estos serán recibidos como entradas en el apartado de **asistente** que será explicado más adelante.
#### CRITERIO
En esta clase se guardan todos los atributos que contiene el criterio:

* Identificador
* Nombre criterio
* Descripción criterio
* Porcentaje ponderación

Todos estos serán utilizados para guardar cada uno de los criterios que serán guardados en el diccionario de criterios del 
controlador.

#### DETALLE CRITERIO
En esta clase se guardan las calificaciones de los criterios:

* Identificador criterio
* Calificación 1
* Calificación 2
* Comentario
* Nota criterio

Todos estos atributos serán utilizados a la hora de calificar por parte de los *jurados*, función que será explicada más adelante.


# INTERFAZ Y FUNCIONAMIENTO
Para la interfaz se utilizan 7 archivos con los cuales se busca satisfacer de manera visual y funcional cada uno de los procesos
los cuales deben ser realizados por los diferentes actores de la página (Director@, Asistente, Jurado).

En el apartado del *asistente* se usaron diferentes cuadros de ingreso de texto con el fin de que el asistente pueda llenar
cada uno de los requerimientos del acta y por medio de un botón la agregue al diccionario de actas ubicado en el controlador.
Seguido de esto ya con el acta creada el *jurado* procede a ingresar a su interfaz la cual inicialmente le mostrara una lista
de actas, en la cual seleccionara el acta que desea calificar y con esto se desplegaran todos los criterios de la misma los
cuales se encuentran ubicados en el diccionario de criterios dentro del acta; finalmente guardando toda esta información en el
diccionario detalle criterio ubicado dentro del acta.

En la interfaz del *director@* se manejan funciones como la del cambio del criterio con la cual modifica el porcentaje de ponderación del mismo,
adicional a esto puede ver el historial de actas y el estado de las mismas utilizando el diccionario del controlador.

Finalmente, se cuenta con la interfaz que genera el *PDF* que utilizando la librería FPDF para Python y con la ayuda de esta
y el manejo de las variables de los diferentes diccionarios se genera el **ACTA**, lo cual es el objetivo principal del programa
guardando está dentro de la carpeta en la que está ubicada el mismo dentro del computador.


## RECURSOS USADOS DENTRO DEL PROGRAMA
* openpyxl
* streamlit 1.8.1
* streamlit-option-menu 0.3.2
* pydataxm  0.2.6
* fpdf 1.7.2
* fpdf2 2.5.4


Para apreciar un poco mejor la en que está modelado este programa se adjunta el archivo UML, y el link en el cual se puede
observar mejor la información del mismo.

## UML
![img_5.png](img_5.png)
*Link:* https://app.diagrams.net/#G1C4d8zLRvIG92U0l_BIQi7bx682WCfkUp
