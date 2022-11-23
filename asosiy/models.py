from django.db import models
from django.contrib.auth.models import User

class Suv(models.Model):
    brend = models.CharField(max_length=50)
    narx = models.PositiveSmallIntegerField()
    litr = models.PositiveSmallIntegerField()
    batafsil = models.CharField(max_length=150)
    def __str__(self):return self.brend

class Mijoz(models.Model):
    ism = models.CharField(max_length=50)
    tel = models.CharField(max_length=13)
    manzil = models.CharField(max_length=100)
    qarz = models.PositiveSmallIntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):return self.ism

class Admin(models.Model):
    ism = models.CharField(max_length=50)
    yosh = models.CharField(max_length=3)
    ish_vaqti = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self): return self.ism

class Haydovchi(models.Model):
    ism = models.CharField(max_length=50)
    tel = models.CharField(max_length=13)
    kiritilgan_sana = models.DateField()
    def __str__(self):return self.ism

class Buyurtma(models.Model):
    suv = models.ForeignKey(Suv, on_delete=models.CASCADE)
    sana = models.DateField()
    mijoz = models.ForeignKey(Mijoz, on_delete=models.CASCADE)
    miqdor = models.PositiveSmallIntegerField()
    umumiy_narxi = models.PositiveSmallIntegerField()
    qabul_qilgan_admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    haydovchi = models.ForeignKey(Haydovchi, on_delete=models.CASCADE)
    def __str__(self):return f"Suv:{self.suv}, mijoz:{self.mijoz}"

