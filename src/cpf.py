# src/cpf.py
import re

CPFS_INVALIDOS = {str(d) * 11 for d in range(10)}


def is_cpf_valido(cpf):
    """Retorna True se o CPF no formato brasileiro for válido, False caso contrário."""
    if not isinstance(cpf, str):
        return False

    cpf = re.sub(r"[^0-9]", "", cpf)

    if cpf in CPFS_INVALIDOS:
        return False

    if len(cpf) != 11:
        return False

    soma = sum(int(cpf[n]) * (10 - n) for n in range(9))
    digito = 11 - soma % 11
    primeiro_digito = 0 if digito > 9 else digito

    soma = sum(int(cpf[n]) * (11 - n) for n in range(10))
    digito = 11 - soma % 11
    segundo_digito = 0 if digito > 9 else digito

    return cpf[-2:] == f"{primeiro_digito}{segundo_digito}"


def is_cnpj_valido(cnpj):
    """Retorna True se o CNPJ no formato brasileiro for válido, False caso contrário."""
    if not isinstance(cnpj, str):
        return False

    cnpj = re.sub(r"[^0-9]", "", cnpj)

    if len(cnpj) != 14:
        return False

    pesos_primeiro = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = sum(int(cnpj[n]) * pesos_primeiro[n] for n in range(12))
    resto = soma % 11
    primeiro_digito = 0 if resto < 2 else 11 - resto

    pesos_segundo = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = sum(int(cnpj[n]) * pesos_segundo[n] for n in range(13))
    resto = soma % 11
    segundo_digito = 0 if resto < 2 else 11 - resto

    return cnpj[-2:] == f"{primeiro_digito}{segundo_digito}"
