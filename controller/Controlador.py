from model.Criterio import Criterio


class Controlador:
    def __init__(self) -> None:

        self.actas = {}
        self.current_length = 0
        self.criterios = {1: Criterio(1, "Desarrollo y profundidad en el tratamiento del tema",
                                      "", 0.20),
                          2: Criterio(2, "Desafío académico y científico del tema",
                                      "", 0.15),
                          3: Criterio(3, "Cumplimiento de los objetivos propuestos",
                                      "", 0.10),
                          4: Criterio(4, "Creatividad e innovación de las soluciones y desarrollos propuestos:",
                                      "", 0.10),
                          5: Criterio(5, "Validez de los resultados y conclusiones",
                                      "", 0.10),
                          6: Criterio(6, "Manejo y procesamiento de la información y bibliografía",
                                      "", 0.10),
                          7: Criterio(7, "Calidad y presentación del documento escrito",
                                      "", 0.075),
                          8: Criterio(8, "Presentación oral", "", 0.075)}
