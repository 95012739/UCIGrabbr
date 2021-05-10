
import os
import uuid as ud
import boto3 as b3
import pandas
import bs4 #beautifulsoup4
import requests
import functools
import sys

os.chdir("~/UCIGrabbr")
sys.path.append("/uci/pyfiles")

import interface
import worker 
import printr 
import logging
from botocore.exceptions import ClientError

os.chdir("~/UCIGrabbr")
sys.path.append("/uci/UCI-ML-API/")

from UCI_ML_Functions import download_dataset_url, download_dataset_name

directory = "seeds"
cwd = os.getcwd()
local_directory = cwd + "/uci" + str(directory)

os.makedirs(local_directory)

dataset, buck, instructions = interface.usr_input()

data = worker.datagrabbr(dataset)

printr.doit(data, buck)


