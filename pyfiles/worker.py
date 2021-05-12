#Does anything including the name, ie Adult gets Adult and Autism Screening Adult


from bs4 import BeautifulSoup
import pandas as pd
import requests
import os
import sys


import io


known = 1

def datagrabbr(name):   
    url = "https://data.world/alexandra/" + name

    try:
        urlData = requests.get(url).content
        df = pd.read_csv(io.StringIO(urlData.decode('utf-8')))
        df = pd.DataFrame(df)
        return(df)
        
    except:
        print("Type the right name in")
    #Get to a pd df


#print(datagrabbr("chord-progressions").head(3))