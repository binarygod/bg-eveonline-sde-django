from django.db import models
from bg_eveonline_sde_django.common.models import CustomFloatField


class SolarSystem(models.Model):
    regionID = models.IntegerField(null=True, db_index=True)
    constellationID = models.IntegerField(null=True, db_index=True)
    solarSystemID = models.IntegerField(primary_key=True)
    solarSystemName = models.CharField(max_length=100, null=True)
    x = models.FloatField(null=True)
    y = models.FloatField(null=True)
    z = models.FloatField(null=True)
    xMin = models.FloatField(null=True)
    xMax = models.FloatField(null=True)
    yMin = models.FloatField(null=True)
    yMax = models.FloatField(null=True)
    zMin = models.FloatField(null=True)
    zMax = models.FloatField(null=True)
    luminosity = models.FloatField(null=True)
    border = models.BooleanField(null=True)
    fringe = models.BooleanField(null=True)
    corridor = models.BooleanField(null=True)
    hub = models.BooleanField(null=True)
    international = models.BooleanField(null=True)
    regional = models.BooleanField(null=True)
    constellation = models.BooleanField(null=True)
    security = models.FloatField(null=True, db_index=True)
    factionID = models.IntegerField(null=True)
    radius = models.FloatField(null=True)
    sunTypeID = models.IntegerField(null=True)
    securityClass = models.CharField(max_length=2)

    class Meta:
        db_table = 'mapSolarSystems'
