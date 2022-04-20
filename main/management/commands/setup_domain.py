from django.apps import apps
from django.conf import settings
from django.core.management.base import BaseCommand

class Command(BaseCommand) :
    help = ""

    def add_arguments(self, parser) :
        parser.add_argument(
            'domain',
            type    = str,
            help    = 'Define default domain name for contrib.site app.'
        )

    def handle(self, *args, **kwargs):
        domain = kwargs.get('domain')

        Site    = apps.get_model('sites', 'Site')
        Site(
            pk      = getattr(settings, 'SITE_ID', 1),
            domain  = domain,
            name    = domain).save()
