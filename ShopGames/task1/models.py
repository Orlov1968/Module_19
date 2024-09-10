from django.db import models


# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=70)
    balance = models.DecimalField(max_digits=10, decimal_places=3)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=150)
    cost = models.DecimalField(max_digits=10, decimal_places=3)
    size = models.DecimalField(max_digits=10000000, decimal_places=5)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='game')
    discount = models.DecimalField(max_digits=2, decimal_places=2)
    buy = models.BooleanField()

    def __str__(self):
        return self.title
