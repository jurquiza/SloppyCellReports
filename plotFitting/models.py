from __future__ import unicode_literals

from django.db import models

# Create your models here.

#class periodConstraint(models.Model):
 #   experiment = models.CharField(max_length=10)
  #  period_contraint_start =  models.floatField(max_digits=10)
    #period_constrain_stop =

class fittingProfile(models.Model):
    CLOCK_MODELS = (
    ('P11','P2011'),
    ('F14','F2014'),
    ('C16','C2016'),
    )
    
    PHOTO_PATTERN = (
    ('LD', 'Light_Dark'),
    ('LD_LL', 'Light_Dark->Light'),
    ('LD_DD', 'Light_Dark->Dark'),
    ('LL', 'Constant_Light'),
    ('DD', 'Constant_Dark'),
    )
    
    model_base = models.CharField(max_length=3, choices=CLOCK_MODELS)
    photo_period_pattern = models.CharField(max_length=5, choices=PHOTO_PATTERN)
    published = models.BooleanField(default=False)

