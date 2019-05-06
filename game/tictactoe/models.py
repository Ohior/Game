from django.db import models

# Create your models here.
class TttModel(models.Model):
    name = models.CharField(max_length=50)
    turn = models.CharField(max_length=50)
    computer_score = models.IntegerField()
    username_score = models.IntegerField()