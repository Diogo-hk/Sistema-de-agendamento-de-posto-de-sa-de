# tests/test_unidade_saude.py
import unittest
from src.unidadeSaude import UnidadeSaude


class TestUnidadeSaude(unittest.TestCase):

    def setUp(self):
        self.unidade = UnidadeSaude(1, "Posto Central", "Rua A, 100")

    def test_unidade_inicia_ativa(self):
        self.assertTrue(self.unidade.ativa)

    def test_desativar_marca_como_inativa(self):
        self.unidade.desativar()
        self.assertFalse(self.unidade.ativa)

    def test_atualizar_dados_altera_nome(self):
        self.unidade.atualizar_dados(novo_nome="Posto Novo Nome")
        self.assertEqual(self.unidade.nome, "Posto Novo Nome")

    def test_atualizar_dados_altera_endereco(self):
        self.unidade.atualizar_dados(novo_endereco="Rua B, 200")
        self.assertEqual(self.unidade.endereco, "Rua B, 200")

    def test_atualizar_dados_sem_argumentos_mantem_valores(self):
        self.unidade.atualizar_dados()
        self.assertEqual(self.unidade.nome, "Posto Central")
        self.assertEqual(self.unidade.endereco, "Rua A, 100")

    def test_propriedade_id(self):
        self.assertEqual(self.unidade.id, 1)


if __name__ == "__main__":
    unittest.main()
