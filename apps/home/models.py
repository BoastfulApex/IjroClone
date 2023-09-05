from django.db import models
from django.contrib.auth.models import User
import random
import string


def generate_random_string():
    digits = ''.join(random.choices(string.digits, k=8))

    letters = ''.join(random.choices(string.ascii_uppercase, k=2))

    custom_string = letters + digits
    return custom_string


class DocsObjects(models.Model):
    id = models.CharField(max_length=10, primary_key=True, default=generate_random_string, editable=False)
    file = models.FileField(null=True, upload_to='files/')
    qrcode = models.ImageField(null=True, blank=True, upload_to='files/')
    document_address = models.CharField(max_length=200, null=True)
    date = models.DateField(null=True)
    who_signed = models.CharField(max_length=200, null=True)
    signatory_position = models.CharField(max_length=200, null=True)
    signatory_workplace = models.CharField(max_length=200, null=True)
    performer = models.CharField(max_length=200, null=True)
    performer_position = models.CharField(max_length=200, null=True)
    performer_workplace = models.CharField(max_length=200, null=True)
    start_ERI = models.DateField(null=True, blank=True)
    end_ERI = models.DateField(null=True, blank=True)
    given_by_ERI = models.CharField(max_length=200, null=True)

    @property
    def PhotoURL(self):
        try:
            return self.qrcode.url
        except:
            return ''

    @property
    def FileURL(self):
        try:
            return self.file.url
        except:
            return ''
