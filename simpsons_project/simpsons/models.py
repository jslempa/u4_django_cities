from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=100)
    population = models.IntegerField(default=0)
    photo_url = models.TextField()

    def __str__(self):
        return self.name
    
class Attraction(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='attractions')
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    photo_url = models.TextField()

    def __str__(self):
        return self.name

class Review(models.Model):
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE, related_name='reviews')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    photo_url = models.TextField()

    def __str__(self):
        return self.title     