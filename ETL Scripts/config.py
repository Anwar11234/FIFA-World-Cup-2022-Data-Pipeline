import os
from sqlalchemy import create_engine

server = os.getenv("DB_SERVER")
source_database = os.getenv("SOURCE_DATABASE")
destination_database = os.getenv("DESTINATION_DATABASE")

source_connection_string = f"mssql+pyodbc://{server}/{source_database}?driver=ODBC+Driver+17+for+SQL+Server"
destination_connection_string = f"mssql+pyodbc://{server}/{destination_database}?driver=ODBC+Driver+17+for+SQL+Server"

source_engine = create_engine(source_connection_string)
destination_engine = create_engine(destination_connection_string)