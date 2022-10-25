from django.db import models


# Create your models here.
class Collagename(models.Model):
  collage_name = models.CharField(max_length=50)
  collage_website = models.CharField(max_length=60)
  cs_cutoff = models.FloatField()
  ecs_cutoff = models.FloatField()
  mech_cutoff = models.FloatField()
  extc_cutoff = models.FloatField()
  Image = models.ImageField(null=True, blank=True, upload_to="img/%y")

  def __str__(self):
    return self.collage_name
