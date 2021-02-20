import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pizzaria.settings')
django.setup()

from faker import Faker
from validate_docbr import CPF
import requests
from cliente.models import *
from cliente.models import Endereco, Cliente
from random import choices, randint


def criando_cliente(quantidade):
    fake = Faker(['fr_FR', 'pt_PT', 'it_IT', 'en_US', 'pt_BR'])
    for _ in range(quantidade):
        gerador_cpf = CPF()
        nome = fake.name()
        cpf = gerador_cpf.generate()
        endereco = Endereco.objects.all()[randint(0, Endereco.objects.count())]
        obj = Cliente.objects.create(nome=nome, cpf=cpf, endereco=endereco)
        obj.save()
    print(f'Objetos criados com sucesso!')


def criando_enderecos(quantidade):
    ceps = ['04735000', '02443102', '02763085', '05343010', '04550004', '04826410',
            '04826410', '02764080', '04824110', '05873277', '04844220']
    cont = 0
    for _ in range(quantidade):
        cep = choices(ceps)[0]

        request = requests.get(f'http://viacep.com.br/ws/{cep}/json/?')
        if request.status_code == 200:
            print(request.json())
            r = request.json()
            cep = cep
            rua = r['logradouro']
            numero = randint(1, 999)
            complemento = r['complemento']
            bairro = r['bairro']
            cidade = r['localidade']
            uf = r['uf']
            obj = Endereco.objects.create(cep=cep, rua=rua, numero=numero, complemento=complemento,
                                          bairro=bairro, cidade=cidade, uf=uf)
            obj.save()
        else:
            cont += 1
    print(f'A requisição falhou {cont} vezes.')
# criando_enderecos(40)
criando_cliente(50)