# src/consulta.py
from datetime import date,datetime

class Consulta:
    def __init__(self, id_consulta, data_hora, status, especialidade, paciente):
        self.__id_consulta = id_consulta
        self.__data_hora = data_hora
        self.__status = status
        self.__especialidade = especialidade
        self.__paciente = paciente

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

    def confirmar(self):
        pass

    def cancelar(self):
        data_hoje = date.today()
        data_Para_Comparar = datetime.strptime(self.__data_hora, "%d/%m/%Y").date()
        
        dias_restantes = (data_Para_Comparar - data_hoje).days
        
        if(dias_restantes <= 1):
            print("Não será possivel cancelar, devido que falta menos de 24hrs")
        else:
            self.__status = "Cancelada"
            print("Alterado com Sucesso")
        

    def reagendar(self):
        self.__status = "Reagendado"

    def verificar_prioridade(self):
        pass
