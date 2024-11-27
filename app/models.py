from django.db import models
from django.conf import settings

# Modelo para un favorito
class Favourite(models.Model):
    url = models.URLField(max_length=500)  # Podemos usar URLField para un enlace de URL
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=50)  # Podemos usar CharField para un estado corto (alive, dead, unknown)
    last_location = models.CharField(max_length=200)  # Si es una locación corta podemos usar CharField
    first_seen = models.DateTimeField()  # Podemos usar DateTimeField para fechas y horas

    # Asociamos el favorito con el usuario 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'url')  # Asegura que un usuario solo tenga un favorito con el mismo URL

    # Regresa una cadena con el nombre del personaje guardado como favorito, su estado y tu nombre de usuario 
    def __str__(self):
        return f"{self.name} - {self.status} - {self.user.username}"
