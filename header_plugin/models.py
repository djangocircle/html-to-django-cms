from django.db import models
from cms.models import CMSPlugin

# Create your models here.
class Header(CMSPlugin):
    heading_text = models.CharField(max_length=100, help_text="Page Name or Title of Page", blank=True)
