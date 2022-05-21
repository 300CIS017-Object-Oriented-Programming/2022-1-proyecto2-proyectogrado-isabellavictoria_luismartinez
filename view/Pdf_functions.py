import streamlit
from fpdf import FPDF
from controller.Controlador import *


class PDF(FPDF):
    def header(self):
        from datetime import datetime
        dia = datetime.today().strftime('%Y-%m-%d')
        año = datetime.today().strftime('%Y')
        self.set_font('Arial', 'B', size=15)
        self.cell(200, 5, txt='Facultad de Ingeniería', ln=1, align='C')
        self.cell(200, 5, txt='Maestría en Ingeniería', ln=1, align='C')
        self.image('https://redvalorcompartido.com/wp-content/uploads/2020/06/logo-universidad-javeriana.png', 10, 5,45)
        self.set_font('Arial', 'B', size=11)
        self.ln(10)
        self.cell(155, 10, txt='ACTA: ' + "11" + '-' + año, ln=0, align='L')
        self.set_font('Arial', size=11)
        self.cell(100, 10, txt='Fecha: ' + dia, ln=1, align='L')



