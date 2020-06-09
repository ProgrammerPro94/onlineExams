from django.db import models
from django_mysql.models import ListCharField

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=50, default='How')
    email = models.EmailField()

    def __str__(self):
        return self.name


class Test(models.Model):
    name = models.CharField(max_length=100, unique=True)
    date = models.DateTimeField(auto_now=True)
    no_questions = models.IntegerField()
    questions = models.TextField()
    subject = models.CharField(max_length=80, default='Maths')
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    class_name = models.IntegerField(default=8)
    password = models.CharField(max_length=50, default='init')

    def __str__(self):
        return f"{self.name} by {self.author}"
        

class Question(models.Model):
    text = models.TextField()
    answer = models.CharField(max_length=4)
    options = models.TextField(default="A")
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    index = models.IntegerField(default=1)

    def __str__(self):
        return self.text
    
class Result(models.Model):
    marks = models.IntegerField()
    given_answers = models.TextField(default='none')
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    student = models.CharField(max_length=100)
    student_class = models.IntegerField(default=8)
    student_section = models.CharField(max_length=1, default='A')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, default='Maths')
    full_marks = models.IntegerField(default=10)

    def __str__(self):
        return f"{self.test} by {self.student}"
