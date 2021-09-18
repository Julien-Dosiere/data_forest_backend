import datetime
import random

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from django.http import HttpResponse, JsonResponse

from forest.models import Tree, Event, Forest, TREE_SPECIES
from forest.serializers import TreeSerializer, EventSerializer, ForestSerializer


class ForestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Forest.objects.all().order_by('name')
    serializer_class = ForestSerializer
    permission_classes = [permissions.AllowAny]


class TreeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Tree.objects.all().order_by('area')
    serializer_class = TreeSerializer
    permission_classes = [permissions.AllowAny]


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.AllowAny]


def drop_all(request):
    try:
        Forest.objects.all().delete()
    except Exception as error:
        return JsonResponse(error)
    return JsonResponse(f'All forests deleted')









