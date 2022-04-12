from django.contrib import admin
from .models import ASN


@admin.register(ASN)
class ASNAdmin(admin.ModelAdmin):
    list_display = ("as_number", "company")
