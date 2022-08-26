from functions import create_dataframe, calculate_time_metrics, dataframe_to_json_file
from database import db_create_table
import requests
import pandas as pd


if __name__ == '__main__':

    #obteniendo datos desde el endpoint 
    countries_languages_data = requests.get('https://restcountries.com/v3.1/all')

    #creando un dataframe con la función createdataframe y los datos obtenidos desde el endpoint.
    dataframe_languages= create_dataframe(countries_languages_data)

    print(dataframe_languages)

    #obteniendo las métricas indicadas (suma, promedio, mínimo y máximo)
    print(calculate_time_metrics(dataframe_languages))
    
    #Exportando el data frame a sqlite en la tabla countries
    dataframe_languages.to_sql('countries', db_create_table, if_exists='replace', index = False)

    #leyendo la información en la tabla countries de la base de datos y obteniendolo como DataFrame
    df_coutries = pd.read_sql_query('SELECT * FROM countries', db_create_table)
    
    #creando el archivo data.json desde el data frame con los datos obtenidos de la tabla countries

    dataframe_to_json_file(df_coutries)

    
    