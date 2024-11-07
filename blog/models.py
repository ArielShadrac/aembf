from django.db import models
from django.utils import timezone
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class Article(models.Model):
    title = models.CharField('Titre',max_length=500, blank=False)
    resume = models.TextField('Resumé',max_length=500,blank=False)
    created = models.DateTimeField(auto_now_add=True)
    content = RichTextUploadingField("Contenu (Veillez à bien rediger et structurer l'article) :")
    publish = models.DateTimeField('Date de publication', default=timezone.now)
    image = models.ImageField("Image de l'article",blank=False, upload_to='blog/post_image')

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return self.title
