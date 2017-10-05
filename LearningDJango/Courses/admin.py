from django.contrib import admin

# Register your models here.

from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'start_date', 'created_at']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Course, CourseAdmin)