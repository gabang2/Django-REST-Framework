from django.contrib import admin

# Register your models here.
from student.models import Student, Class

admin.site.register(Student)
admin.site.register(Class)
