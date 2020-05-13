from django.db import models
from cms.models import CMSPlugin
from django.contrib import admin
from django.core.validators import FileExtensionValidator

class ImageGallery(CMSPlugin):
    heading = models.CharField(
        blank=True, max_length=100, help_text="Enter heading", default="")

    def copy_relations(self, oldinstance):
        for item in oldinstance.image_items.all():
            item.pk = None
            item.heading = self
            item.save()

    def __str__(self):
        return self.heading

class Images(models.Model):
    title = models.CharField(
        blank=False, max_length=100, help_text="Enter title", default="")
    image = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['svg','png','jpg','jpeg'])])
    description = models.CharField(blank=False, max_length=500, help_text="Enter description", default="")
    heading = models.ForeignKey(ImageGallery, related_name='image_items', on_delete=models.CASCADE)

class ImageGalleryInlineAdmin(admin.StackedInline):
    model = Images