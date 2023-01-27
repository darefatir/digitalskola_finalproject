import requests
import pandas as pd
import logging

class CovidScraper():
    def __init__(self,url):
        self.url=url

    def get_data(self):
        response = requests.get(self.url)
        result = response.json()['data']['content']
        logging.info("Get data from API is completed")
        df = pd.json_normalize(result)
        logging.info("Data from API to dataframe is ready")
        return df