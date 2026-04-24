#!/usr/bin/env python3
"""Provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx = client.logs.nginx

    total = nginx.count_documents({})
    print("{} logs".format(total))

    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = nginx.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    status_count = nginx.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(status_count))
