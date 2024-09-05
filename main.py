import requests
import pprint

def fetch_fbi_wanted_data(page=1):
    url = f"https://api.fbi.gov/wanted/v1/list?page={page}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data['items']
    else:
        return None

def extract_wanted_info(items):
    extracted_data = []
    for item in items:
        title = item.get('title', '')
        subjects = item.get('subjects', [])
        field_offices = item.get('field_offices', [])
        subjects_filtered = ','.join(subjects) if subjects!=None else ''
        field_offices_filtered = ','.join(field_offices) if field_offices!=None else ''
        extracted_data.append(f"{title}þ{subjects_filtered}þ{field_offices_filtered}")
    return extracted_data

page_data = fetch_fbi_wanted_data(page=1)
pprint.pprint(page_data[0])
if page_data:
    formatted_data = extract_wanted_info(page_data)
    for entry in formatted_data:
        print(entry)
else:
    print("Failed to fetch data")
