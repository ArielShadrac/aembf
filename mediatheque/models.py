from django.db import models

# Create your models here.

class Media(models.Model):
    image = models.ImageField('Images du media (au moins une image representative)', blank=True, upload_to="mediathèque")
    titre = models.CharField('titre et descripton du media', blank=False, max_length=255)
    link = models.URLField('Lien drive du media', blank=False)

    class Meta:
        ordering = ['titre']

    def __str__(self):
        return self.titre