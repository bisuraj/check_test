import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Extract username and password from environment variables
username = os.getenv('QUALYS_USERNAME')
password = os.getenv('QUALYS_PASSWORD')

# Base URL for the API
base_url = 'https://qualysapi.qg3.apps.qualys.com/api/2.0/fo/asset/host/vm/detection'

# Parameters for the API request
params = {
    'action': 'list',
    'qids': '105335,097,...',  # Replace with actual QIDs
    'output_format': 'CSV',
    'show_igs': '1'
}

# Make the API request
response = requests.get(base_url, params=params, auth=HTTPBasicAuth(username, password))

# Check if the request was successful
if response.status_code == 200:
    # Save the response content to a CSV file
    with open('qualys_detections.csv', 'wb') as file:
        file.write(response.content)
    print('CSV file downloaded successfully.')
else:
    print(f'Failed to download CSV file. Status code: {response.status_code}')
    print(f'Response: {response.text}')
