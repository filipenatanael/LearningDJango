from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField('Name',max_length=100)
    slug = models.SlugField('Shortcut')
    description = models.TextField('Description', blank=True)
    start_date = models.DateField('Data Starting', null=True, blank=True)
    image = models.ImageField(upload_to='courses/images', verbose_name='Images', null=True, blank=True)

    created_at = models.DateTimeField('Created in', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now_add=True)