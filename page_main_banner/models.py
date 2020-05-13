from django.db import models
from cms.models import CMSPlugin
from django.contrib import admin
from django.core.validators import FileExtensionValidator

class PageMainBanner(CMSPlugin):
    image = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['svg','png','jpg','jpeg'])])
    heading = models.CharField(
        blank=True, max_length=100, help_text="Enter heading", default="")
    description = models.CharField(
        blank=True, max_length=500, help_text="Enter description", default="")
    