
from rest_framework import serializers
from forest.models import Tree, Event, Forest


class ForestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forest
        fields = [
            'id',
            'name',
        ]


class TreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tree
        fields = [
            'id',
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
            'id',
            'tree',
            'type',
            'details',
            'date',
        ]
