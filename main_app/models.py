from django.db import models
from django.urls import reverse

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
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})

class Feeding(models.Model):
  date = models.DateField()
  meal = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=MEALS,
    # set the default value for meal to be 'B'
    default=MEALS[0][0]
  )
  finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']