#!/usr/bin/env python3
"""
list_all module
"""


def list_all(mongo_collection):
    """
    Python function that lists all documents in a collection
    """
    list_documents = []
    for document in mongo_collection.find():
        list_documents.append(document)
    return list_documents
