from django.db import models

# Create your models here.
class Animal(models.Model):
    KIND_OF_ANIMAL = [
        ('D', 'dogs'),
        ('C', 'cats'),
        ('P', 'parrots')
    ]
    KIND_OF_CHARACTER = [
        ('A', 'активный'),
        ('K', 'спокойный')
    ]
    SEX = [
        ('F', 'female'),
        ('M', 'male'),
    ]
    name = models.TextField(max_length=100)
    breed = models.TextField(max_length=30)
    description = models.TextField()
    date = models.DateField()
    kind = models.CharField(max_length=1, choices=KIND_OF_ANIMAL)
    age = models.IntegerField(blank=True, null=True)
    character = models.CharField(max_length=1, choices=KIND_OF_CHARACTER)
    avatar = models.ImageField(upload_to='avatars', blank=True)
    sex = models.CharField(max_length=1, choices=SEX)

    def __str__(self):
        return self.name