
from google.cloud import storage

def create_bucket(bucket_name, location="US_CENTRAL1", storage_class="STANDARD"):
    """Creates a new bucket in the specified location."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    bucket.location = location
    bucket = storage_client.create_bucket(bucket)

    print(f"Bucket {bucket.name} created in {bucket.location}.")