from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class MyUserManager(BaseUserManager):
    def _create_user(self, number, password, **extra_fields):
        if not number:
            raise ValueError("Вы не ввели Номер телефона")
        user = self.model(
            number=number,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,number, password):
        return self._create_user(number, password)

    # Делаем метод для создание админа сайта
    def create_superuser(self, number, password):
        return self._create_user(number, password,full_name="admin", is_staff=True, is_superuser=True)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)
    number = models.CharField(max_length=11, unique=True)
    avatar = models.ImageField()
    full_name = models.CharField(max_length=255)
    city = models.CharField(max_length=170)
    tel_number_relatives = models.IntegerField(blank=True, null=True)
    name_relatives = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    location_access = models.BooleanField(blank=True, default=False)
    role = models.ForeignKey('Roles', on_delete=models.PROTECT, null=True)
    balance = models.IntegerField(default=0)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'number'
    REQUIRED_FIELDS = []

    objects = MyUserManager()

    # Метод для отображения в админ панели
    def __str__(self):
        return self.full_name

class Roles(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
