# main.py
from src.administrador import Administrador
from src.paciente import Paciente
from src.consulta import Consulta
from src.unidadeSaude import UnidadeSaude
from src.agenda import Agenda
from src.funcionario import Funcionario
from datetime import date,datetime,timedelta


hoje = datetime.now()
dias_para_marca = hoje + timedelta(days = 2)
# --- Dados de teste ---
admin_teste = Administrador(1, "Diogo", "12377756980", "diogoCarvalho@teste.com", "89012", "diogo4545", "1")
paciente_teste = Paciente(1, "Victor", "12345678910", "victor@teste.com", "1234", "victor123", "123", "17/06/2001", "Joinville")
unidade_teste = UnidadeSaude(1, "Posto Arroz Frito", "Muito Longe de Casa")
consulta_teste = Consulta(1, "27/06/2027", "Agendada", "Odontologia", paciente_teste)
funcionario_teste = Funcionario 

agenda_cardio = Agenda(1, "Dr. Roberto", "Cardiologia", unidade_teste, dias_para_marca.strftime("%d/%m/%Y"))
agenda_odonto = Agenda(2, "Dra. Ana", "Odontologia", unidade_teste, dias_para_marca.strftime("%d/%m/%Y"))

base_usuarios = [admin_teste, paciente_teste]
base_unidades = [unidade_teste]
base_consultas = [consulta_teste]
agendas_disponiveis = [agenda_cardio, agenda_odonto]


# --- Funções auxiliares ---

def mostrar_consulta(paciente_logado):
    print(f"\nConsultas do {paciente_logado.nome}")
    for c in base_consultas:
        if c.paciente == paciente_logado:
            print (f"ID Consulta: [{c.id_consulta}] | Especialidade: {c.especialidade} | Status: {c.status} | Data/Hora: {c.data_hora}")

def cadastrar_paciente():
    id_usuario = input("Digite o ID: ")
    nome = input("Nome: ")
    cpf = input("CPF: ")
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

    novo_paciente = Paciente(id_usuario, nome, cpf, email, telefone, senha, cartao_sus, data_nasc, endereco)
    base_usuarios.append(novo_paciente)
    print("\nPaciente cadastrado com sucesso!")

def exibir_menu_admin():
    while True:
        print("\n" + "=" * 30)
        print("SISTEMA DE AGENDAMENTO - ADMINISTRADOR")
        print("=" * 30)
        print("1. Cadastrar nova unidade de saúde")
        print("2. Cadastrar paciente")
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

        elif escolha == "0":
            break

        else:
            print("Opção inválida. Tente novamente.")

def escolher_unidade_saude(paciente_logado):
        print("\n" + "=" * 30)
        print("Escolha uma unidade de saúde:")
        print("=" * 30)

        for unidade in base_unidades:
            print(f"[{unidade.id}] {unidade.nome} | Endereço: {unidade.endereco}")

        id_escolhido = input("\nDigite o ID da unidade desejada: ")
        unidade_selecionada = None

        for unidade in base_unidades:
            if str(unidade.id) == id_escolhido:
                unidade_selecionada = unidade
                break

        if unidade_selecionada is None:
            print("Unidade não encontrada.")
            return

        print(f"\nVagas disponíveis em {unidade_selecionada.nome}:")
        agendas_da_unidade = [a for a in agendas_disponiveis if a.unidade == unidade_selecionada]

        if not agendas_da_unidade:
            print("Nenhuma vaga disponível nesta unidade no momento.")
            return

        for agenda in agendas_da_unidade:
            print(f"[{agenda.id}] {agenda.especialidade} com {agenda.profissional} - {agenda.horario}")

        id_agenda_escolhida = input("\nDigite o ID da vaga que deseja agendar: ")
        agenda_selecionada = None

        for agenda in agendas_da_unidade:
            if str(agenda.id) == id_agenda_escolhida:
                agenda_selecionada = agenda
                break

        if agenda_selecionada is None:
            print("ID da vaga não encontrado.")
            return

        ja_possui_especialidade = any(
            c.paciente == paciente_logado
            and c.especialidade == agenda_selecionada.especialidade
            and c.status == "Agendada"
            for c in base_consultas
        )

        if ja_possui_especialidade:
            print(f"\n[ERRO] Você já possui uma consulta ativa para {agenda_selecionada.especialidade}!")
            return

        nova_id = len(base_consultas) + 1
        nova_consulta = Consulta(nova_id, agenda_selecionada.horario, "Agendada", agenda_selecionada.especialidade, paciente_logado)
        base_consultas.append(nova_consulta)
        print(f"\n[SUCESSO] Consulta de {agenda_selecionada.especialidade} agendada para {agenda_selecionada.horario}!")

def cancelar_consulta(paciente_logado):
    lista_nova_temporaria = []
    mostrar_consulta(paciente_logado)
    
    escolha = int(input("\nDigite o ID da consulta que você quer cancelar: "))
    
    for b in base_consultas:
        if b.id_consulta == escolha:
            b.cancelar()
            break
        
        print("Nenhuma ID Encontrada sua")
        
def exibir_menu_paciente(paciente_logado):
    while True:
        print("\n" + "=" * 30)
        print("SISTEMA DE PACIENTE")
        print("=" * 30)
        print("1. Agendar Consulta")
        print("2. Cancelar Consulta")
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
            print("\nSaindo")
            break
        
 

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
        usuario_encontrado = None

        for usuario in base_usuarios:
            if usuario.cpf == cpf_digitado:
                usuario_encontrado = usuario
                break

        if usuario_encontrado is None:
            print("Erro: Usuário não encontrado.")
        elif usuario_encontrado.realizar_login(cpf_digitado, senha_digitada):
            print(f"\nBem-vindo(a), {usuario_encontrado.nome}!")

            if isinstance(usuario_encontrado, Administrador):
                exibir_menu_admin()
            elif isinstance(usuario_encontrado, Paciente):
                exibir_menu_paciente(usuario_encontrado)
        else:
            print("Erro: Senha incorreta.")

    elif escolha == "2":
        cadastrar_paciente()

    elif escolha == "0":
        print("Encerrando o sistema. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")
