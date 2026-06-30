from src.usuario import Usuario


class Funcionario(Usuario):
    def __init__(self, id_funcionario, nome, cpf, email, telefone, senha, matricula, cargo):
        super().__init__(id_funcionario, nome, cpf, email, telefone, senha)
        self._matricula = matricula
        self._cargo = cargo

    def registrar_presenca(self, consulta):
        consulta.confirmar()
        print("Presença confirmada")
