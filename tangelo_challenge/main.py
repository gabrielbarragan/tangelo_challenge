from functions import create_dataframe, calculate_time_metrics
from database import db_create_table
import requests
import pandas as pd

if __name__ == '__main__':

    countries_languages_data = requests.get('https://restcountries.com/v3.1/all')

    dataframe_languages= create_dataframe(countries_languages_data)

    print(dataframe_languages)

    print(calculate_time_metrics(dataframe_languages))

    # data to export
    languages_db_output = dataframe_languages.itertuples()
    languages_db_data = tuple(languages_db_output)


    #exporting dataframe into sqlite
    dataframe_languages.to_sql('countries', db_create_table, if_exists='replace', index = False)

    #testing data in sqlite databes 
    df_employees = pd.read_sql_query('select * from countries', db_create_table)

    print(df_employees)