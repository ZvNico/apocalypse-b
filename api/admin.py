from django.contrib import admin
from django.db.models import Model
from .consts import MODELS_TO_REGISTER

# Register your models here.


for model in MODELS_TO_REGISTER:
    if issubclass(model, Model):
        admin.site.register(model)
    else:
        admin.site.register(model[0], model[1])
