import heapq

class FilaPrioritaria:
    def __init__(self):
        # Inicializa uma nova fila prioritária.
        # A fila é implementada como um min-heap usando o módulo heapq.
        # O contador é usado para garantir a ordem de chegada em caso de pacientes com a mesma prioridade de risco.
        self.fila = []
        self.contador = 0

    def adicionar_paciente(self, paciente):
        # Adiciona um paciente à fila prioritária.
        # A prioridade é determinada pela classificação de risco do paciente.
        # Para simular um max-heap (maior risco = maior prioridade) com um min-heap,
        # armazenamos o negativo da classificação de risco.
        # O contador é incluído para desempate: pacientes adicionados antes têm prioridade
        # se tiverem a mesma classificação de risco.
        heapq.heappush(self.fila, (-paciente.classificacao_risco, self.contador, paciente))
        self.contador += 1

    def remover_paciente(self):
        # Remove e retorna o paciente com a maior prioridade (menor classificação de risco).
        # Se a fila estiver vazia, retorna None.
        if not self.fila:
            return None
        # heapq.heappop() remove e retorna o menor item do heap.
        # Como armazenamos o negativo do risco, isso nos dá o paciente com o maior risco (menor valor negativo).
        return heapq.heappop(self.fila)[2] # [2] para pegar o objeto Paciente

    def esta_vazia(self):
        # Verifica se a fila prioritária está vazia.
        return len(self.fila) == 0

    def tamanho(self):
        # Retorna o número de pacientes na fila prioritária.
        return len(self.fila)


