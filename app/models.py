from django.db import models

# Create your models here.
class Persona(models.Model):
    speciality = models.CharField(max_length=255)
    age = models.IntegerField()
    degree = models.CharField(max_length=255)
    phone = models.IntegerField()
    city = models.CharField(max_length=255)
    birthday = models.CharField(max_length=255)
    remote = models.BooleanField()
    freelance = models.BooleanField()

# para el about, el contact ...
class TextDescript(models.Model):
    description = models.TextField()
    ubicacion = models.CharField(max_length=255)


class SocialNetwork(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)


class Skills(models.Model):
    name = models.CharField(max_length=255)
    percent = models.IntegerField()

class Resume(models.Model):
    pass

class Portafolio(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    date = models.DateField()
    client = models.CharField(max_length=255)

class PortafolioIMG(models.Model):
    portafolio = models.ForeignKey(Portafolio, on_delete=models.CASCADE)
    url = models.CharField(max_length=255)

class Services(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()


