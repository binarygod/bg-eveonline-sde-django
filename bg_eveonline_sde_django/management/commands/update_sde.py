import requests
import bz2
import subprocess
import os
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings


class Command(BaseCommand):
    help = 'Updates SDE from Fuzzworks'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        tables = []

        app: str
        for app in settings.INSTALLED_APPS:
            # Check if starts with bg_eveonline_sde_django
            if app.startswith('bg_eveonline_sde_django.'):
                tables.append(app.split('.')[:1])

        for table in tables:
            self.stdout.write(self.style.NOTICE('Updating {table}...'.format(table=table)))
            # Download the file
            # r = requests.get('https://www.fuzzwork.co.uk/dump/latest/{table}.sql.bz2'.format(table=table))
            # open('{table}.sql.bz2'.format(table=table), 'wb').write(r.content)
            #
            # # Extract the SQL Dump
            # zipfile = bz2.BZ2File('{table}.sql.bz2'.format(table=table))
            # data = zipfile.read()
            # newfilepath = '{table}.sql'.format(table=table)
            # open(newfilepath, 'wb').write(data)
            #
            # # Import the SQL Dump
            # p = subprocess.run('mysql -u {user} --password={password} -h {host} {database} < {table}.sql'.format(
            #         user=settings.DATABASES['default']['USER'],
            #         password=settings.DATABASES['default']['PASSWORD'],
            #         host=settings.DATABASES['default']['HOST'],
            #         database=settings.DATABASES['default']['NAME'],
            #         table=table
            # ), shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            #
            # # Delete the files
            # os.remove('{table}.sql.bz2'.format(table=table))
            # os.remove('{table}.sql'.format(table=table))
