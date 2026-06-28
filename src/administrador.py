# src/administrador.py
from src.usuario import Usuario
from src.unidadeSaude import UnidadeSaude


class Administrador(Usuario):
    def __init__(self, id_admin, nome, cpf, email, telefone, senha, nivel_acesso):
        super().__init__(id_admin, nome, cpf, email, telefone, senha)
        self._nivel_acesso = nivel_acesso

    def cadastrar_unidade(self, id_unidade, nome, endereco):
        nova_unidade = UnidadeSaude(id_unidade, nome, endereco)
        print("Unidade criada com sucesso.")
        return nova_unidade
