from django.db import models
from datetime import date, time, datetime, timedelta
import datetime

class Language(models.Model):
    name = models.CharField(max_length=20)
    month_to_learn = models.IntegerField()

    def __str__(self):
        return f'{self.name}'

    def change_name(self):
        l1 = str(self.name)
        lf = str.title(l1)
        return lf

    def save(self, *args, **kwargs):
        self.name = self.change_name()
        super().save(*args, **kwargs)

class AbstractPerson(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=13)

    # def __str__(self):
    #     return f'{self.name}'

    def change_tel(self):
        t1 = str(self.phone_number)
        if t1[0] == '0':
            tf = '+996' + t1[1:]
            return tf

    def save(self, *args, **kwargs):
        self.phone_number = self.change_tel()
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
        ordering = ['name', ]

class Student(AbstractPerson):
    work_study_place = models.CharField(max_length=50, null=True)
    has_own_notebook = models.BooleanField(default=False)
    preferred_os = (
        ('win', 'Windows'),
        ('mac', 'MacOS'),
        ('lin', 'Linux'))

    def __str__(self):
        return self.name

    class Meta(AbstractPerson.Meta):
        pass

class Mentor(AbstractPerson):
    main_work = models.CharField(max_length=50, null=True)
    experience = models.DateField()
    members = models.ManyToManyField(Student, related_name='mentors', through='Course')

    class Meta:
        ordering = ['name', ]

    def __str__(self):
        return f'{self.name} - {self.main_work}'

class Course(models.Model):
    name = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    date_started = models.DateField()
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def get_end_date(self):
        dstart = datetime.datetime.strptime(self.date_started, '%Y-%m-%d')
        month = dstart.now().date().month - Language.month_to_learn
        return (f'{self.name} {month}')

    def __str__(self):
        return f'{self.mentor.name} - {self.student.name} - {self.get_end_date()}'