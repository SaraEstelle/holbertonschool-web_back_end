#!/usr/bin/env python3
"""Module that lists all documents in a mongoDB collection."""


def list_all(mongo_collection):
    """List all documents in a collection.

    Args:
        mongo_collection: pymongo collection object

    Returns:
        list of docuemnts, or empty list if none
    """
    documents = list(mongo_collection.find())
    return documents
