from django.db import models
from ASN.models import ASN


class Prefix(models.Model):
    asn = models.ForeignKey(ASN, verbose_name="ASN", on_delete=models.CASCADE)
    prefix = models.CharField("Prefix", max_length=18, unique=True)

    class Meta:
        ordering = ["prefix"]

    def __str__(self):
        return self.prefix

    @property
    def prefix_len(self):
        return int(self.prefix[-2:])

    @property
    def network(self):
        return self.prefix[:-3]


class Records(models.Model):
    prefix = models.ForeignKey(Prefix, verbose_name="Prefixo", on_delete=models.CASCADE)
    address = models.CharField("Address", max_length=15)
    _timestamp = models.PositiveIntegerField("Timestamp")
    total_packets = models.PositiveIntegerField("Total Packets")
    min_packets = models.PositiveIntegerField("Min Packets")
    max_packets = models.PositiveIntegerField("Max Packets")
    total_bps = models.PositiveIntegerField("Bips per Second")
    min_bps = models.PositiveIntegerField("Min BPS")
    max_bps = models.PositiveIntegerField("Max BPS")

    class Meta:
        ordering = ["_timestamp"]

    @property
    def date(self):
        return self._timestamp

    @property
    def packets_avg(self):
        self.total_packets / 300
        return

    @property
    def bps_avg(self):
        self.total_bps / 300
        return
