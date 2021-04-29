#Does anything including the name, ie Adult gets Adult and Autism Screening Adult


from bs4 import BeautifulSoup
import pandas as pd
import requests
import os
import sys

known = 1
#problem is in mkdir statement, directory that;s passed is an issue
sys.path.append("UCIGrabbr/uci/UCI-ML-API")

from UCI_ML_Functions import *
name = "adult"
directory = "lcldata"

if known ==1:
    name = name.replace(" ", "+") 
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/" + name +"/"

    download_dataset_url(url,directory,msg_flag=True,download_flag=True)
else:
    download_dataset_name(name,msg_flag=True,download_flag=True)
#data is stored in a folder cwd/name
#need to clean and do other stuff