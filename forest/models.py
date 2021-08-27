from calendar import calendar
from datetime import date

from django.db import models

# Create your models here.

TREE_SIZES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
)

EVENT_TYPE = (
    ('I', 'Infestation'),
    ('D', 'Damage'),
    ('A', 'Care'),
    ('C', 'Cutting'),
    ('F', 'Felling'),
)

TREE_STATE = (
    ('H', 'Healthy'),
    ('W', 'Worrying'),
    ('C', 'Critical'),
)

# TREE_SPECIES = (
#     ('A', 'Ash'),
#     ('D', 'Alder'),
#     ('B', 'Beech'),
#     ('C', 'Chestnut tree'),
#     ('E', 'Elm'),
#     ('F', 'Fir'),
#     ('H', 'Hornbeam'),
#     ('L', 'Larch'),
#     ('M', 'Maple'),
#     ('O', 'Oak'),
#     ('P', 'Pine'),
#     ('S', 'Spruce'),
#     ('W', 'Wild Cherry'),
# )

TREE_SPECIES = (
    ('S', 'Spruce'),
    ('P', 'Pine'),
    ('B', 'Beech'),
    ('O', 'Oak'),
    ('F', 'Fir'),
    ('L', 'Larch'),
    ('A', 'Ash'),
    ('D', 'Alder'),
    ('M', 'Maple'),
)


class Forest(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"


class Tree(models.Model):
    alive = models.BooleanField(default=True)
    species = models.CharField(max_length=1, choices=TREE_SPECIES)
    lon = models.FloatField()
    lat = models.FloatField()
    nickname = models.CharField(max_length=30, null=True, blank=True)
    forest = models.ForeignKey(Forest, null=True, on_delete=models.CASCADE, related_name="trees")
    area: int = models.IntegerField()
    # planted_date = models.DateField(default=date.today)
    age = models.IntegerField(default=1)
    size = models.CharField(max_length=1, choices=TREE_SIZES, default='S')
    state = models.CharField(max_length=1, choices=TREE_STATE, default='H')

    def __str__(self):
        return f"{self.species} {self.id}, area {self.area}"


class Event(models.Model):
    tree = models.ForeignKey(Tree, null=True, on_delete=models.CASCADE, related_name="events")
    type = models.CharField(max_length=1, choices=EVENT_TYPE)
    details = models.TextField()
    date = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.get_type_display()} on {self.tree.species} {self.tree_id}, {self.date}"



