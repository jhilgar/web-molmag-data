from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.core.validators import MaxValueValidator, MinValueValidator

def default_reference_info():
    return {
        'pub_name': '',
        'authors': [],
        'journal': '',
        'year': '',
        'month': '',
    }

def default_compound_info():
    return {}

class Reference(models.Model):
    submitter = models.ForeignKey(User, editable=False, on_delete=models.SET_NULL, null=True, blank=True)
    doi = models.CharField('DOI', max_length=200, unique=True)
    info = JSONField(default=default_reference_info)

    def __str__(self):
        return self.doi

class Compound(models.Model):
    submitter = models.ForeignKey(User, editable=False, on_delete=models.SET_NULL, null=True, blank=True)
    checker = models.ForeignKey(User, editable=False, on_delete=models.SET_NULL, null=True, blank=True, related_name='checker')
    doi = models.ForeignKey(Reference, on_delete=models.CASCADE)
    formula = models.CharField('Formula', max_length=50)
    ccdc = models.CharField('CCDC Identifier', max_length=9, null=True, blank=True)
    dimensionality = models.IntegerField(default=0, validators=[MaxValueValidator(3), MinValueValidator(0)])
    ueff = models.FloatField('Effective Barrier', validators=[MaxValueValidator(10000), MinValueValidator(0)], null=True, blank=True)
    hdc = models.FloatField('DC Field', validators=[MaxValueValidator(70000), MinValueValidator(0)], null=True, blank=True)
    tau0 = models.FloatField('τ₀', null=True, blank=True)
    tc = models.FloatField('Curie Temperature', validators=[MaxValueValidator(10000), MinValueValidator(0)], null=True, blank=True)
    info = JSONField(default=default_compound_info, null=True, blank=True)

    def __str__(self):
        return str(self.doi) + ' - ' + str(self.formula)
