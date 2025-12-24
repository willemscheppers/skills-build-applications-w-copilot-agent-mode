from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import models as app_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Deleting old data...'))
        # Delete all data from collections, children first, and use instance delete to avoid unhashable errors
        for obj in app_models.Activity.objects.all():
            if obj.pk:
                obj.delete()
        for obj in app_models.Leaderboard.objects.all():
            if obj.pk:
                obj.delete()
        for obj in app_models.User.objects.all():
            if obj.pk:
                obj.delete()
        for obj in app_models.Workout.objects.all():
            if obj.pk:
                obj.delete()
        for obj in app_models.Team.objects.all():
            if obj.pk:
                obj.delete()

        self.stdout.write(self.style.SUCCESS('Old data deleted. Creating test data...'))


        # Create Teams

        marvel = app_models.Team(name='Team Marvel')
        marvel.save()
        dc = app_models.Team(name='Team DC')
        dc.save()

        # Create Users
        ironman = app_models.User(email='ironman@marvel.com', name='Iron Man', team=marvel)
        ironman.save()
        captain = app_models.User(email='captain@marvel.com', name='Captain America', team=marvel)
        captain.save()
        batman = app_models.User(email='batman@dc.com', name='Batman', team=dc)
        batman.save()
        superman = app_models.User(email='superman@dc.com', name='Superman', team=dc)
        superman.save()

        # Create Activities
        run = app_models.Activity(user=ironman, type='Run', duration=30, calories=300)
        run.save()
        swim = app_models.Activity(user=captain, type='Swim', duration=45, calories=400)
        swim.save()
        bike = app_models.Activity(user=batman, type='Bike', duration=60, calories=500)
        bike.save()
        yoga = app_models.Activity(user=superman, type='Yoga', duration=20, calories=150)
        yoga.save()

        # Create Workouts
        morning_cardio = app_models.Workout(name='Morning Cardio', description='Cardio for all heroes', duration=40)
        morning_cardio.save()
        strength_training = app_models.Workout(name='Strength Training', description='Strength for all heroes', duration=50)
        strength_training.save()

        # Create Leaderboard
        marvel_lb = app_models.Leaderboard(team=marvel, points=700)
        marvel_lb.save()
        dc_lb = app_models.Leaderboard(team=dc, points=650)
        dc_lb.save()

        self.stdout.write(self.style.SUCCESS('Test data created successfully!'))
