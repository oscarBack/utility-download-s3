import boto3
import os
from dotenv import load_dotenv

# Load environment variables from .env at import time
load_dotenv()


def download_s3_files(bucket_name, s3_prefix, local_directory):
    s3 = boto3.client('s3')

    # Create the local base directory if it doesn't exist
    os.makedirs(local_directory, exist_ok=True)

    try:
        paginator = s3.get_paginator('list_objects_v2')
        pages = paginator.paginate(Bucket=bucket_name, Prefix=s3_prefix)

        for page in pages:
            if "Contents" in page:
                for obj in page['Contents']:
                    object_key = obj['Key']

                    # Skip S3 "folder" markers which end with a trailing slash
                    if object_key.endswith('/'):
                        print(f"Skipping S3 folder marker: {object_key}")
                        continue

                    # Construct the local file path, maintaining the S3 folder structure
                    # Ensure that the path is relative to the s3_prefix, not the entire bucket
                    relative_path = os.path.relpath(object_key, s3_prefix) if s3_prefix else object_key

                    # If relative_path is '.' or empty, it's a placeholder — skip it
                    if relative_path in ('.', ''):
                        print(f"Skipping placeholder object: {object_key}")
                        continue

                    local_file_path = os.path.join(local_directory, relative_path)

                    # Create any necessary subdirectories
                    os.makedirs(os.path.dirname(local_file_path), exist_ok=True)

                    s3.download_file(bucket_name, object_key, local_file_path)
                    print(f"Downloaded: {object_key} to {local_file_path}")
    except Exception as e:
        print(f"Error during bulk download: {e}")

if __name__ == "__main__":
    # Read configuration from environment (or .env loaded above)
    BUCKET_NAME = os.getenv('BUCKET_NAME')
    if not BUCKET_NAME:
        print("Error: BUCKET_NAME not set in environment or .env")
        raise SystemExit(1)

    S3_PREFIX = os.getenv('S3_PREFIX', '')
    # Default to a local `downloaded_files` folder when not provided
    LOCAL_DIRECTORY = os.getenv('LOCAL_DIRECTORY') or os.path.join(os.getcwd(), 'downloaded_files')

    print(f"Starting download from s3://{BUCKET_NAME}/{S3_PREFIX} to {LOCAL_DIRECTORY}")
    download_s3_files(BUCKET_NAME, S3_PREFIX, LOCAL_DIRECTORY)
    print("Download complete.")
