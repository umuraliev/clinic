from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Direction(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = 'Direction'
        verbose_name_plural = 'Directions'

    def __str__(self):
        return self.title


class Speciality(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, primary_key=True, unique=True)
    direction = models.ManyToManyField(Direction, related_name='directions')

    def __str__(self):
        return self.title

class Doctor(models.Model):
    speciality = models.ForeignKey(Speciality, related_name='doctors', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='doctors', blank=True)
    ranks = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'

    def __str__(self):
        return self.name


class Review(models.Model):
    """Отзывы"""
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    doctor = models.ForeignKey(Doctor, related_name='reviews', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author}: {self.body}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
