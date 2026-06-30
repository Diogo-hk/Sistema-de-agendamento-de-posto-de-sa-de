# tests/test_usuario.py
import unittest
from unittest.mock import patch
from src.usuario import Usuario


class TestUsuario(unittest.TestCase):

    def setUp(self):
        self.usuario = Usuario(1, "Victor", "12345678910", "victor@teste.com","47999999999", "senha123")

    def test_login_com_credenciais_corretas(self):
        resultado = self.usuario.realizar_login("12345678910", "senha123")
        self.assertTrue(resultado)

    def test_login_zera_tentativas_apos_sucesso(self):
        self.usuario.realizar_login("12345678910", "senha_errada")
        self.assertEqual(self.usuario.tentativas_falhas, 1)
        self.usuario.realizar_login("12345678910", "senha123")
        self.assertEqual(self.usuario.tentativas_falhas, 0)

    def test_login_com_cpf_incorreto(self):
        resultado = self.usuario.realizar_login("00000000000", "senha123")
        self.assertFalse(resultado)

    def test_login_com_senha_incorreta(self):
        resultado = self.usuario.realizar_login("12345678910", "senha_errada")
        self.assertFalse(resultado)

    def test_tentativas_falhas_incrementa_a_cada_erro(self):
        self.usuario.realizar_login("12345678910", "errada")
        self.assertEqual(self.usuario.tentativas_falhas, 1)
        self.usuario.realizar_login("12345678910", "errada")
        self.assertEqual(self.usuario.tentativas_falhas, 2)

    @patch("src.usuario.time.sleep", return_value=None)
    def test_bloqueio_apos_cinco_tentativas_falhas(self, mock_sleep):
        """RN2.1: a conta deve recusar login após 5 tentativas incorretas."""
        for _ in range(5):
            self.usuario.realizar_login("12345678910", "senha_errada")

        self.assertEqual(self.usuario.tentativas_falhas, 5)

        resultado = self.usuario.realizar_login("12345678910", "senha123")
        self.assertFalse(resultado, "Login deveria ser recusado mesmo com senha correta após bloqueio")

    @patch("src.usuario.time.sleep", return_value=None)
    def test_quinta_tentativa_aciona_sleep(self, mock_sleep):
        for _ in range(5):
            self.usuario.realizar_login("12345678910", "senha_errada")
        mock_sleep.assert_called_once_with(900)

    def test_propriedade_cpf(self):
        self.assertEqual(self.usuario.cpf, "12345678910")

    def test_propriedade_nome(self):
        self.assertEqual(self.usuario.nome, "Victor")


if __name__ == "__main__":
    unittest.main()
