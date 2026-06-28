# src/paciente.py
from src.usuario import Usuario


class Paciente(Usuario):
    def __init__(self, id_usuario, nome, cpf, email, telefone, senha_hash,
                 cartao_sus, data_nasc, endereco):
        super().__init__(id_usuario, nome, cpf, email, telefone, senha_hash)
        self.__cartao_sus = cartao_sus
        self.__data_nasc = data_nasc
        self.__endereco = endereco

    @property
    def cartao_sus(self):
        return self.__cartao_sus

    @property
    def data_nasc(self):
        return self.__data_nasc

    @property
    def endereco(self):
        return self.__endereco
