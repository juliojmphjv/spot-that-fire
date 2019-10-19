from django.core.management.base import BaseCommand, CommandError
from services.dataframe import builder


class Command(BaseCommand):
    help = "Create dataframe"

    def handle(self, *args, **options):
        builder()

        self.stdout.write(
            self.style.SUCCESS("Successfully generated dataframe")
        )
