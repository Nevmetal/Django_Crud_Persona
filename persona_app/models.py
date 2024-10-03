from django.db import models

# Create your models here.
class Persona(models.Model):
    id = models.AutoField(primary_key=True)  
    CI = models.CharField(max_length=10, unique=True)  
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'