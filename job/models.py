from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.



JOP_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

def image_upload(instance, filename):
    imagename, extension = filename.split('.')
    return "jobs/%s.%s"%(instance.id,extension)

class Jop(models.Model):
    owner = models.ForeignKey(User, related_name="job_owner", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    jop_type  = models.CharField(max_length=15 , choices=JOP_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    Category = models.ForeignKey('Category',on_delete=models.CASCADE)
    image = models.ImageField(upload_to= image_upload)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Jop, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    


class Apply(models.Model):
    job = models.ForeignKey(Jop, related_name='Apply_Job', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email  = models.EmailField(max_length= 100)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=550)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
