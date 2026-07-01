# main.py
from src.administrador import Administrador
from src.paciente import Paciente
from src.consulta import Consulta
from src.unidadeSaude import UnidadeSaude
from src.agenda import Agenda
from src.funcionario import Funcionario
from src.cpf import is_cpf_valido
from datetime import datetime, date, timedelta


hoje = datetime.now()
dias_para_marca = hoje + timedelta(days=2)

# --- Dados de teste ---
admin_teste = Administrador(1, "Diogo", "12377756980", "diogoCarvalho@teste.com", "89012", "diogo4545", "1")
paciente_teste = Paciente(1, "Victor", "12345678910", "victor@teste.com", "1234", "victor123", "123", "17/06/2001", "Joinville")
unidade_teste = UnidadeSaude(1, "Posto Arroz Frito", "Muito Longe de Casa")
funcionario_teste = Funcionario(1, "Rafael", "12345678980", "rafael@teste.com", "3123123", "1234", "12345678", "Funcionario")

agenda_cardio = Agenda(1, "Dr. Roberto", "Cardiologia", unidade_teste, dias_para_marca.strftime("%d/%m/%Y"))
agenda_odonto = Agenda(2, "Dra. Ana", "Odontologia", unidade_teste, dias_para_marca.strftime("%d/%m/%Y"))

# Consulta de teste já referencia a agenda para F4 funcionar corretamente
consulta_teste = Consulta(1, "27/06/2027", "Agendada", "Odontologia", paciente_teste,
                          unidade_teste, agenda_odonto)
agenda_odonto.ocupar()  # Marca a vaga como ocupada pois já há uma consulta de teste

base_usuarios = [admin_teste, paciente_teste, funcionario_teste]
base_unidades = [unidade_teste]
base_consultas = [consulta_teste]
agendas_disponiveis = [agenda_cardio, agenda_odonto]


# --- Funções auxiliares ---

def mostrar_consulta(paciente_logado):
    print(f"\nConsultas de {paciente_logado.nome}:")
    encontrou = False
    for c in base_consultas:
        if c.paciente == paciente_logado:
            print(f"  ID: [{c.id_consulta}] | Especialidade: {c.especialidade} "
                  f"| Status: {c.status} | Data: {c.data_hora}")
            encontrou = True
    if not encontrou:
        print("  Nenhuma consulta encontrada.")


def cadastrar_paciente():
    id_usuario = input("Digite o ID: ")
    nome = input("Nome: ")
    cpf = input("CPF: ")

    # RN1.1: valida o dígito verificador do CPF antes de prosseguir
    if not is_cpf_valido(cpf):
        print("\n" + "=" * 30)
        print("Erro: CPF inválido.")
        print("=" * 30)
        return

    email = input("Email: ")
    telefone = input("Telefone: ")
    senha = input("Senha: ")
    cartao_sus = input("Cartão do SUS: ")
    data_nasc = input("Data de Nascimento: ")
    endereco = input("Endereço: ")

    for usuario in base_usuarios:
        if usuario.cpf == cpf:
            print("\n" + "=" * 30)
            print("Erro: CPF já cadastrado.")
            print("=" * 30)
            return

    novo_paciente = Paciente(id_usuario, nome, cpf, email, telefone, senha,
                             cartao_sus, data_nasc, endereco)
    base_usuarios.append(novo_paciente)
    print("\nPaciente cadastrado com sucesso!")


def exibir_menu_admin():
    while True:
        print("\n" + "=" * 30)
        print("SISTEMA DE AGENDAMENTO - ADMINISTRADOR")
        print("=" * 30)
        print("1. Cadastrar nova unidade de saúde")
        print("2. Cadastrar paciente")
        print("3. Editar unidade de saúde")
        print("4. Desativar unidade de saúde")
        print("5. Listar unidades de saúde")
        print("0. Sair")
        print("=" * 30)

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            id_unidade = input("ID da unidade: ")
            nome_unidade = input("Nome da unidade: ")
            endereco = input("Endereço da unidade: ")
            nova_unidade = UnidadeSaude(id_unidade, nome_unidade, endereco)
            base_unidades.append(nova_unidade)
            print("Unidade cadastrada com sucesso!")

        elif escolha == "2":
            cadastrar_paciente()

        elif escolha == "3":
            print("\nUnidades cadastradas:")
            for u in base_unidades:
                status = "Ativa" if u.ativa else "Inativa"
                print(f"  [{u.id}] {u.nome} | {u.endereco} | Status: {status}")

            id_editar = input("\nID da unidade para editar: ")
            unidade_editar = next((u for u in base_unidades if str(u.id) == id_editar), None)

            if unidade_editar is None:
                print("Unidade não encontrada.")
            else:
                novo_nome = input(f"Novo nome (Enter para manter '{unidade_editar.nome}'): ").strip()
                novo_end = input(f"Novo endereço (Enter para manter '{unidade_editar.endereco}'): ").strip()
                unidade_editar.atualizar_dados(novo_nome or None, novo_end or None)

        elif escolha == "4":
            ativas = [u for u in base_unidades if u.ativa]
            if not ativas:
                print("Nenhuma unidade ativa.")
            else:
                for u in ativas:
                    print(f"  [{u.id}] {u.nome} | {u.endereco}")

                id_desativar = input("ID da unidade para desativar: ")
                unidade_desativar = next((u for u in ativas if str(u.id) == id_desativar), None)

                if unidade_desativar is None:
                    print("Unidade não encontrada ou já inativa.")
                else:
                    tem_pendentes = any(
                        c.status == "Agendada" and c.unidade == unidade_desativar
                        for c in base_consultas
                    )
                    if tem_pendentes:
                        print(f"[ERRO] RN10.1: '{unidade_desativar.nome}' possui consultas "
                              f"pendentes e não pode ser desativada.")
                    else:
                        unidade_desativar.desativar()

        elif escolha == "5":
            print("\nTodas as unidades:")
            for u in base_unidades:
                status = "Ativa" if u.ativa else "Inativa"
                print(f"  [{u.id}] {u.nome} | {u.endereco} | Status: {status}")

        elif escolha == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")


def escolher_unidade_saude(paciente_logado):
    """F3: agendamento de consulta com controle de vagas (RN3.1)."""
    print("\n" + "=" * 30)
    print("Escolha uma unidade de saúde:")
    print("=" * 30)

    unidades_ativas = [u for u in base_unidades if u.ativa]
    if not unidades_ativas:
        print("Nenhuma unidade de saúde disponível no momento.")
        return

    for unidade in unidades_ativas:
        print(f"  [{unidade.id}] {unidade.nome} | Endereço: {unidade.endereco}")

    id_escolhido = input("\nDigite o ID da unidade desejada: ")
    unidade_selecionada = next(
        (u for u in unidades_ativas if str(u.id) == id_escolhido), None
    )

    if unidade_selecionada is None:
        print("Unidade não encontrada.")
        return

    # F3: filtra apenas agendas disponíveis (não ocupadas) da unidade escolhida
    agendas_da_unidade = [
        a for a in agendas_disponiveis
        if a.unidade == unidade_selecionada and a.disponivel
    ]

    if not agendas_da_unidade:
        print(f"\nNenhuma vaga disponível em {unidade_selecionada.nome} no momento.")
        return

    print(f"\nVagas disponíveis em {unidade_selecionada.nome}:")
    for agenda in agendas_da_unidade:
        print(f"  [{agenda.id}] {agenda.especialidade} com {agenda.profissional} - {agenda.horario}")

    id_agenda_escolhida = input("\nDigite o ID da vaga que deseja agendar: ")
    agenda_selecionada = next(
        (a for a in agendas_da_unidade if str(a.id) == id_agenda_escolhida), None
    )

    if agenda_selecionada is None:
        print("ID da vaga não encontrado.")
        return

    # RN3.1: paciente não pode ter dois agendamentos ativos na mesma especialidade
    ja_possui_especialidade = any(
        c.paciente == paciente_logado
        and c.especialidade == agenda_selecionada.especialidade
        and c.status == "Agendada"
        for c in base_consultas
    )

    if ja_possui_especialidade:
        print(f"\n[ERRO] RN3.1: Você já possui uma consulta ativa para "
              f"{agenda_selecionada.especialidade}!")
        return

    # F3: ocupa a vaga e cria a consulta guardando a referência da agenda
    agenda_selecionada.ocupar()
    nova_id = len(base_consultas) + 1
    nova_consulta = Consulta(
        nova_id,
        agenda_selecionada.horario,
        "Agendada",
        agenda_selecionada.especialidade,
        paciente_logado,
        unidade_selecionada,
        agenda_selecionada  # referência guardada para F4 poder liberar a vaga
    )
    base_consultas.append(nova_consulta)
    print(f"\n[SUCESSO] Consulta de {agenda_selecionada.especialidade} "
          f"agendada para {agenda_selecionada.horario}!")


def cancelar_consulta(paciente_logado):
    """F4 + RN4.1: cancela consulta com mínimo 24h de antecedência e libera a vaga."""
    mostrar_consulta(paciente_logado)

    try:
        escolha = int(input("\nDigite o ID da consulta que deseja cancelar: "))
    except ValueError:
        print("ID inválido.")
        return

    # F4: encontra a consulta e chama cancelar() — a própria Consulta libera a vaga
    encontrada = False
    for c in base_consultas:
        if c.id_consulta == escolha and c.paciente == paciente_logado:
            if c.status != "Agendada":
                print(f"[ERRO] Esta consulta já está com status '{c.status}' e não pode ser cancelada.")
            else:
                c.cancelar()
            encontrada = True
            break

    if not encontrada:
        print("Consulta não encontrada.")


def exibir_menu_paciente(paciente_logado):
    while True:
        print("\n" + "=" * 30)
        print("SISTEMA DO PACIENTE")
        print("=" * 30)
        print("1. Agendar consulta")
        print("2. Cancelar consulta")
        print("3. Reagendar consulta")
        print("4. Exibir consultas")
        print("0. Sair")
        print("=" * 30)

        escolha = input("\nDigite sua opção: ")

        if escolha == "1":
            escolher_unidade_saude(paciente_logado)
        elif escolha == "2":
            cancelar_consulta(paciente_logado)
        elif escolha == "3":
            escolher_unidade_saude(paciente_logado)
        elif escolha == "4":
            mostrar_consulta(paciente_logado)
        elif escolha == "0":
            print("\nSaindo.")
            break
        else:
            print("Opção inválida. Tente novamente.")


def exibir_menu_funcionario(funcionario_logado):
    while True:
        print("\n" + "=" * 30)
        print("SISTEMA DO FUNCIONÁRIO")
        print("=" * 30)
        print("1. Configurar profissionais")
        print("2. Confirmar presença")
        print("0. Sair")
        print("=" * 30)

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print("\n" + "=" * 30)
            for a in agendas_disponiveis:
                status_vaga = "Disponível" if a.disponivel else "Ocupada"
                print(f"  ID: {a.id} | {a.unidade.nome} | {a.especialidade} | "
                      f"{a.profissional} | {a.horario} | {status_vaga}")

            try:
                escolha_agenda = int(input("Digite o ID da agenda: "))
                data = input("Digite a nova data (dd/mm/yyyy): ")
                for ad in agendas_disponiveis:
                    if ad.id == escolha_agenda:
                        ad.configurar_horario(data)
            except ValueError:
                print("ID inválido.")

        elif escolha == "2":
            for b in base_consultas:
                print(f"  ID: {b.id_consulta} | Paciente: {b.paciente.nome} "
                      f"| Data: {b.data_hora} | Status: {b.status}")

            try:
                escolha_consulta = int(input("Digite o ID da consulta para confirmar presença: "))
                for b in base_consultas:
                    if b.id_consulta == escolha_consulta:
                        funcionario_logado.registrar_presenca(b)
            except ValueError:
                print("ID inválido.")

        elif escolha == "0":
            print("Saindo.")
            break
        else:
            print("Opção inválida. Tente novamente.")


def exibir_menu_principal():
    print("\n" + "=" * 30)
    print("SISTEMA DE AGENDAMENTO - MENU PRINCIPAL")
    print("=" * 30)
    print("1. Login")
    print("2. Cadastrar-se")
    print("0. Sair")
    print("=" * 30)


# --- Loop principal ---

while True:
    exibir_menu_principal()
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        cpf_digitado = input("CPF: ")
        senha_digitada = input("Senha: ")
        usuario_encontrado = next(
            (u for u in base_usuarios if u.cpf == cpf_digitado), None
        )

        if usuario_encontrado is None:
            print("Erro: Usuário não encontrado.")
        elif usuario_encontrado.realizar_login(cpf_digitado, senha_digitada):
            print(f"\nBem-vindo(a), {usuario_encontrado.nome}!")

            if isinstance(usuario_encontrado, Administrador):
                exibir_menu_admin()
            elif isinstance(usuario_encontrado, Paciente):
                exibir_menu_paciente(usuario_encontrado)
            elif isinstance(usuario_encontrado, Funcionario):
                exibir_menu_funcionario(usuario_encontrado)
        else:
            print("Erro: Senha incorreta.")

    elif escolha == "2":
        cadastrar_paciente()

    elif escolha == "0":
        print("Encerrando o sistema. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")
