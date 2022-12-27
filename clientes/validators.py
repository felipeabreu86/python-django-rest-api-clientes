import re
from validate_docbr import CPF


def cpf_valido(numero_cpf):
    return CPF().validate(numero_cpf)


def nome_valido(nome):
    return nome.replace(' ', '').isalpha()


def rg_valido(rg):
    modelo = '[0-9]{9}'
    return re.findall(modelo, rg)


def celular_valido(celular):
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    return re.findall(modelo, celular)
