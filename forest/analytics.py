from enum import Enum

import numpy as np
import pandas as pd
from django.http import HttpResponse
from django_pandas.io import read_frame

from forest.models import Tree


def get_frame(request):
    try:
        if request.method != 'POST':
            raise ValueError('Incorrect Request')

        x_data = get_data_type(request.POST.get('x_data'))
        y_data = get_data_type(request.POST.get('y_data'))

        forest_id = request.POST.get('forest_id')
        if not forest_id.isnumeric():
            raise ValueError('forest_id must be a number')
        query = Tree.objects.filter(forest__id=forest_id).values()
        if len(query) == 0:
            raise ValueError('This forest does not exist or is empty')

        df = pd.DataFrame.from_records(query)
        pivot = df.pivot_table(
            values='id',
            columns=y_data,
            index=x_data,
            margins=True,
            fill_value=0,
            aggfunc=pd.Series.nunique)
        return HttpResponse(pivot.to_json())
    except ValueError as error:
        return HttpResponse(error)


def get_data_type(input: str):
    if input in DataType._value2member_map_:
        return input
    else:
        raise ValueError('Incorrect x_data or y_data value, accepted value are species, area, age, size, state, alive')


class DataType(Enum):
    SPECIES = 'species'
    AREA = 'area'
    AGE = 'age'
    SIZE = 'size'
    STATE = 'state'
    ALIVE = 'alive'
