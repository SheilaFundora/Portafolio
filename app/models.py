from django.db import models

# Create your models here.
class Persona(models.Model):
    speciality = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    birthday = models.CharField(max_length=255)
    remote = models.BooleanField()
    freelance = models.BooleanField()
    img = models.ImageField(upload_to='persona')

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

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

class Sumary(models.Model):
    description = models.TextField()

class Project(models.Model):
    title = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    description = models.TextField()

class ProectTech(models.Model):
    tech = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.TextField()

class Experience(models.Model):
    ocupation = models.CharField(max_length=255)
    center = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

class ExperienceDetails(models.Model):
    description = models.CharField(max_length=255)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)

class Education(models.Model):
    school = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    title = models.TextField()

class EducationsDetails(models.Model):
    education = models.ForeignKey(Education, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

class Awards(models.Model):
    education = models.ForeignKey(Education, on_delete=models.CASCADE)
    awards = models.TextField()

class Categories(models.Model):
    category = models.CharField(max_length=255)

class Portafolio(models.Model):
    name = models.CharField(max_length=255)
    client = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date = models.DateField()
    img = models.ImageField(upload_to='project')


class PortafolioIMG(models.Model):
    portafolio = models.ForeignKey(Portafolio, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='project')

class Services(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icono = models.CharField(max_length=255)

class Contacto(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()
    # estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
