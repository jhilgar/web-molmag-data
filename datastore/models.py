from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField

class Reference(models.Model):
    submitter = models.ForeignKey(User, editable=False, on_delete=models.SET_NULL, null=True, blank=True)
    doi = models.CharField('DOI', max_length=200, unique=True)
    info = JSONField(default={
        'pub_name': '',
        'authors': [],
        'journal': '',
        'year': '',
        'month': '',
    })

    def __str__(self):
        return self.doi

class Compound(models.Model):
    submitter = models.ForeignKey(User, editable=False, on_delete=models.SET_NULL, null=True, blank=True)
    checker = models.ForeignKey(User, editable=Flase, on_delete=models.SET_NULL, null=True, blank=True)
    doi = models.ForeignKey(Reference, on_delete=models.SET_NULL, null=True, blank=True)
    info = JSONField(default={
        'dimensionality': 0,
        'ccdc': '',
        'formula': '',
        'ueff': '',
    })

    def __str__(self):
        return str(self.doi) + ' - ' + self.info['ccdc']
