# src/usuario.py
import time


class Usuario:
    def __init__(self, id_usuario, nome, cpf, email, telefone, senha_hash):
        self.__id = id_usuario
        self.__nome = nome
        self.__cpf = cpf
        self.__email = email
        self.__telefone = telefone
        self.__senha_hash = senha_hash
        self.__tentativas = 0

    @property
    def cpf(self):
        return self.__cpf

    @property
    def nome(self):
        return self.__nome

    @property
    def tentativas_falhas(self):
        return self.__tentativas

    def realizar_login(self, cpf_digitado, senha_digitada):
        if self.__tentativas >= 5:
            print("Conta bloqueada! Aguarde 15 minutos.")
            return False

        if self.__cpf == cpf_digitado and self.__senha_hash == senha_digitada:
            self.__tentativas = 0
            return True

        self.__tentativas += 1

        if self.__tentativas == 5:
            print(f"Senha incorreta! Tentativa {self.__tentativas} de 5. Aguarde 15 minutos.")
            time.sleep(900)
        else:
            print(f"Senha incorreta! Tentativa {self.__tentativas} de 5.")

        return False
