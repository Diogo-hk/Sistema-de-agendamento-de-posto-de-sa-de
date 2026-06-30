# src/unidadeSaude.py


class UnidadeSaude:
    def __init__(self, id_unidade, nome, endereco):
        self.__id = id_unidade
        self.__nome = nome
        self.__endereco = endereco
        self.__ativa = True

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def endereco(self):
        return self.__endereco

    @property
    def ativa(self):
        return self.__ativa

    def atualizar_dados(self, novo_nome=None, novo_endereco=None):
        if novo_nome:
            self.__nome = novo_nome
        if novo_endereco:
            self.__endereco = novo_endereco
        print("Dados da unidade atualizados com sucesso.")

    def desativar(self):
        self.__ativa = False
        print(f"Unidade '{self.__nome}' desativada com sucesso.")
