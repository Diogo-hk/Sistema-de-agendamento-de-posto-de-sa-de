class Agenda:
    def __init__(self, id_agenda, profissional, especialidade, unidade, dias_disponiveis):
        self.__id = id_agenda
        self.__profissional = profissional
        self.__especialidade = especialidade
        self.__unidade = unidade
        self.__dias_disponiveis = dias_disponiveis
        self.__disponivel = True

    @property
    def id(self):
        return self.__id

    @property
    def unidade(self):
        return self.__unidade

    @property
    def especialidade(self):
        return self.__especialidade

    @property
    def profissional(self):
        return self.__profissional

    @property
    def horario(self):
        return self.__dias_disponiveis

    @property
    def disponivel(self):
        return self.__disponivel

    def ocupar(self):
        self.__disponivel = False

    def liberar(self):
        self.__disponivel = True

    def configurar_horario(self, data):
        self.__dias_disponiveis = data
        print("Data alterada com sucesso.")

    def bloquear_periodo(self):
        pass
