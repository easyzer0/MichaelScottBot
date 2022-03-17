from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Member(models.Model):
    user = models.ForeignKey(
    User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(null=True, blank=True, max_length=200)
    number = PhoneNumberField(null=False, blank=False, unique=True)
    created = models.DateTimeField(auto_now_add=True)
