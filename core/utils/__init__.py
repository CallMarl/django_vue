import json

from collections.abc import Iterable

from django.core import serializers
from django.db import connection

'''
Transform a django instance model into json. Foreign Keys are not included
'''
def model_to_json(models) :
    if isinstance(models, Iterable) :
        list    = []
        data    = json.loads(
            serializers.serialize(
                'json',
                models, use_natural_primary_keys = True
                )
            )
        for row in data :
            dict = {"pk" : row['pk']}
            dict.update(row['fields'])
            list.append(dict)
    else :
        list    = {}
        data    = json.loads(
            serializers.serialize(
                'json',
                [models, ],
                use_natural_primary_keys = True))
        for row in data :
            dict = {"pk" : row['pk']}
            dict.update(row['fields'])
            list = dict
    return list

'''
This function enable to display sql query done with django ORM.
'''
def display_sql() :
    for sql in connection.queries :
        print(sql.get('sql'))
        print("\n")
