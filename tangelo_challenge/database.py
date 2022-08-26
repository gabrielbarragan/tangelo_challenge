import sqlite3

# database connect
db_create_table = sqlite3.connect('countries_languages.db')
database_connection = db_create_table.cursor()

#creating table
database_connection.execute('CREATE TABLE IF NOT EXISTS countries (Region, Country, Languages, time)')
db_create_table.commit()