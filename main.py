import argparse
import sys
import json
import requests

# Fetches data from the FBI's Wanted API for a specific page number.
def fetch_fbi_wanted_data(page):
    response = requests.get('https://api.fbi.gov/wanted/v1/list', params={'page': page})
    data = json.loads(response.content)
    return data

# Loads data from a specified JSON file.
def load_data_from_file(file):
    with open(file, 'r') as f:
        return json.load(f)

# Extracts the 'title' field from an item, returns an empty string if the title is not found.
def extract_title(item):
    title = item.get('title', '')
    return title if title else ''

# Extracts the 'subjects' field from an item, returns them as a comma-separated string
def extract_subjects(item):
    subjects = item.get('subjects', [])
    return ','.join(subjects) if subjects else ''

# Extracts the 'field_offices' field from an item, returns them as a comma-separated string
def extract_field_offices(item):
    field_offices = item.get('field_offices', [])
    return ','.join(field_offices) if field_offices else ''

 # Prints data for each item in the provided JSON.
def print_fbi_data(json_data): 
    for item in json_data['items']:
        title = extract_title(item)
        subjects_filtered = extract_subjects(item)
        field_offices_filtered = extract_field_offices(item)
        print(f"{title}þ{subjects_filtered}þ{field_offices_filtered}")

# Main function to handle fetching data based on command line arguments for either page number or file.
def main(page=None, file=None):
    if page is not None:
        json_data = fetch_fbi_wanted_data(page)
    elif file is not None:
        json_data = load_data_from_file(file)
    else:
        return

    print_fbi_data(json_data)

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str, required=False, help="File location to read from specified")
    parser.add_argument("--page", type=int, required=False, help="Page number to fetch data from the FBI API")

    args = parser.parse_args()

    if args.page:
        main(page=args.page)
    elif args.file:
        main(file=args.file)
    else:
        parser.print_help(sys.stderr)
