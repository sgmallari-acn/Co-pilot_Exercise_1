from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User(name='Batman', email='batman@dc.com', team=dc),
        ]
        for user in users:
            user.save()

        # Create activities
        Activity.objects.create(user=users[0], type='Running', duration=30, timestamp='2025-11-29T10:00:00Z')
        Activity.objects.create(user=users[1], type='Cycling', duration=45, timestamp='2025-11-29T11:00:00Z')
        Activity.objects.create(user=users[2], type='Swimming', duration=60, timestamp='2025-11-29T12:00:00Z')
        Activity.objects.create(user=users[3], type='Yoga', duration=20, timestamp='2025-11-29T13:00:00Z')

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=75)
        Leaderboard.objects.create(team=dc, points=80)

        # Create workouts
        Workout.objects.create(name='Hero HIIT', description='High intensity for heroes', suggested_for='Marvel')
        Workout.objects.create(name='Justice Yoga', description='Balance and strength', suggested_for='DC')

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
