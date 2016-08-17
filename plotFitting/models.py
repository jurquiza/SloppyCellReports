from __future__ import unicode_literals

from django.db import models

# Create your models here.


## this is nice because we can setup a data base of constrains that we can reuse and also no in which fitting thery were used 






'''
class PeriodConstraint(models.Model):
    start_time = models.FloatField(default=0)
    end_time = models.FloatField(default=0)

class ModelProfile(models.Model):
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
    model_base = models.CharField(default = 'P2011', max_length=3, choices=CLOCK_MODELS)
    photo_period_pattern = models.CharField(default = 'LD', max_length=5, choices=PHOTO_PATTERN)    

class FittingProfile(models.Model):
    
    modelprofile = models.ForeignKey(ModelProfile, on_delete=models.CASCADE)
    periodconstraint = models.ForeignKey(PeriodConstraint, on_delete=models.CASCADE)

'''

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
class PeriodConstraint(models.Model):
    LIGHT_REGIME_CHOICES = (
    ('LD','Light:Dark'),
    ('LL','Constant Light'),
    ('DD','Constant Dark'),
    )
    light_regime = models.CharField(default = 'LD', max_length=3, choices=LIGHT_REGIME_CHOICES)
    gene = models.CharField(max_length=200)
    start_time = models.FloatField(default=0)
    end_time = models.FloatField(default=0)
    def __unicode__(self):
        return self.light_regime
    
class ModelProfile(models.Model):
    model_profile = models.CharField(default='edit name', max_length=200)
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
    model_base = models.CharField(default = 'P2011', max_length=3, choices=CLOCK_MODELS)
    photo_period_pattern = models.CharField(default = 'LD', max_length=5, choices=PHOTO_PATTERN)
    number_of_LD_cycles = models.IntegerField(default=1, blank=True)
    period_constraint = models.ForeignKey(PeriodConstraint, blank=True, null=True,on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    
    
    ## this returns the value of the object 
    def __unicode__(self):
        return self.model_profile
    
    
    
    
    
    