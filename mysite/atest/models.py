from django.db import models

# Create your models here.
class Atestation(models.Model):
    fio = models.TextField('FIO:')
    student_card = models.IntegerField("ID:")
    gpa = models.FloatField("GPA:")

    def __str__(self):
        return self.fio

    def get_absolute_url(self):
        return f"/"


    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
