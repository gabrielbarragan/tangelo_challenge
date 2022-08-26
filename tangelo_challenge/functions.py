import pandas as pd
import hashlib, time
import requests

def get_languages(languages: requests.models.Response) -> str:
    """
    get languages from a dictionary of languages where name doesn't alone into dictionary.\n

    Arguments:
    languages: is a dict that contains the languages names.\n

    Return:
    String as a list of  languages names
    """
    languages_values = languages.values()
    languages_list = list(languages_values)
    all_languages = ','.join(languages_list)
    all_languages_list_string =f"[{all_languages}]"

    return all_languages_list_string

def create_dataframe(countries_languages: dict) -> pd.DataFrame:
    """
    Creating a Pandas DataFrame from a dict with countries and languages.\n
    Arguments:
    countries_languages: is a dict that contains information about countries obtained from the restcountries endpoint <<https://restcountries.com/v3.1/all>>.\n
    Return:
    Pandas DataFrame with fields: Region, Country, Languages, time
    """
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
            
    table_dataframe = pd.DataFrame(data= countries_list)
    return table_dataframe


def calculate_time_metrics(dataframe: pd.DataFrame) -> str:
    """
    Calculating mean, sum, min and max of a DataFrame that contain a time value in milliseconds.\n
    Arguments:
    dataframe: DataFrame that contain a time value in milliseconds.\n
    Return:
    calculated values as a string
    """
    sum_time = dataframe['time'].sum()
    avg_time = round(dataframe['time'].mean(),4)
    min_time = dataframe['time'].min()
    max_time = dataframe['time'].max()

    return (f"Suma: {sum_time}, Promedio: {avg_time}, Mínimo: {min_time}, Máximo: {max_time}")

def dataframe_to_json_file(data_frame: pd.DataFrame):
    """
    takes a dataframe and converts it into json format and then generates a data.json file with this data.\n
    Arguments:
    dataframe: DataFrame object.\n
    Return:
    finished message and file with the dataframe data
    """

    dataframe_json= data_frame.to_json(orient= 'records')
    
    with open('data.json', 'w') as myFile:
        try:
            myFile.write(dataframe_json)
            print('finished')
        except:
            raise "Algo pasó al crear el archivo, vuelve a intentarlo o contacta al administrador."
    