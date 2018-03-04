from django.db import models


class Nota(models.Model):
    autor = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, null=False)
    titulo = models.CharField(max_length=200, null=False)
    texto = models.TextField(null=False)
    data_cricao = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.titulo
