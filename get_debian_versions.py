import requests
from datetime import *
import json

def get_debian_details():
    url = f"https://endoflife.date/api/debian.json"
    header = { "Accept": "application/json",  }
    response = requests.request("GET", url, headers=header)
    return json.loads(response.text)

def get_lts_details(debian_details: list):
    lts_details = []

    for item in debian_details:
        eol = date.fromisoformat(item['eol'])
        today = date.today()
        if eol > today:
            lts_details.append(item)
    
    return lts_details

if __name__ == "__main__":
    debian_details = get_debian_details()
    lts_details = get_lts_details(debian_details)

    lts_versions = [int(lts['latest']) for lts in lts_details]

    output = {
        'lts_versions':  lts_versions,
        'lts_min':       min(lts_versions),
        'lts_max':       max(lts_versions)
    }

    print(json.dumps(output, indent=4, sort_keys=True))