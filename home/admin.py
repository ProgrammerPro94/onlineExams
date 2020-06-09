from django.contrib import admin
from .models import Question, Test, Teacher, Result

# Register your models here.
admin.site.register(Question)
admin.site.register(Test)
admin.site.register(Teacher)
admin.site.register(Result)
