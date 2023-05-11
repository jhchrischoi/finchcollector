from django.db import models

MEALS = (
    ('F', 'Fruit'),
    ('S', 'Seed'),
    ('G', 'Grass')
)

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    population = models.CharField(max_length=100)
    habitat= models.CharField(max_length=100)
    trend = models.CharField(max_length=100)
  
    def __str__(self):
        return f'{self.name} ({self.id})'

