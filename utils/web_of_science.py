import os

from dotenv import load_dotenv
import requests

load_dotenv()

# Clarivate API key and endpoint
api_key = os.getenv("CLARIVATE_API_KEY")
doi = '10.1186/s13321-024-00937-7'
url = f'https://api.clarivate.com/apis/wos-starter/v1/documents?q={doi}'

# Set headers including your API key
headers = {
    'X-APIKey': api_key,
    'Accept': 'application/json',
}

# Send GET request to the Clarivate API
response = requests.get(url, headers=headers)

# Check for successful response
if response.status_code == 200:
    data = response.json()

    # Example: Extracting citation count (this structure may vary depending on the API response)
    citation_count = data.get('CitedReferences', {}).get('CitedReference', {}).get('count', 0)

    print(f'Citations for DOI {doi}: {citation_count}')
else:
    print(f'Failed to fetch data. Status Code: {response.status_code}')
    print(response.text)

# TODO: implement this when the API is available

