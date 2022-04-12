from django.contrib import admin
from .models import Prefix, Records


@admin.register(Prefix)
class PrefixAdmin(admin.ModelAdmin):
    list_display = ("prefix", "prefix_len")


@admin.register(Records)
class RecordsAdmin(admin.ModelAdmin):
    list_display = ("prefix", "address", "date")
