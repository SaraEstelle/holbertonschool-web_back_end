#!/usr/bin/env python3
"""Module that returns school having a specific topic"""

def schools_by_topic(mongo_collection, topic):
    """Returns the list of school having a specific topic
    Args:
        mongo_collection: the pymongo collection object
        topic: the topic searched
    Returns:
        the list of school having a specific topic
    """
    return list(mongo_collection.find({"topics": topic}))
