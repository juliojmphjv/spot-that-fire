from django.core.management.base import BaseCommand, CommandError
from services.dataframe import builder, builder_incra


class Command(BaseCommand):
    help = "Create dataframe"

    def handle(self, *args, **options):
        builder_incra()

        self.stdout.write(
            self.style.SUCCESS("Successfully generated dataframe")
        )
