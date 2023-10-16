from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning

data_connector = DatabaseConnector()
creds=data_connector.read_db_creds('db_creds1.yaml')
print(creds)

engine=data_connector.init_db_engine(creds)
print(engine)

inspector=data_connector.list_db_tables(engine)
print(inspector)

data_extractor = DataExtractor()
users = data_extractor.read_rds_table(engine, 'legacy_users')
print(users)



