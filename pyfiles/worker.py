# Grabs anything including the name, i.e., Adult gets Adult and Autism Screening Adult

# Packages
from bs4 import BeautifulSoup
import pandas as pd
import requests
import os
import sys
import io

# Flag to indicate if the data source is known
known = 1

def datagrabbr(name):
    """
    Fetches data from a URL based on the provided 'name' and returns it as a Pandas DataFrame.
    
    Parameters:
    - name: str, the name to be used in the URL for data retrieval.

    Returns:
    - DataFrame: Pandas DataFrame containing the fetched data.
    """
    
    # Construct the URL for data retrieval
    url = "https://data.world/alexandra/" + name

    try:
        # Get data from the URL and decode it as utf-8
        urlData = requests.get(url).content
        df = pd.read_csv(io.StringIO(urlData.decode('utf-8')))
        df = pd.DataFrame(df)
        return df

    # Handle exceptions, such as typos in the provided name
    except:
        print("Type the right name in")

# Example usage:
# data = datagrabbr("example_data")
# print(data.head())
