from django.db import models

# Create your models here.
class Tarea(models.Model):
    estados = [('completo','Finalizado'),('incompleto','Pendiente')]
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)
    estado = models.CharField(max_length=50,choices=estados,default='incompleto')
    def __str__(self):
        return self.titulo
    