#pull from dataset
#push out

import beautifulsoup4
import pandas as pd
import requests
from uci/UCI-ML-API/UCI_ML_Functions import *

#name = name
data = download_dataset_name(name,local_database=None,msg_flag=True,download_flag=True)

#need to clean and do other stuff