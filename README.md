# FBI Data Extraction and Modification

Name: Ishtmeet Singh Arora

## Project Description

This project is focused on retrieving and reformatting data from the FBI’s Most Wanted API. The goal is to build a Python package that, when provided with a page number or a local JSON file, fetches data about wanted individuals and outputs a thorn-separated CSV file. The data contains important fields like the name or title of the wanted individual, the subjects related to the case, and the FBI field offices handling the case. The program is designed to extract this information and print it to the console in the specified format.

## How to install

pipenv install -e .

## How to run

pipenv run python main.py --page <integer>

OR

pipenv run python main.py --file <file-location>

## Functions

fetch_fbi_wanted_data(page): Fetches data from the FBI API for a given page number.

load_data_from_file(file): Loads and returns data from a specified local JSON file.

extract_title(item): Extracts the title field from the provided item (or returns an empty string if not present).

extract_subjects(item): Extracts the subjects field and returns it as a comma-separated string.

extract_field_offices(item): Extracts the field_offices field and returns it as a comma-separated string.

print_fbi_data(json_data): Prints the extracted data in the thorn-separated format to the console.

main(page=None, file=None): Orchestrates the logic for fetching or loading data and printing the result.


