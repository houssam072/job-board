from django.db import models

# Create your models here.



JOP_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

class Jop(models.Model):
    title = models.CharField(max_length=100)
    jop_type  = models.CharField(max_length=15 , choices=JOP_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)

    def __str__(self):
        return self.title
