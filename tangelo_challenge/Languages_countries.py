import requests
import hashlib
import time
import pandas as pd



countries_languages_data = requests.get('https://restcountries.com/v3.1/all')

def get_languages(languages: dict) -> str:
    """
    get languages from a dictionary of languages where name doesn't alone into dictionary

    Arguments:
    languages: is a dict what contains the languages name
    """
    languages_values = languages.values()
    languages_list = list(languages_values)
    all_languages = ','.join(languages_list)
    all_languages_list_string =f"[{all_languages}]"

    return all_languages_list_string

def create_dataframe(countries_languages: dict) -> pd.DataFrame:
    countries_languages = countries_languages.json()
    id=0
    countries_dict=[]
    for country in countries_languages:
        now = time.time()
        if country.get('languages', False) is not False:

            all_languages = get_languages(country['languages'])
            encrypted_languages= (hashlib.sha1(all_languages.encode('utf-8'))).hexdigest()

            country_row = {
                'Region':country['region'],
                'Country':country['name']['common'],
                'Languages':encrypted_languages,
                'time': f"{round(((time.time() - now)*1000),4)} ms"
            }
            countries_dict.append(country_row)
            
    table_dataframe = pd.DataFrame(data= countries_dict)
    print(table_dataframe)

create_dataframe(countries_languages_data)