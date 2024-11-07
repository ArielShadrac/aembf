from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.

class Actualité(models.Model):
    title = models.CharField("Titre de l'évènement",max_length=100, blank=False)
    content =RichTextField("Contenu (Veillez à bien rediger et structurer l'article) :")
    image = models.ImageField("Image de l'évènement", blank=True, upload_to='actu')
    files = models.FileField("Fichier associé (Pdf, Images, vidéo, etc)",blank=True,upload_to='actu/')
    link = models.URLField("Lien de l'évènement",blank=True)
    creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-creation']
        indexes = [
            models.Index(fields=['-creation']),
        ]

    def __str__(self):
        return self.title

class Scope(models.Model):
    image = models.ImageField("Image de l'évènement", blank=False, upload_to='comité/scope')


class Scome(models.Model):
    image = models.ImageField("Image de l'évènement", blank=False, upload_to='comité/scome')


class Scoph(models.Model):
    image = models.ImageField("Image de l'évènement", blank=False, upload_to='comité/scoph')


class Score(models.Model):
    image = models.ImageField("Image de l'évènement", blank=False, upload_to='comité/score')


class Scorp(models.Model):
    image = models.ImageField("Image de l'évènement", blank=True, upload_to='comité/scorp')


class Scora(models.Model):
    image = models.ImageField("Image de l'évènement", blank=False, upload_to='comité/scora')
