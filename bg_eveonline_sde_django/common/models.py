from django.db import models


class CustomFloatField(models.Field):
    def db_type(self, connection):
        return 'float'
