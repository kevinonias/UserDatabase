from django.db import models
from Empresa.models import Company


class Contrato(models.Model):
    company = models.ForeignKey(Company, verbose_name="Company", on_delete=models.CASCADE)


class Aditivo(models.Model):
    contrato = models.ForeignKey(Contrato, verbose_name="Contrato", on_delete=models.CASCADE)
    company_list = models.ManyToManyField(Company)
