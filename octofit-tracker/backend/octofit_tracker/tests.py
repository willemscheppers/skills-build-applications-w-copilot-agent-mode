from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        team = Team.objects.create(name="Test Team")
        user = User.objects.create(email="test@example.com", name="Test User", team=team)
        self.assertEqual(user.name, "Test User")
        self.assertEqual(user.team.name, "Test Team")

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="Alpha Team")
        self.assertEqual(team.name, "Alpha Team")

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        team = Team.objects.create(name="Beta Team")
        user = User.objects.create(email="beta@example.com", name="Beta User", team=team)
        activity = Activity.objects.create(user=user, type="Run", duration=30, calories=200)
        self.assertEqual(activity.type, "Run")
        self.assertEqual(activity.user.name, "Beta User")

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name="Morning Cardio", description="Cardio session", duration=45)
        self.assertEqual(workout.name, "Morning Cardio")

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name="Gamma Team")
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(leaderboard.team.name, "Gamma Team")
        self.assertEqual(leaderboard.points, 100)
