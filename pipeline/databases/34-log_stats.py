import pymongo

# Connect to MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.logs
collection = db.nginx

# Total number of logs
total_logs = collection.count_documents({})

# List of HTTP methods in the required order
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

# Calculate counts for each method
method_counts = {method: collection.count_documents({"method": method}) for method in methods}

# Calculate status check count (GET requests to /status)
status_check = collection.count_documents({"method": "GET", "path": "/status"})

# Output the results in the specified format
print(f"{total_logs} logs")
print("Methods:")
for method in methods:
    print(f"\tmethod {method}: {method_counts[method]}")
print(f"{status_check} status check")
