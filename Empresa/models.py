from django.db import models


class Company(models.Model):
    razao_social = models.CharField("Razão Social", max_length=200, unique=True)
