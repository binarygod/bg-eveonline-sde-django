from django.db import models
from bg_eveonline_sde_django.common.models import CustomFloatField


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
