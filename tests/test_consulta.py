import unittest
from datetime import date, timedelta
from src.consulta import Consulta
from src.paciente import Paciente
from src.agenda import Agenda
from src.unidadeSaude import UnidadeSaude


class TestConsulta(unittest.TestCase):

    def setUp(self):
        self.paciente = Paciente(1, "Victor", "12345678910", "victor@teste.com",
                                  "1234", "senha", "123", "17/06/2001", "Joinville")
        self.unidade = UnidadeSaude(1, "Posto Central", "Rua A, 100")
        self.agenda = Agenda(1, "Dra. Ana", "Odontologia", self.unidade, "Terça 15:00")

        data_futura = (date.today() + timedelta(days=10)).strftime("%d/%m/%Y")
        self.consulta_futura = Consulta(1, data_futura, "Agendada", "Odontologia",
                                         self.paciente, self.unidade, self.agenda)

    def test_confirmar_altera_status_para_presente(self):
        self.consulta_futura.confirmar()
        self.assertEqual(self.consulta_futura.status, "Presente")

    def test_cancelar_com_mais_de_24h_de_antecedencia(self):
        self.consulta_futura.cancelar()
        self.assertEqual(self.consulta_futura.status, "Cancelada")

    def test_cancelar_libera_vaga_na_agenda(self):
        self.agenda.ocupar()
        self.assertFalse(self.agenda.disponivel)

        self.consulta_futura.cancelar()

        self.assertTrue(self.agenda.disponivel)

    def test_cancelar_com_menos_de_24h_de_antecedencia_e_bloqueado(self):
        data_amanha = (date.today() + timedelta(days=1)).strftime("%d/%m/%Y")
        consulta_proxima = Consulta(2, data_amanha, "Agendada", "Cardiologia", self.paciente, self.unidade, self.agenda)

        consulta_proxima.cancelar()

        self.assertEqual(consulta_proxima.status, "Agendada","Status não deveria mudar quando o cancelamento é bloqueado pela RN4.1")

    def test_cancelar_consulta_de_hoje_e_bloqueado(self):
        data_hoje = date.today().strftime("%d/%m/%Y")
        consulta_hoje = Consulta(3, data_hoje, "Agendada", "Cardiologia", self.paciente, self.unidade, self.agenda)

        consulta_hoje.cancelar()

        self.assertEqual(consulta_hoje.status, "Agendada")

    def test_cancelar_sem_agenda_associada_nao_gera_erro(self):
        data_futura = (date.today() + timedelta(days=10)).strftime("%d/%m/%Y")
        consulta_sem_agenda = Consulta(4, data_futura, "Agendada", "Cardiologia", self.paciente)

        consulta_sem_agenda.cancelar()

        self.assertEqual(consulta_sem_agenda.status, "Cancelada")

    def test_reagendar_altera_status(self):
        self.consulta_futura.reagendar()
        self.assertEqual(self.consulta_futura.status, "Reagendado")

    def test_propriedade_paciente(self):
        self.assertEqual(self.consulta_futura.paciente, self.paciente)

    def test_propriedade_unidade(self):
        self.assertEqual(self.consulta_futura.unidade, self.unidade)


if __name__ == "__main__":
    unittest.main()
