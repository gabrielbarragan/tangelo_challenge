import requests
import hashlib
import time


countries_languages = requests.get('https://restcountries.com/v3.1/all')

countries_languages = countries_languages.json()

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


for country in countries_languages:
    now = time.time()
    if country.get('languages', False) is not False:

        all_languages = get_languages(country['languages'])
        encrypted_languages= (hashlib.sha1(all_languages.encode('utf-8'))).hexdigest()

        row = {
            'Region':country['region'],
            'Country':country['name']['common'],
            'Languages':encrypted_languages,
            'time': f"{round(((time.time() - now)*1000),4)} ms"
        }
        print(row)
        # last_time = round(((time.time() - now)*1000),4)

        
            # print(f"{country['region']};{country['name']['common']};{encrypted_languages};{last_time} ms")
            
    


