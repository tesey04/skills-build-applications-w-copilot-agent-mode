from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from pymongo import MongoClient
from django.conf import settings

# Establish MongoDB connection
client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
db = client[settings.DATABASES['default']['NAME']]

@api_view(['GET'])
def api_root(request, format=None):
    base_url = 'http://127.0.0.1:8000/'
    return Response({
        'users': base_url + 'api/users/',
        'teams': base_url + 'api/teams/',
        'activities': base_url + 'api/activities/',
        'leaderboard': base_url + 'api/leaderboard/',
        'workouts': base_url + 'api/workouts/'
    })

class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        users = list(db.users.find())
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class TeamViewSet(viewsets.ViewSet):
    def list(self, request):
        teams = list(db.teams.find())
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)

class ActivityViewSet(viewsets.ViewSet):
    def list(self, request):
        activities = list(db.activity.find())
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)

class LeaderboardViewSet(viewsets.ViewSet):
    def list(self, request):
        leaderboard = list(db.leaderboard.find())
        serializer = LeaderboardSerializer(leaderboard, many=True)
        return Response(serializer.data)

class WorkoutViewSet(viewsets.ViewSet):
    def list(self, request):
        workouts = list(db.workouts.find())
        serializer = WorkoutSerializer(workouts, many=True)
        return Response(serializer.data)