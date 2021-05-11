#Does anything including the name, ie Adult gets Adult and Autism Screening Adult


from bs4 import BeautifulSoup
import pandas as pd
import requests
import os
import sys


import io

#pyfiles.
from uci import * #download_dataset_url, download_dataset_name
#from uci import *
known = 1

def datagrabbr(name):   
    directory = "lcldata"

    try:
        name = name.replace(" ", "+") 
        url = "https://archive.ics.uci.edu/ml/machine-learning-databases/" + name +"/"

        uci.download_dataset_url(url,directory,msg_flag=True,download_flag=True)
    except:
        print("Type the right name in")
    #Get to a pd df

datagrabbr("seeds")
#data is stored in a folder cwd/name
#need to clean and do other stuff