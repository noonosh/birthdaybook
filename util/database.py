import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()


connection = psycopg2.connect(user=os.getenv('DB_USER'),
                              password=os.getenv("DB_PASSWORD"),
                              host=os.getenv("DB_HOST"),
                              port="5432",
                              database=os.getenv("DB_NAME"))
cursor = connection.cursor()
