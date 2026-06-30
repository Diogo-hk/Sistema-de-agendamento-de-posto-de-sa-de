import unittest
from src.paciente import Paciente
from src.administrador import Administrador
from src.funcionario import Funcionario
from src.consulta import Consulta
from src.unidadeSaude import UnidadeSaude


class TestPaciente(unittest.TestCase):

    def setUp(self):
        self.paciente = Paciente(1, "Victor", "12345678910", "victor@teste.com","1234", "victor123", "123", "17/06/2001", "Joinville")

    def test_atributos_especificos(self):
        self.assertEqual(self.paciente.cartao_sus, "123")
        self.assertEqual(self.paciente.data_nasc, "17/06/2001")
        self.assertEqual(self.paciente.endereco, "Joinville")

    def test_heranca_login_funciona(self):
        self.assertTrue(self.paciente.realizar_login("12345678910", "victor123"))

    def test_heranca_propriedade_nome(self):
        self.assertEqual(self.paciente.nome, "Victor")


class TestAdministrador(unittest.TestCase):

    def setUp(self):
        self.admin = Administrador(1, "Diogo", "12377756980", "diogo@teste.com","89012", "diogo4545", "1")

    def test_cadastrar_unidade_retorna_objeto_unidade(self):
        unidade = self.admin.cadastrar_unidade(10, "Posto Central", "Rua A, 100")
        self.assertIsInstance(unidade, UnidadeSaude)

    def test_cadastrar_unidade_preserva_dados(self):
        unidade = self.admin.cadastrar_unidade(10, "Posto Central", "Rua A, 100")
        self.assertEqual(unidade.id, 10)
        self.assertEqual(unidade.nome, "Posto Central")
        self.assertEqual(unidade.endereco, "Rua A, 100")

    def test_heranca_login_funciona(self):
        self.assertTrue(self.admin.realizar_login("12377756980", "diogo4545"))


class TestFuncionario(unittest.TestCase):

    def setUp(self):
        self.funcionario = Funcionario(1, "Rafael", "12345678980", "rafael@teste.com","3123123", "1234", "12345678", "Recepcionista")
        self.paciente = Paciente(2, "Victor", "98765432100", "victor@teste.com","1234", "senha", "123", "17/06/2001", "Joinville")
        self.consulta = Consulta(1, "01/01/2030", "Agendada", "Cardiologia", self.paciente)

    def test_registrar_presenca_confirma_status_da_consulta(self):
        self.funcionario.registrar_presenca(self.consulta)
        self.assertEqual(self.consulta.status, "Presente")

    def test_heranca_login_funciona(self):
        self.assertTrue(self.funcionario.realizar_login("12345678980", "1234"))


if __name__ == "__main__":
    unittest.main()
