#!/usr/bin/env python3
"""
insert_school module
"""


def insert_school(mongo_collection, **kwargs):
    """
    Python function that inserts a new document in a collection based on kwargs
    """
    new_id = mongo_collection.insert_one(kwargs).inserted_id
    return new_id
