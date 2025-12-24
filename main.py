from paciente import Paciente
from caso import Caso
from fila_prioritaria import FilaPrioritaria

def coletar_dados_paciente():
    """
    Coleta os dados de um novo paciente através da entrada do usuário.
    Solicita nome, CPF, telefone, endereço e a classificação de risco.
    A classificação de risco deve ser um número inteiro entre 1 e 5.
    Retorna um objeto Paciente com os dados coletados.
    """
    print("\n--- Coleta de Dados do Paciente ---")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")
    endereco = input("Endereço: ")
    while True:
        try:
            classificacao_risco = int(input("Classificação de Risco (1-5, onde 1 é o mais grave e 5 o menos grave): "))
            if 1 <= classificacao_risco <= 5:
                break
            else:
                print("Por favor, insira um número entre 1 e 5.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")
    return Paciente(nome, cpf, telefone, endereco, classificacao_risco)

def coletar_dados_caso():
    """
    Coleta os dados do caso clínico de um paciente através da entrada do usuário.
    Solicita sintomas, e se o paciente tem febre, cortes ou úlceras.
    Retorna um objeto Caso com os dados coletados.
    """
    print("\n--- Coleta de Dados do Caso ---")
    sintomas = input("Sintomas (descreva brevemente): ")
    febre_str = input("Tem febre? (sim/não): ").lower()
    febre = True if febre_str == 'sim' else False
    cortes_str = input("Tem cortes? (sim/não): ").lower()
    cortes = True if cortes_str == 'sim' else False
    ulceras_str = input("Tem úlceras? (sim/não): ").lower()
    ulceras = True if ulceras_str == 'sim' else False
    return Caso(sintomas, febre, cortes, ulceras)

def main():
    """
    Função principal que gerencia o sistema de triagem de pacientes.
    Permite adicionar pacientes, atender o próximo paciente na fila prioritária,
    visualizar a fila e sair do sistema.
    """
    fila_triagem = FilaPrioritaria()

    while True:
        print("\n--- Sistema de Triagem de Pacientes ---")
        print("1. Adicionar novo paciente")
        print("2. Atender próximo paciente")
        print("3. Visualizar fila")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            paciente = coletar_dados_paciente()
            caso = coletar_dados_caso()
            # Associa o caso ao paciente para manter a informação organizada.
            paciente.caso = caso
            fila_triagem.adicionar_paciente(paciente)
            print(f"Paciente {paciente.nome} adicionado à fila com prioridade {paciente.classificacao_risco}.")
        elif opcao == '2':
            paciente_atendido = fila_triagem.remover_paciente()
            if paciente_atendido:
                print(f"Paciente {paciente_atendido.nome} atendido e removido da fila.")
            else:
                print("A fila de triagem está vazia.")
        elif opcao == '3':
            if fila_triagem.esta_vazia():
                print("A fila de triagem está vazia.")
            else:
                print("\n--- Pacientes na Fila (Ordem de Prioridade) ---")
                # Para visualizar a fila sem remover, criamos uma cópia e a ordenamos.
                # A ordem é do maior risco (menor número de classificação) para o menor risco.
                # O heap armazena (-risco, contador, paciente), então ordenar pelo primeiro elemento
                # da tupla já nos dá a ordem correta de prioridade.
                temp_fila = sorted(fila_triagem.fila, key=lambda x: x[0])
                for i, (prioridade_negativa, _, paciente) in enumerate(temp_fila):
                    print(f"{i+1}. {paciente}")
        elif opcao == '4':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()


