from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Collagename(models.Model):
  collage_name = models.CharField(max_length=50)
  about = models.TextField()
  location = models.TextField()
  collage_website = models.CharField(max_length=60)
  cs_cutoff = models.FloatField()
  ecs_cutoff = models.FloatField()
  mech_cutoff = models.FloatField()
  extc_cutoff = models.FloatField()
  Image = models.ImageField(null=True, blank=True, upload_to="img/%y")

  def __str__(self):
    return self.collage_name


class Rating(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  collagename = models.ForeignKey(Collagename, on_delete=models.CASCADE)
  rating = models.IntegerField()

  def __str__(self):
    return str(self.rating)
