from django.db import models

# Create your models here.


class National(models.Model):
    name = models.TextField('Nom et prenom(s) de membre du bureau', max_length=255, blank=False)
    post = models.TextField('Poste du membre du bureau', max_length=255, blank=False)
    photo = models.ImageField('Photo du membre du bureau', blank=True, upload_to="office/national/")
    link = models.URLField('Lien LinkedIn du membre du bureau', max_length=500, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created']),
        ]

    def __str__(self):
        return self.post

class UJKZ(models.Model):
    name = models.TextField('Nom et prenom(s) de membre du bureau', max_length=255, blank=False)
    post = models.TextField('Poste du membre du bureau', max_length=255, blank=False)
    photo = models.ImageField('Photo du membre du bureau', blank=True, upload_to="office/ujkz/")
    link = models.URLField('Lien LinkedIn du membre du bureau', max_length=500, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created']),
        ]

    def __str__(self):
        return self.post

class USTA(models.Model):
    name = models.TextField('Nom et prenom(s) de membre du bureau', max_length=255, blank=False)
    post = models.TextField('Poste du membre du bureau', max_length=255, blank=False)
    photo = models.ImageField('Photo du membre du bureau', blank=True, upload_to="office/usta/")
    link = models.URLField('Lien LinkedIn du membre du bureau', max_length=500, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created']),
        ]
    def __str__(self):
        return self.post
    
class INSSA(models.Model):
    name = models.TextField('Nom et prenom(s) de membre du bureau', max_length=255, blank=False)
    post = models.TextField('Poste du membre du bureau', max_length=255, blank=False)
    photo = models.ImageField('Photo du membre du bureau', blank=True, upload_to="office/inssa/")
    link = models.URLField('Lien LinkedIn du membre du bureau', max_length=500, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created']),
        ]
    
    def __str__(self):
        return self.post

class UOHG(models.Model):
    name = models.TextField('Nom et prenom(s) de membre du bureau', max_length=255, blank=False)
    post = models.TextField('Poste du membre du bureau', max_length=255, blank=False)
    photo = models.ImageField('Photo du membre du bureau', blank=True, upload_to="office/uohg/")
    link = models.URLField('Lien LinkedIn du membre du bureau', max_length=500, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created']),
        ]

    def __str__(self):
        return self.post    

class USDAO(models.Model):
    name = models.TextField('Nom et prenom(s) de membre du bureau', max_length=255, blank=False)
    post = models.TextField('Poste du membre du bureau', max_length=255, blank=False)
    photo = models.ImageField('Photo du membre du bureau', blank=True, upload_to="office/usdao/")
    link = models.URLField('Lien LinkedIn du membre du bureau', max_length=500, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created']),
        ]

    def __str__(self):
        return self.post

