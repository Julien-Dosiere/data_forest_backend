import random

from django.http import JsonResponse, HttpResponse

from forest.models import Forest, TREE_SPECIES, Tree, TREE_STATE

MIN_FOREST_TREE = 1000
MAX_FOREST_TREE = 4000
AREA_NUMBER = 4


def seeds(request) -> HttpResponse:
    if request.method != 'POST':
        raise ValueError('Incorrect Request, try POST instead')

    forest_name = request.POST.get('name') or 'Unnamed Forest'
    new_forest_id = generate_forest(forest_name)
    return HttpResponse(f'New Forest seeded, id: {new_forest_id}, name: {forest_name}')


def generate_forest(forest_name: str) -> int:
    new_forest = Forest(name=forest_name)
    new_forest.save()

    forest_trees_total = random.randint(MIN_FOREST_TREE, MAX_FOREST_TREE)

    print(f"seeding maximum of {forest_trees_total} trees...")

    max_area_trees = round(forest_trees_total / AREA_NUMBER)
    min_area_trees = round(max_area_trees / 3)

    tree_prototype: Tree = Tree(forest=new_forest)

    area_seeder(max_area_trees, min_area_trees, tree_prototype)

    return new_forest.id


def area_seeder(max_area_trees, min_area_trees, tree_prototype: Tree):
    for area in range(1, AREA_NUMBER, 1):
        area_trees_amount = random.randint(min_area_trees, max_area_trees)
        tree_prototype.area = area
        species_seeder(area_trees_amount, tree_prototype)


def species_seeder(area_trees_amount: int, tree_prototype: Tree):
    area_taken_coordinates = set()
    for species in TREE_SPECIES:
        min_species_trees = round(area_trees_amount / 4)
        species_trees_amount = random.randint(min_species_trees, area_trees_amount)
        tree_prototype.species = species[0]
        state_seeder(species_trees_amount, tree_prototype, area_taken_coordinates)
        area_trees_amount -= species_trees_amount


def state_seeder(species_trees_amount: int, tree_prototype: Tree, area_taken_coordinates: set):
    for state in TREE_STATE:
        min_state_trees = round(species_trees_amount / 2)
        state_trees_amount = random.randint(min_state_trees, species_trees_amount)
        tree_prototype.state = state[0]
        age_seeder(state_trees_amount, tree_prototype, area_taken_coordinates)
        species_trees_amount -= state_trees_amount


def age_seeder(species_trees_amount: int, tree_prototype: Tree, area_taken_coordinates: set):
    for group in AGE_GROUPS:
        min_age_group_trees = round(species_trees_amount / 4)
        max_age_group_trees = round(species_trees_amount * .8)

        age_group_trees_amount = random.randint(min_age_group_trees, max_age_group_trees)
        for tree in range(1, age_group_trees_amount):
            generate_tree(group, tree_prototype, area_taken_coordinates)
        species_trees_amount -= age_group_trees_amount


def generate_tree(age_group: tuple[int, int], tree_prototype: Tree, area_taken_coordinates: set):

    generate_tree_age(age_group, tree_prototype)

    set_tree_size(tree_prototype)

    generate_tree_coordinates(tree_prototype, area_taken_coordinates)

    plant_tree(tree_prototype)


def generate_tree_age(age_group, tree_prototype):
    new_tree_age = random.randint(age_group[0], age_group[1])
    tree_prototype.age = new_tree_age


def set_tree_size(tree_prototype):
    if tree_prototype.age < 30:
        tree_prototype.size = 'S'
    elif tree_prototype.age < 75:
        tree_prototype.size = 'M'
    else:
        tree_prototype.size = 'L'


def generate_tree_coordinates(tree_prototype, area_taken_coordinates: set):
    while True:
        new_lat = random.randint(0, 1000)
        new_lon = random.randint(0, 1000)
        new_coordinates = f'{new_lat}{new_lon}'

        if new_coordinates not in area_taken_coordinates:
            tree_prototype.lat = new_lat
            tree_prototype.lon = new_lon
            area_taken_coordinates.add(new_coordinates)
            break


def plant_tree(tree_prototype):
    tree_prototype.save()
    tree_prototype.id = None


AGE_GROUPS = (
    (51, 250),
    (51, 100),
    (11, 50),
    (1, 10),

)
