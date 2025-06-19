#!/usr/bin/env python3
"""
Write a Python function that lists all documents in a collection:
"""

def list_all(mongo_collection):
    """
    list_all function
    """

    if mongo_collection.count_documents({}) == 0:
        return []
    else:
        return list(mongo_collection.find())