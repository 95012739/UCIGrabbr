#move to place they should be
import os
import uuid as ud
import boto3 as b3
import pandas
import bs4 #beautifulsoup4
import requests

from pyfiles.interface import*
import pyfiles.worker 
import pyfiles.printr 
import logging
from botocore.exceptions import ClientError
#pyfiles/interface.py
#UCIGRABBR.pyfiles.
"""directory = "seeds"
cwd = os.getcwd()
local_directory = cwd + "/uci" + str(directory)

os.makedirs(local_directory)"""

dataset, buck, instructions = pyfiles.interface.usr_input()

data = pyfiles.worker.datagrabbr(dataset)

pyfiles.printr.doit(data, buck)


