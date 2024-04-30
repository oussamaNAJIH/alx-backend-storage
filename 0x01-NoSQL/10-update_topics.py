#!/usr/bin/env python3
"""
update_topics module
"""


def update_topics(mongo_collection, name, topics):
    """
    Python function that changes all topics of a
    school document based on the name
    """
    result = mongo_collection.find({"name": name})
    if result:
        mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}})
