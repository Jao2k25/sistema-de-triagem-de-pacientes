class Paciente:
    def __init__(self, nome, cpf, telefone, endereco, classificacao_risco):
        # Inicializa um objeto Paciente com os dados fornecidos.
        # nome (str): Nome completo do paciente.
        # cpf (str): Cadastro de Pessoa Física do paciente.
        # telefone (str): Número de telefone para contato.
        # endereco (str): Endereço completo do paciente.
        # classificacao_risco (int): Nível de risco do paciente (1 a 5, onde 1 é o mais grave).
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco
        self.classificacao_risco = classificacao_risco

    def __str__(self):
        # Retorna uma representação em string do objeto Paciente, útil para impressão.
        return f"Nome: {self.nome}, CPF: {self.cpf}, Risco: {self.classificacao_risco}"


