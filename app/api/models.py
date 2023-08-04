from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models


class Doctor(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50, null=True)
    lastname = models.CharField(max_length=50)
    specialization = models.CharField(max_length=100)


class Patient(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50, null=True)
    lastname = models.CharField(max_length=50)


class Exercise(models.Model):
    name = models.CharField(max_length=200, unique=True)
    period = ArrayField(models.BooleanField(default=False), size=7)
    allowed_doctors = models.ManyToManyField(Doctor, related_name='exercises')


class AssignedExercise(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='assigned_exercises')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='assigned_exercises')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    date_start = models.DateField(auto_now_add=True)


__all__ = ('Doctor', 'Patient', 'Exercise', 'AssignedExercise', 'User',)
