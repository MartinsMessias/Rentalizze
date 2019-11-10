from django.db import models
import datetime
from django.core.validators import MinValueValidator, MaxValueValidator


STATUS_CHOICES = (('A', 'Ativo'), ('I', 'Inativo'))

class Cliente(models.Model):
    nome_cliente = models.CharField(max_length=200)
    cpf_cliente = models.CharField(max_length=20, unique=True, default='---')
    telefone_cliente = models.CharField(max_length=20)
    email_cliente = models.CharField(max_length=120)
    rg_cliente = models.CharField(max_length=50)
    cnpj_cliente = models.CharField(max_length=50, unique=True, default='---')
    cnh_cliente = models.CharField(max_length=100)
    validade_cnh = models.DateField(max_length=50)
    criado_em = models.DateTimeField(auto_now=True)
    rua = models.CharField(max_length=200)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=200)
    cep = models.CharField(max_length=10)
    bairro = models.CharField(max_length=200)
    estado = models.CharField(max_length=2)
    cidade = models.CharField(max_length=200)
    modificado_em = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=6, choices=STATUS_CHOICES)

    def __str__(self):
        return self.nome_cliente

class Locacao(models.Model):
    dt_hora_locacao = models.CharField(max_length=50)
    dt_hora_devolucao = models.CharField(max_length=50)
    quilometragem = models.FloatField()
    valor_locacao = models.DecimalField(max_digits=6, decimal_places=2)
    # usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    automovel = models.ForeignKey('Automovel', on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now=True)
    modificacado_em = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return self.cliente


class Automovel(models.Model):
    COMBUSTIVEL_CHOICES = (
        ('Gasolina', 'Gasolina'),
    )
    placa_automovel = models.CharField(max_length=15)
    cor_automovel = models.CharField(max_length=20)
    nro_portas_automovel = models.IntegerField()
    tipo_combustivel_automovel = models.CharField(max_length=20, choices=COMBUSTIVEL_CHOICES)
    quilometragem_automovel = models.FloatField()
    chassi_automovel = models.IntegerField()
    valor_locacao = models.DecimalField(max_digits=6, decimal_places=2)
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    ano = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(datetime.datetime.now().year)],
        help_text="Informe um ano válido!")
    criado_em = models.DateTimeField(auto_now=True)
    categoria = models.CharField(max_length=200)
    valor_diario = models.DecimalField(max_digits=6, decimal_places=2)
    modificacado_em = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)


    def __str__(self):
        return self.modelo
