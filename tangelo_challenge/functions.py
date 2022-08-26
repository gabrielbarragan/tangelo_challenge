import requests
import hashlib
import time
import pandas as pd
import sqlite3

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
    countries_list=[]
    for country in countries_languages:
        now = time.time()
        if country.get('languages', False) is not False:

            all_languages = get_languages(country['languages'])
            encrypted_languages= (hashlib.sha1(all_languages.encode('utf-8'))).hexdigest()

            country_row = {
                'Region':country['region'],
                'Country':country['name']['common'],
                'Languages':encrypted_languages,
                'time': round(((time.time() - now)*1000),4)
            }
            countries_list.append(country_row)
            
    table_dataframe = pd.DataFrame(data= countries_dict)
    return table_dataframe


dataframe_languages= create_dataframe(countries_languages_data)

print(dataframe_languages)

sum_time = dataframe_languages['time'].sum()
avg_time = dataframe_languages['time'].mean()
min_time = dataframe_languages['time'].min()
max_time = dataframe_languages['time'].max()

print(f"Suma: {sum_time}, Promedio: {avg_time}, Mínimo: {min_time}, Máximo: {max_time}")

# data to export
languages_db_output = dataframe_languages.itertuples()
languages_db_data = tuple(languages_db_output)

# database connect

db_create_table = sqlite3.connect('countries_languages.db')
database_connection = db_create_table.cursor()
#creating table
database_connection.execute('CREATE TABLE IF NOT EXISTS countries (region, country, languages, time)')
db_create_table.commit()

#exporting dataframe into sqlite
dataframe_languages.to_sql('countries', db_create_table, if_exists='replace', index = False)

#testing data in sqlite databes 
df_employees = pd.read_sql_query('select * from countries', db_create_table)

print(df_employees)