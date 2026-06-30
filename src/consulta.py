# src/consulta.py
from datetime import date, datetime


class Consulta:
    def __init__(self, id_consulta, data_hora, status, especialidade, paciente,
                 unidade=None, agenda=None):
        self.__id_consulta = id_consulta
        self.__data_hora = data_hora
        self.__status = status
        self.__especialidade = especialidade
        self.__paciente = paciente
        self.__unidade = unidade
        self.__agenda = agenda

    @property
    def id_consulta(self):
        return self.__id_consulta

    @property
    def data_hora(self):
        return self.__data_hora

    @property
    def paciente(self):
        return self.__paciente

    @property
    def especialidade(self):
        return self.__especialidade

    @property
    def status(self):
        return self.__status

    @property
    def unidade(self):
        return self.__unidade

    def confirmar(self):
        self.__status = "Presente"

    def cancelar(self):
        data_hoje = date.today()
        data_para_comparar = datetime.strptime(self.__data_hora, "%d/%m/%Y").date()

        dias_restantes = (data_para_comparar - data_hoje).days

        if dias_restantes <= 1:
            print("[ERRO] RN4.1: Não é possível cancelar com menos de 24h de antecedência.")
        else:
            self.__status = "Cancelada"
            if self.__agenda is not None:
                self.__agenda.liberar()
            print("[SUCESSO] Consulta cancelada. A vaga foi liberada.")

    def reagendar(self):
        self.__status = "Reagendado"

    def verificar_prioridade(self):
        pass
