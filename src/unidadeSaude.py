# src/unidadeSaude.py


class UnidadeSaude:
    def __init__(self, id_unidade, nome, endereco):
        self.__id = id_unidade
        self.__nome = nome
        self.__endereco = endereco

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def endereco(self):
        return self.__endereco

    def atualizar_dados(self):
        pass
