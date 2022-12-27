"""
Script para popular o banco de dados com dados fictícios de clientes.

Rodar esse script na raiz do projeto.
"""
import random
from validate_docbr import CPF
from faker import Faker
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()


def criando_pessoas(quantidade_de_pessoas):
    from clientes.models import Cliente

    fake = Faker('pt_BR')
    for _ in range(quantidade_de_pessoas):
        cpf = CPF()
        nome = fake.name()
        email = '{}@{}'.format(nome.lower(), fake.free_email_domain())
        email = email.replace(' ', '')
        cpf = cpf.generate()
        rg = "{}{}{}{}".format(random.randrange(10, 99), random.randrange(
            100, 999), random.randrange(100, 999), random.randrange(0, 9))
        celular = "{} 9{}-{}".format(random.randrange(10, 21),
                                     random.randrange(4000, 9999), random.randrange(4000, 9999))
        ativo = random.choice([True, False])
        p = Cliente(nome=nome, email=email, cpf=cpf,
                    rg=rg, celular=celular, ativo=ativo)
        p.save()


criando_pessoas(50)
print('Populate Script - Finalizado com Sucesso!')
