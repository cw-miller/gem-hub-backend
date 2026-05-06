import random
from django.core.management.base import BaseCommand
from django.apps import apps
from faker import Faker

class Command(BaseCommand):
    help = 'Seeds multiple entries and prints progress'

    def handle(self, *args, **options):
        fake = Faker()
        
        # 1. Dynamic Model Loading
        Profile = apps.get_model('core', 'Profile')
        GemListing = apps.get_model('gems', 'GemListing')
        Job = apps.get_model('jobs', 'Job')
        Application = apps.get_model('jobs', 'Application')

        # 2. Get the Profile (Supabase UUID)
        target_uuid = "a614ed82-1074-459f-8172-311c75aa6f09"
        user_profile, _ = Profile.objects.get_or_create(
            profile=target_uuid,
            defaults={"username": f"user_{random.randint(1, 999)}"}
        )

        # 3. Seed GEMS in a loop
        self.stdout.write("--- Starting Gem Seeding ---")
        for i in range(1, 11): # This ensures it runs 10 times
            try:
                GemListing.objects.create(
                    owner=user_profile,
                    name=f"{fake.color_name().capitalize()} {random.choice(['Sapphire', 'Ruby', 'Emerald'])} #{i}",
                    carat=round(random.uniform(1.0, 5.0), 2),
                    price=float(random.randint(1000, 5000)),
                    description=fake.sentence(),
                    location=fake.city(),
                    status="active"
                )
                self.stdout.write(f"Created Gem {i}/10")
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Failed to create Gem {i}: {e}"))

        # 4. Seed JOBS in a loop
        self.stdout.write("--- Starting Job Seeding ---")
        for i in range(1, 11):
            try:
                Job.objects.create(
                    employer=user_profile,
                    title=f"{fake.job()} Position #{i}",
                    company_info=fake.company(),
                    salary=float(random.randint(50000, 100000)),
                    status="open",
                    logo_color=random.randint(0, 16777215)
                )
                self.stdout.write(f"Created Job {i}/10")
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Failed to create Job {i}: {e}"))

        self.stdout.write(self.style.SUCCESS('Seeding process finished!'))