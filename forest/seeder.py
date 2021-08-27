import random

from django.http import JsonResponse, HttpResponse

from forest.models import Forest, TREE_SPECIES, Tree

MIN_FOREST_TREE = 10000
MAX_FOREST_TREE = 100000


def seeds(request):
    Forest.objects.all().delete()
    black_forest_seeder()
    return HttpResponse('Seeding Completed')



def black_forest_seeder():
    black_forest = Forest(name='black_forest')
    black_forest.save()


    forest_trees_total = round(random.uniform(MIN_FOREST_TREE, MAX_FOREST_TREE))
    print(f"seeding less than {forest_trees_total} trees...")

    forest_available_trees = forest_trees_total

    max_area_trees = forest_trees_total / 9
    min_area_trees = max_area_trees / 3

    tree_prototype: Tree = Tree(forest=black_forest)

    for area in range(1, 10, 1):
        area_trees_amount = round(random.uniform(min_area_trees, max_area_trees))
        # print(f'area {area}: {area_trees_amount}')

        tree_prototype.area = area

        for species in TREE_SPECIES:
            min_species_trees = area_trees_amount / 4
            species_trees_amount = round(random.uniform(min_species_trees, area_trees_amount))
            # print(f'species {species[0]}: {species_trees_amount}')

            tree_prototype.species = species[0]
            distribute_by_age(species_trees_amount, tree_prototype)
            # species_ratio[species] = random_share * 100
            area_trees_amount -= species_trees_amount



def distribute_by_age(species_trees_amount: int, tree_prototype: Tree):
    for group in AGE_GROUPS:
        min_age_group_trees = species_trees_amount / 4
        age_group_trees_amount = round(random.uniform(min_age_group_trees, species_trees_amount))
        for tree in range(1, age_group_trees_amount):
            generate_tree(group, tree_prototype)
        species_trees_amount -= age_group_trees_amount


def generate_tree(age_group: tuple[int, int], tree_prototype: Tree):
    new_tree_age = random.uniform(age_group[0], age_group[1])
    tree_prototype.age = new_tree_age
    tree_prototype.lon = 1
    tree_prototype.lat = 1
    tree_prototype.save()
    tree_prototype.id = None


AGE_GROUPS = (
    (1, 10),
    (11, 50),
    (51, 100),
    (51, 250),
)
