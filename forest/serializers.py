
from rest_framework import serializers
from forest.models import Tree, Event, Forest


class ForestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Forest
        fields = [
            'name',
        ]


class TreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tree
        fields = [
            'alive',
            'species',
            'lon',
            'lat',
            'nickname',
            'forest',
            'area',
            'age',
            'size',
            'state',
        ]


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = [
            'tree',
            'type',
            'details',
            'date',
        ]
