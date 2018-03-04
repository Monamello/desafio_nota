from django.db import models


class Nota(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    data_cricao = models.DateTimeField(auto_now_add=True, blank=True)
