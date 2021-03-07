import factory
from factory.django import DjangoModelFactory
from cliente.models import Endereco, Cliente

faker = factory.faker.faker.Faker(['pt_BR'])
# factory.Faker = factory.Faker(locale='pt_BR')

class EnderecoFactory(DjangoModelFactory):
    cep = factory.Faker('postcode', locale='pt_BR')
    rua = factory.Faker('street_name', locale='pt_BR')
    numero = factory.Faker('building_number', locale='pt_BR')
    bairro = factory.Faker('bairro', locale='pt_BR')
    cidade = factory.Faker('city', locale='pt_BR')
    uf = factory.Faker('estado_sigla', locale='pt_BR')

    class Meta:
        model = Endereco


class ClienteFactory(DjangoModelFactory):
    nome = factory.Faker('name', locale='pt_BR')
    cpf = factory.Faker('cpf', locale='pt_BR')
    endereco = factory.SubFactory(EnderecoFactory)
    telefone = factory.Faker('phone_number', locale='pt_BR')

    class Meta:
        model = Cliente
