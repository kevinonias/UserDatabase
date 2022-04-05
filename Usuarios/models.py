from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import MaxValueValidator, MinValueValidator

from Empresa.models import Company

class UsuarioManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('O username é obrigatório')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_staff' is not True):
            raise ValueError('Superuser precisa ter staff True')

        if extra_fields.get('is_superuser' is not True):
            raise ValueError('Superuser precisa ter superuser True')

        return self._create_user(username, password, **extra_fields)


class Usuarios(AbstractUser):
    email = models.EmailField('E-mail', unique=True)
    phone = models.CharField('Phone', max_length=15, blank=True)
    is_staff = models.BooleanField('Staff Member', default=False)
    role = models.CharField("Role", max_length=15)
    billing_cycle = models.PositiveIntegerField("Billing Cycle", validators=[
        MaxValueValidator(31),
        MinValueValidator(1)])
    _asnumber = models.PositiveIntegerField("Main ASN", unique=True)

    company = models.ForeignKey(Company, verbose_name="Company", on_delete=models.CASCADE, blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name']

    def __str__(self):
        return self.username

    @property
    def asnumber(self):
        return f"AS{self._asnumber}"

    objects = UsuarioManager()
