'''
script to ingest RDS logs and write them to Loki
'''

import boto3
import time
import os

# AWS credentials and region
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID', 'default_access_key')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY', 'default_secret_key')
region_name = os.getenv('AWS_REGION', 'us-west-2')


# RDS instance identifier
db_instance_identifier = 'rds-loki-test-db'

# Function to continuously fetch and print logs
def fetch_and_print_rds_logs():
    client = boto3.client('rds', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)

    # Use a marker to keep track of the last read log event
    marker = None

    while True: #infinite loop; which can be used to collect the FileLastWritten marker and set the value; should also consider when application fails/restarts to store the marker in PVC or something
        try:
            # Describe the available log files
            #response = client.describe_db_log_files(DBInstanceIdentifier=db_instance_identifier, FileLastWritten=marker)
            response = client.describe_db_log_files(DBInstanceIdentifier=db_instance_identifier)

            log_files = response.get('DescribeDBLogFiles', [])
            if not log_files:
                print("No log files available.")
                time.sleep(10)  # Sleep for a while before checking again
                continue
            print("Available log files: {}".format([f['LogFileName'] for f in log_files]))

            # Get the most recent log file
            latest_log = max(log_files, key=lambda x: x['LastWritten'])

            #set the marker to the last written value; might not be needed since the latest log file is being retrieved always
            marker = latest_log['LastWritten'] 

            # Fetch and print the log content by invoking the RDS API
            log_data = client.download_db_log_file_portion(
                DBInstanceIdentifier=db_instance_identifier,
                LogFileName=latest_log['LogFileName']
            )

            # Print the log data if it exists
            if log_data.get('LogFileData'):
                log_lines = log_data['LogFileData'].split('\n')
                for line in log_lines:
                    print(line.strip())

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(10)  # Sleep for a while before retrying

if __name__ == "__main__":
    print(f"Monitoring logs for RDS instance: {db_instance_identifier}")
    fetch_and_print_rds_logs()
