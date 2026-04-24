#!/usr/bin/env python3
"""Module that inserts a new document in a MongoDB collection"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a MongoDB collection based on kwargs
    Args:
        mongo_collection: the pymongo collection object
        **kwargs:  key/value pairs of the new document to insert
    Returns:
        The new _id of the new document
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
