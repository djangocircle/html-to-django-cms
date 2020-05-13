# Generated by Django 3.0.6 on 2020-05-13 13:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageGallery',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='image_gallery_imagegallery', serialize=False, to='cms.CMSPlugin')),
                ('heading', models.CharField(blank=True, default='', help_text='Enter heading', max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', help_text='Enter title', max_length=100)),
                ('image', models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['svg', 'png', 'jpg', 'jpeg'])])),
                ('description', models.CharField(default='', help_text='Enter description', max_length=500)),
                ('heading', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_items', to='image_gallery.ImageGallery')),
            ],
        ),
    ]