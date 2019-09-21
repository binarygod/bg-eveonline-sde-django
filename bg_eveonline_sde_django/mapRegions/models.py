from django.db import models
from bg_eveonline_sde_django.common.models import CustomFloatField


class Region(models.Model):
    regionID = models.IntegerField(primary_key=True)
    regionName = models.CharField(max_length=100, null=True)
    x = models.FloatField(null=True)
    y = models.FloatField(null=True)
    z = models.FloatField(null=True)
    xMin = models.FloatField(null=True)
    xMax = models.FloatField(null=True)
    yMin = models.FloatField(null=True)
    yMax = models.FloatField(null=True)
    zMin = models.FloatField(null=True)
    zMax = models.FloatField(null=True)
    factionID = models.IntegerField(null=True)
    radius = CustomFloatField(null=True)

    class Meta:
        db_table = 'mapRegions'
