import unittest
from src.cpf import is_cpf_valido, is_cnpj_valido


class TestIsCpfValido(unittest.TestCase):

    def test_cpf_valido_sem_formatacao(self):
        self.assertTrue(is_cpf_valido("11144477735"))

    def test_cpf_valido_com_formatacao(self):
        self.assertTrue(is_cpf_valido("123.456.789-09"))

    def test_cpf_invalido_digito_verificador_errado(self):
        self.assertFalse(is_cpf_valido("11144477736"))

    def test_cpf_com_todos_digitos_iguais_e_invalido(self):
        self.assertFalse(is_cpf_valido("11111111111"))
        self.assertFalse(is_cpf_valido("00000000000"))

    def test_cpf_com_tamanho_incorreto(self):
        self.assertFalse(is_cpf_valido("123456"))
        self.assertFalse(is_cpf_valido("123456789012"))

    def test_cpf_nao_string_retorna_falso(self):
        self.assertFalse(is_cpf_valido(11144477735))
        self.assertFalse(is_cpf_valido(None))

    def test_cpf_vazio(self):
        self.assertFalse(is_cpf_valido(""))


class TestIsCnpjValido(unittest.TestCase):

    def test_cnpj_com_tamanho_incorreto(self):
        self.assertFalse(is_cnpj_valido("123456"))

    def test_cnpj_nao_string_retorna_falso(self):
        self.assertFalse(is_cnpj_valido(12345678000199))


if __name__ == "__main__":
    unittest.main()
