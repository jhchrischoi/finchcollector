from django.db import models

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    population = models.CharField(max_length=100)
    habitat= models.CharField(max_length=100)
    trend = models.CharField(max_length=100)
  
    def __str__(self):
        return self.name

# finches = [
#   {'name':'Evening Grosbeak',
#   'population':'3.4 Million',
#   'habitat':'Northern and montane forests',
#   'trend':'Decreasing population'},
#   {'name':'Pine Grosbeak',
#   'population':'4.4 Million',
#   'habitat':'Open boreal forest',
#   'trend':'Decreasing population'}
# ]