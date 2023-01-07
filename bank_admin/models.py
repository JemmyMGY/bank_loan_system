from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class AdminModel(models.Model):
    admin_email = models.EmailField(primary_key=True, max_length=50,  db_index=True)
    admin_password = models.CharField(max_length=16, validators=[MinLengthValidator(8)])