from django.db import models


class CustomFloatField(models.Field):
    def db_type(self, connection):
        return 'float'


class Station(models.Model):
    stationID = models.BigIntegerField()
    security = models.FloatField(null=True)
    dockingCostPerVolume = models.FloatField(null=True)
    maxShipVolumeDockable = models.FloatField(null=True)
    officeRentalCost = models.IntegerField(null=True)
    operationID = models.IntegerField(null=True, db_index=True)
    stationTypeID = models.IntegerField(null=True, db_index=True)
    corporationID = models.IntegerField(null=True, db_index=True)
    solarSystemID = models.IntegerField(null=True, db_index=True)
    constellationID = models.IntegerField(null=True, db_index=True)
    regionID = models.IntegerField(null=True, db_index=True)
    stationName = models.CharField(max_length=100, null=True)
    x = models.FloatField(null=True)
    y = models.FloatField(null=True)
    z = models.FloatField(null=True)
    reprocessingEfficiency = models.FloatField(null=True)
    reprocessingStationsTake = models.FloatField(null=True)
    reprocessingHangarFlag = models.IntegerField(null=True)

    class Meta:
        db_table = 'staStations'


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
        managed = False
