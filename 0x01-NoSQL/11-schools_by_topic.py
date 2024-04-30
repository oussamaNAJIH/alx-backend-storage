#!/usr/bin/env python3
"""
schools_by_topic module
"""


def schools_by_topic(mongo_collection, topic):
    """
    Python function that returns the list of school having a specific topic
    """
    return [school for school in mongo_collection.find({"topic": topic})]
