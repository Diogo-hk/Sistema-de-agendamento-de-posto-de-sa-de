import unittest
from src.agenda import Agenda
from src.unidadeSaude import UnidadeSaude


class TestAgenda(unittest.TestCase):

    def setUp(self):
        self.unidade = UnidadeSaude(1, "Posto Central", "Rua A, 100")
        self.agenda = Agenda(1, "Dr. Roberto", "Cardiologia", self.unidade, "Segunda 14:00")

    def test_agenda_inicia_disponivel(self):
        self.assertTrue(self.agenda.disponivel)

    def test_ocupar_marca_como_indisponivel(self):
        self.agenda.ocupar()
        self.assertFalse(self.agenda.disponivel)

    def test_liberar_marca_como_disponivel(self):
        self.agenda.ocupar()
        self.agenda.liberar()
        self.assertTrue(self.agenda.disponivel)

    def test_configurar_horario_atualiza_horario(self):
        self.agenda.configurar_horario("Quarta 09:00")
        self.assertEqual(self.agenda.horario, "Quarta 09:00")

    def test_propriedade_unidade(self):
        self.assertEqual(self.agenda.unidade, self.unidade)

    def test_propriedade_especialidade(self):
        self.assertEqual(self.agenda.especialidade, "Cardiologia")

    def test_propriedade_profissional(self):
        self.assertEqual(self.agenda.profissional, "Dr. Roberto")


if __name__ == "__main__":
    unittest.main()
