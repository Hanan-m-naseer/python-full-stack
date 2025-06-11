from django.db import models
from datetime import timedelta

# Create your models here.
class Recipes(models.Model):
    Name = models.CharField(max_length=250)
    Prep_time = models.DurationField (default=timedelta(minutes=120))
    DIFFICULTY_CHOICES=[
        (1,'easy'),
        (2,'medium'),
        (3,'hard')
    ]
    Difficulty = models.IntegerField(choices=DIFFICULTY_CHOICES)
    Vegetarian=models.Boolean()
    Recipe_img = models.ImageField(upload_to='recipe/')
    Description = models.CharField(max_length=5000)

