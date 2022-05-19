import streamlit
from fpdf import FPDF
from controller.Controlador import *


def exportar_acta(st):
    from datetime import datetime
    numero_act = 1
    st.title("PDF Prueba")
    pdf = FPDF()
    pdf.add_page()
    dia = datetime.today().strftime('%Y-%m-%d')
    año = datetime.today().strftime('%Y')
    pdf.set_font('Arial', 'B', size=15)

    pdf.image('https://redvalorcompartido.com/wp-content/uploads/2020/06/logo-universidad-javeriana.png', 15, 10,
              40)

    pdf.cell(200, 10, txt='Facultad de Ingeniería', ln=0, align='C')
    pdf.cell(200, 10, txt='Maestría en Ingeniería', ln=2, align='C')
    pdf.set_font('Arial', size=11)
    pdf.cell(150, 10, txt='ACTA: ' + "11" + '-' + año, ln=0, align= 'L')
    pdf.cell(100, 10, txt='Fecha: ' + dia, ln=1, align='L')
    pdf.cell(200, 10, txt='ACTA DE EVALUACIÓN DE TRABAJO DE GRADO', ln=1, align='C')

    # for posicion in controller.actas:
    pdf.cell(63, 10, txt='Trabajo de grado denominado: ', ln=1, align='L')
    # pdf.cell(80, 10, txt=str(posicion.tema_proyecto), ln=1, align='L')
    pdf.cell(40, 10, txt='Autor: ', ln=1, align='L')
    # pdf.cell(100, 10, txt=str(posicion.nombre), ln=0, align='L')
    # pdf.cell(50, 10, txt='ID: '+str(posicion.id_estudiante), ln=1, align='L')
    pdf.cell(40, 10, txt='Periodo: ', ln=1, align='L')
    # pdf.cell(100, 10, txt=str(posicion.periodo), ln=1, align='L')
    pdf.cell(40, 10, txt='Director: ', ln=1, align='L')
    # pdf.cell(100, 10, txt=str(posicion.director), ln=1, align='L')
    pdf.cell(40, 10, txt='Co-Director: ', ln=1, align='L')
    # pdf.cell(100, 10, txt=str(posicion.co_director), ln=1, align='L')
    pdf.cell(40, 10, txt='Énfasis en:  ', ln=1, align='L')
    # pdf.cell(100, 10, txt=str(posicion.enfasis), ln=1, align='L')
    pdf.cell(40, 10, txt='Modalidad:  ', ln=1, align='L')
    # pdf.cell(100, 10, txt=str(posicion.modalidad), ln=1, align='L')
    pdf.cell(40, 10, txt='Jurado 1:  ', ln=1, align='L')
    # pdf.cell(100, 10, txt=str(posicion.jurado1), ln=1, align='L')
    pdf.cell(40, 10, txt='Jurado 2:  ', ln=1, align='L')
    # pdf.cell(100, 10, txt=str(posicion.jurado2), ln=1, align='L')



    enviar_calificacion = st.button('Generar PDF')
    nombre = st.text_input('Nombre del acta')
    if enviar_calificacion:
        pdf.output(nombre + '.pdf')
        st.write('ACTA GENERADA')
        st.write('El nombre del acta es:', nombre + '.pdf')
    while numero_act < 10000:
        numero_act += 1

