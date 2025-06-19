
from bs4 import BeautifulSoup # pip install beautifulsoup4
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import pandas as pd
pd.set_option("display.max_rows", None, "display.max_columns", None)
import re
import json
from datetime import datetime
import os

url = "https://earthquake.phivolcs.dost.gov.ph/"
page = requests.get(url, verify=False)
soup = BeautifulSoup(page.text, 'html.parser')

def is_row_valid(row):
    if row == None:
        return False
    if len(row) < 70:
        return False

    invalid_starts = ["PHIVOLCS", "JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC", "Jan", "Date", "199", "200", "201", "202", "203", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    invalid_phrases = ["SEISMICITY MAPS", "PHIVOLCS LATEST", "Seismological Observation"]

    for word in invalid_starts:
        if row.startswith(word):
            return False

    for phrase in invalid_phrases:
        if phrase in row:
            return False

    return True
    
def extract_data(input_str):
    # Regular expression patterns for the different parts
    datetime_pattern = r"^\d{2} \w+ \d{4} - \d{2}:\d{2} [AP]M"
    float_two_decimal_pattern = r"(\d{2}\.\d{2})"
    float_three_decimal_pattern = r"(\d{3}\.\d{2})"
    whole_number_pattern = r"(\d{3})"
    float_one_decimal_pattern = r"(\d\.\d)"
    remainder_pattern = r"\d{3}\s+\w+.*"

    # Extract datetime
    datetime_match = re.match(datetime_pattern, input_str)
    output1 = datetime_match.group(0) if datetime_match else ""

    # Remove the datetime part from the string for further processing
    remainder_str = input_str[len(output1):].strip()

    # Extract floating numbers with two decimal places
    float_two_decimal_match = re.match(float_two_decimal_pattern, remainder_str)
    output2 = float_two_decimal_match.group(0) if float_two_decimal_match else ""

    # Remove the float_two_decimal part from the string
    remainder_str = remainder_str[len(output2):].strip()

    # Extract floating numbers with three decimal places
    float_three_decimal_match = re.match(float_three_decimal_pattern, remainder_str)
    output3 = float_three_decimal_match.group(0) if float_three_decimal_match else ""

    # Remove the float_three_decimal part from the string
    remainder_str = remainder_str[len(output3):].strip()

    # Extract whole number
    whole_number_match = re.match(whole_number_pattern, remainder_str)
    output4 = whole_number_match.group(0) if whole_number_match else ""

    # Remove the whole number part from the string
    remainder_str = remainder_str[len(output4):].strip()

    # Extract floating numbers with one decimal place
    float_one_decimal_match = re.match(float_one_decimal_pattern, remainder_str)
    output5 = float_one_decimal_match.group(0) if float_one_decimal_match else ""

    # Remove the float_one_decimal part from the string
    remainder_str = remainder_str[len(output5):].strip()

    # The remainder is the final output
    output6 = remainder_str

    return output1, output2, output3, output4, output5, output6

years = [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
years.reverse()
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
months.reverse()

dict_history = {
    'Datetime': [],
    'Latitude': [],
    'Longitude': [],
    'Depth': [],
    'Magnitude': [],
    'Location': []
}
df_history = pd.DataFrame(dict_history)

for year in years:
  for month in months:
    #print(f"Scraping on {year} {month}")
    url_history = f"https://earthquake.phivolcs.dost.gov.ph/EQLatest-Monthly/{year}/{year}_{month}.html"
    page_history = requests.get(url_history, verify=False)
    
    if page_history.status_code == 200:
        soup_history = BeautifulSoup(page_history.text, 'html.parser')

        rows_portion = soup_history.find_all('tr')

        datetimes_portion = []
        latitudes_portion = []
        longitudes_portion = []
        depths_portion = []
        magnitudes_portion = []
        locations_portion = []

        for i in rows_portion:
            row = i.text.replace('\n', '').replace('\t', '').replace('  ', '').replace('\r', '').replace('<', '').replace('>', '')

            try:
                if is_row_valid(row):
                    extracted_row = extract_data(row)
                    datetimes_portion.append(extracted_row[0])
                    latitudes_portion.append(extracted_row[1])
                    longitudes_portion.append(extracted_row[2])
                    depths_portion.append(extracted_row[3])
                    magnitudes_portion.append(extracted_row[4])
                    locations_portion.append(extracted_row[5])
                    #print(f"valid row: {row}")
            except:
                print(f"ROW INVALID: {row}")

        dict_portion = {
            'Datetime': datetimes_portion,
            'Latitude': latitudes_portion,
            'Longitude': longitudes_portion,
            'Depth': depths_portion,
            'Magnitude': magnitudes_portion,
            'Location': locations_portion
        }
        df_portion = pd.DataFrame(dict_portion)
        df_history = pd.concat([df_history, df_portion])

base_dir = os.path.dirname(__file__)
metadata_path = os.path.join(base_dir, "metadata.json")

with open(metadata_path, "r") as f:
    metadata = json.load(f)

current_version = metadata["data_version"]
new_version = current_version + 1
time_scraped = datetime.now().isoformat()

file_name = f"earthquake_ph_list_v{new_version}.csv"
df_history.to_csv(file_name, index=False)

metadata = {
    "data_version": new_version,
    "last_scraped": time_scraped,
    "output_file": file_name
}

with open(metadata_path, "w") as f:
    json.dump(metadata, f, indent=4)
