from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.


class Protocol(models.Model):
    title = models.CharField('Titre',blank=False, max_length=350)
    created = models.DateTimeField(auto_now_add=True)
    publish = models.DateTimeField('Date de publication', default=timezone.now)
    resume = models.TextField("Resumé de l'article :", blank=False)
    content = RichTextField("Contenu (Veillez à bien rediger et structurer l'article) :", blank=False)
    image = models.ImageField('Image',blank=False, upload_to="protocol/")
    source = models.TextField(blank=True)

    class Meta():
        ordering = ['-created']

    def __str__(self):
        return self.title
    
