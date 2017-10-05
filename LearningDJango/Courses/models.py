from django.db import models

# Create your models here.

class CourseManager(models.Manager):
    #Course.objects.search('Phyton')
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | \
            models.Q(description__icontains=query)
        )
    def insert(self, name, description):
        newCourse = Course()
        newCourse.name = name
        newCourse.description = description
        newCourse.save()


class Course(models.Model):
    name = models.CharField('Name',max_length=100)
    slug = models.SlugField('Shortcut')
    description = models.TextField('Description', blank=True)
    start_date = models.DateField('Data Starting', null=True, blank=True)
    image = models.ImageField(upload_to='courses/images', verbose_name='Images', null=True, blank=True)

    created_at = models.DateTimeField('Created in', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now_add=True)

    objects = CourseManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = "Cursos"
        ordering = ['-name']