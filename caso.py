class Caso:
    def __init__(self, sintomas, febre, cortes, ulceras):
        # Inicializa um objeto Caso com os detalhes do quadro clínico do paciente.
        # sintomas (str): Descrição dos sintomas do paciente.
        # febre (bool): Indica se o paciente tem febre (True/False).
        # cortes (bool): Indica se o paciente tem cortes (True/False).
        # ulceras (bool): Indica se o paciente tem úlceras (True/False).
        self.sintomas = sintomas
        self.febre = febre
        self.cortes = cortes
        self.ulceras = ulceras

    def __str__(self):
        # Retorna uma representação em string do objeto Caso, útil para impressão.
        return f"Sintomas: {self.sintomas}, Febre: {self.febre}, Cortes: {self.cortes}, Úlceras: {self.ulceras}"


