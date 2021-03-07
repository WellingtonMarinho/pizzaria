import factory
from factory.django import DjangoModelFactory
from cliente.models import Endereco, Cliente

faker = factory.faker.faker.Faker(['pt_BR'])

class EnderecoFactory(DjangoModelFactory):
    cep = factory.Faker('postcode')
    rua = factory.Faker('street_name')
    numero = factory.Faker('building_number')
    bairro = factory.Faker('bairro')
    cidade = factory.Faker('city')
    uf = factory.Faker('estado_sigla')

    class Meta:
        model = Endereco


class ClienteFactory(DjangoModelFactory):
    nome = factory.Faker('name')
    cpf = factory.Faker('cpf')
    endereco = factory.SubFactory(EnderecoFactory)
    telefone = factory.Faker('phone_number')

    class Meta:
        model = Cliente
