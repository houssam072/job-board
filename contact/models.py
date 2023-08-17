from django.db import models

# Create your models here.

class Info(models.Model):
    place = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)

    class Meta:
        verbose_name = ("info")
        verbose_name_plural = ("infos")

    def __str__(self):
        return self.email