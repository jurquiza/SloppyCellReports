from django.contrib import admin

# Register your models here.
from .models import   Question, Choice, ModelProfile, PeriodConstraint


admin.site.register(Question)
admin.site.register(Choice)
#admin.site.register(PeriodConstraint)
admin.site.register(ModelProfile)
admin.site.register(PeriodConstraint)