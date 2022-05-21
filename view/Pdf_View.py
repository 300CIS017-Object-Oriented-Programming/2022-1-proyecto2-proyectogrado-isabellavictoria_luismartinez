from fpdf import FPDF
from view.Pdf_functions import *
from model.Detalle_Criterio import *

def generar_pdf(st, controller):
    actas = controller.actas.keys()
    identificador_acta = st.selectbox("Seleccione el identificador del acta por calificar", list(actas))
    numero_act = 1
    pdf = PDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', size=11)
    pdf.cell(200, 5, txt='ACTA DE EVALUACIÓN DE TRABAJO DE GRADO', ln=1, align='C')
    pdf.set_font('Arial', size=11)
    pdf.ln(5)
    pdf.cell(63, 10, txt='Trabajo de grado denominado: ', ln=0, align='L')
    pdf.multi_cell(190, 10,txt=str(controller.actas[identificador_acta].titulo_trabajo),align='L')
    #pdf.cell(80, 10, txt=str(controller.actas[identificador_acta].titulo_trabajo), ln=1, align='L')
    pdf.cell(40, 10, txt='Autor: ', ln=0, align='L')
    pdf.cell(100, 10, txt=str(controller.actas[identificador_acta].nombre_estudiante), ln=0, align='L')
    pdf.cell(50, 10, txt='ID: '+str(controller.actas[identificador_acta].id_estudiante), ln=1, align='L')
    pdf.cell(40, 10, txt='Periodo: ', ln=0, align='L')
    pdf.cell(100, 10, txt=str(controller.actas[identificador_acta].periodo), ln=1, align='L')
    pdf.cell(40, 10, txt='Director: ', ln=0, align='L')
    pdf.cell(100, 10, txt=str(controller.actas[identificador_acta].nombre_director), ln=1, align='L')
    pdf.cell(40, 10, txt='Co-Director: ', ln=0, align='L')
    pdf.cell(100, 10, txt=str(controller.actas[identificador_acta].nombre_codirector), ln=1, align='L')
    pdf.cell(40, 10, txt='Énfasis en:  ', ln=0, align='L')
    pdf.cell(100, 10, txt=str(controller.actas[identificador_acta].enfasis), ln=1, align='L')
    pdf.cell(40, 10, txt='Modalidad:  ', ln=0, align='L')
    pdf.cell(100, 10, txt=str(controller.actas[identificador_acta].tipo_trabajo), ln=1, align='L')
    pdf.cell(40, 10, txt='Jurado 1:  ', ln=0, align='L')
    pdf.cell(100, 10, txt=str(controller.actas[identificador_acta].nombre_jurado1), ln=1, align='L')
    pdf.cell(40, 10, txt='Jurado 2:  ', ln=0, align='L')
    pdf.cell(100, 10, txt=str(controller.actas[identificador_acta].nombre_jurado2), ln=1, align='L')
    pdf.ln(10)
    pdf.multi_cell(190,5,txt="En atención al desarrollo de este Trabajo de Grado y al documento y sustentación que presentó el(la) autor(a), "
                              "los Jurados damos las siguientes calificaciones parciales y observaciones (los criterios a evaluar y sus "
                              "ponderaciones se estipulan en el artículo 7.1 de las Directrices para Trabajo de Grado de Maestría):", align='L')
    pdf.ln(5)
    pdf.set_font('Arial', 'B', size=11)
    criterios_aux = controller.actas[identificador_acta].criterios
    for x in range ( 0, len(criterios_aux),1):
        pdf.multi_cell(190, 5,txt=str(controller.actas[identificador_acta].criterios[x + 1].identificador) + '.  ' + str(
        controller.actas[identificador_acta].criterios[x + 1].nombre_criterio),align='L')
        pdf.ln(2)
        pdf.set_font('Arial', size=11)
        if controller.actas[identificador_acta].detalles_criterio[criterios_aux[x + 1].identificador].identificador_criterio == controller.actas[identificador_acta].criterios[x + 1].identificador:
            pdf.cell(150,5,txt= "Calificacion parcial: "+ str(controller.actas[identificador_acta].detalles_criterio[criterios_aux[x + 1].identificador].nota_criterio),ln= 0,align= 'L')
            pdf.cell(100,5,txt= "Ponderacion: "+ str(criterios_aux[x+1].porcentaje_ponderacion * 100) + "%",ln= 1,align='L')
            pdf.cell(100,5,txt= "Observaciones: " + str(controller.actas[identificador_acta].detalles_criterio[criterios_aux[x + 1].identificador].comentario))
            pdf.set_font('Arial', 'B', size=11)
        pdf.ln(5)
        pdf.multi_cell(190, 5,
                       txt="_______________________________________________________________________________________________________________"
                           "_________________________________________________________________________________________________________________"
                           ,align='L')

        pdf.ln(5)



    enviar_calificacion = st.button('Generar PDF')
    nombre = st.text_input('Nombre del acta')
    if enviar_calificacion:
        pdf.output(nombre + '.pdf')
        st.write('ACTA GENERADA')
        st.write('El nombre del acta es:', nombre + '.pdf')
    while numero_act < 10000:
        numero_act += 1

