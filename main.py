import argparse
import sys
import json
import requests

def fetch_fbi_wanted_data(page):
    # Fetches data from the FBI's Wanted API for a specific page number.
    response = requests.get('https://api.fbi.gov/wanted/v1/list', params={'page': page})
    # Converts the response content from JSON string to Python dictionary.
    data = json.loads(response.content)
    return data

def load_data_from_file(file):
    # Loads data from a specified JSON file.
    with open(file, 'r') as f:
        return json.load(f)

def extract_title(item):
    # Extracts the 'title' field from an item, returns an empty string if the title is not found.
    title = item.get('title', '')
    return title if title else ''

def extract_subjects(item):
    # Extracts the 'subjects' field from an item, returns them as a comma-separated string,
    # returns an empty string if no subjects are found.
    subjects = item.get('subjects', [])
    return ','.join(subjects) if subjects else ''

def extract_field_offices(item):
    # Extracts the 'field_offices' field from an item, returns them as a comma-separated string,
    # returns an empty string if no field offices are found.
    field_offices = item.get('field_offices', [])
    return ','.join(field_offices) if field_offices else ''

def print_fbi_data(json_data):
    # Prints data for each item in the provided JSON. Each item's title, subjects, and field offices
    # are printed in a format separated by the thorn character 'þ'.
    for item in json_data['items']:
        title = extract_title(item)
        subjects_filtered = extract_subjects(item)
        field_offices_filtered = extract_field_offices(item)
        print(f"{title}þ{subjects_filtered}þ{field_offices_filtered}")

def main(page=None, file=None):
    # Main function to handle fetching data based on command line arguments for either page number or file.
    if page is not None:
        # Fetch data based on page number if provided.
        json_data = fetch_fbi_wanted_data(page)
    elif file is not None:
        # Load data from file if provided.
        json_data = load_data_from_file(file)
    else:
        # Exit if neither page nor file is specified.
        return

    # Print the fetched or loaded data.
    print_fbi_data(json_data)

if __name__ == '__main__':
    # Set up argument parser to parse command-line arguments.
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str, required=False, help="File location to read from specified")
    parser.add_argument("--page", type=int, required=False, help="Page number to fetch data from the FBI API")

    args = parser.parse_args()

    # Call main function based on provided arguments.
    if args.page:
        main(page=args.page)
    elif args.file:
        main(file=args.file)
    else:
        # Print help if no arguments are provided.
        parser.print_help(sys.stderr)
