from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')
        User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel)
        User.objects.create(name='Batman', email='batman@dc.com', team=dc)

    def test_user_team(self):
        user = User.objects.get(email='spiderman@marvel.com')
        self.assertEqual(user.team.name, 'Marvel')

    def test_team_count(self):
        self.assertEqual(Team.objects.count(), 2)

    def test_user_count(self):
        self.assertEqual(User.objects.count(), 2)
