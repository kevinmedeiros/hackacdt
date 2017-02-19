from django.db import models


class CredCard(models.Model):
    name = models.CharField(max_length=100, blank=False)
    vale_date = models.CharField(max_length=5, blank=False)
    number = models.CharField(max_length=16, blank=False)
    cvv = models.CharField(max_length=3, blank=False)

    def __str__(self):
        return self.name


class BankAccount(models.Model):
    name = models.CharField(max_length=100, blank=False)
    cpf = models.CharField(max_length=11, blank=False)
    bank = models.CharField(max_length=50, blank=False)
    agency = models.CharField(max_length=10, blank=False)
    account = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.name


class Address(models.Model):
    zip_code = models.CharField(max_length=8, blank=False)
    street = models.CharField(max_length=100, blank=False)
    address_number = models.IntegerField(max_length=20)
    neighborhood = models.CharField(max_length=100)
    typ_uf = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernanbuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    )
    uf = models.CharField(max_length=2, choices=typ_uf, verbose_name='UF', default='PB')
    city = models.CharField(max_length=100, default='João Pessoa')

    def __str__(self):
        return self.zip_code


class Company(models.Model):
    Address = models.ForeignKey(Address)
    social_name = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)
    fone = models.CharField(max_length=12)
    bank_account = models.ForeignKey(BankAccount)

    def __str__(self):
        return self.social_name


class Buyer(models.Model):
    name = models.CharField(max_length=100)
    address = models.ForeignKey(Address)
    cred_card = models.ForeignKey(CredCard)

    def __str__(self):
        return self.name

