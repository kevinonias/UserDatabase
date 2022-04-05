from django.db import models
from Empresa.models import Company


class ASN(models.Model):
    _as_number = models.PositiveIntegerField("ASN")
    company = models.ForeignKey(Company, verbose_name="Company", on_delete=models.CASCADE)

    class Meta:
        ordering = ["_as_number"]

    @property
    def asn_number(self):
        return f"AS{self._as_number}"
