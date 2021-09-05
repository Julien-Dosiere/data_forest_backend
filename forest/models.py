from calendar import calendar
from datetime import date

from django.db import models

TREE_SIZES = (
    ('Small', 'Small'),
    ('Medium', 'Medium'),
    ('Large', 'Large'),
)

EVENT_TYPE = (
    ('I', 'Infestation'),
    ('D', 'Damage'),
    ('A', 'Care'),
    ('C', 'Cutting'),
    ('F', 'Felling'),
)

TREE_STATE = (
    ('Healthy', 'Healthy'),
    ('Worrying', 'Worrying'),
    ('Critical', 'Critical'),
)


TREE_SPECIES = (
    ('Spruce', 'Spruce'),
    ('Pine', 'Pine'),
    ('Beech', 'Beech'),
    ('Oak', 'Oak'),
    ('Fir', 'Fir'),
    ('Larch', 'Larch'),
    ('Ash', 'Ash'),
    ('Alder', 'Alder'),
    ('Maple', 'Maple'),
)


class Forest(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"


class Tree(models.Model):
    alive = models.BooleanField(default=True)
    species = models.CharField(max_length=20, choices=TREE_SPECIES)
    lon = models.FloatField()
    lat = models.FloatField()
    nickname = models.CharField(max_length=30, null=True, blank=True)
    forest = models.ForeignKey(Forest, null=True, on_delete=models.CASCADE, related_name="trees")
    area = models.IntegerField()
    # planted_date = models.DateField(default=date.today)
    age = models.IntegerField(default=1)
    size = models.CharField(max_length=20, choices=TREE_SIZES, default='S')
    state = models.CharField(max_length=20, choices=TREE_STATE, default='H')

    def __str__(self):
        return f"{self.species} {self.id}, area {self.area}"


class Event(models.Model):
    tree = models.ForeignKey(Tree, null=True, on_delete=models.CASCADE, related_name="events")
    type = models.CharField(max_length=1, choices=EVENT_TYPE)
    details = models.TextField()
    date = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.get_type_display()} on {self.tree.species} {self.tree_id}, {self.date}"





