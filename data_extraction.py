#Data_extraction
import pandas as pd
import tabula
import requests
import json
import boto3

class DataExtractor:
    def __init__(self):
        pass
    def read_rds_table(self, engine, table_name):
           
            users = pd.read_sql_query(f'''SELECT * FROM {table_name}''', engine).set_index('index')
            print(users.columns)
            users.to_string('uncleaned_users.txt')
            return users
    def retrieve_pdf_data(self,link):
        dfs = tabula.read_pdf(link, pages='all')
        df = pd.concat(dfs)
        return df
    def list_number_of_stores(self):
         api_dict = {'x-api-key':'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'}
         api_fetch = requests.get('https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores',headers=api_dict)
         api_json = api_fetch.json()
         num_stores = api_json['number_stores']
         return num_stores
    def retrieve_stores_data(self,store_endpoint):
         api_dict = {'x-api-key':'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'}
         api_fetch_list=[]
         for i in range(451):
              api_fetch = requests.get(f'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{i}', headers=api_dict)
              api_fetch_list.append(api_fetch.json())
         api_df = pd.DataFrame(api_fetch_list)
         return api_df
    def extractfroms3(self):
         BUCKET_NAME = 'data-handling-public'
         KEY = 'products.csv'
         s3 = boto3.resource('s3')
         extracted = s3.Bucket(BUCKET_NAME).download_file(KEY, 's3_extracted.csv')
         products = pd.read_csv('s3_extracted.csv')
         products.to_string('product_unclean.csv')
         return products
    def extract_dates(self):
         api_fetch = requests.get('https://data-handling-public.s3.eu-west-1.amazonaws.com/date_details.json')
         return pd.DataFrame(api_fetch.json())
         
         