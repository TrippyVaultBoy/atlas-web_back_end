#!/usr/bin/env python3
"""
Write a Python script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    logs = client.logs
    
    total_logs = logs.nginx.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = logs.nginx.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    
    status = logs.nginx.count_documents({"method": "GET", "path": "/status"})
    print(f"{status} status check")