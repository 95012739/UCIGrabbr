#move to place they should be
import os
import uuid as ud
import boto3 as b3
import pandas
import bs4 #beautifulsoup4
import requests

import pyfiles.interface as intrf
import pyfiles.worker as wrkr
import pyfiles.printr as prntr
import logging
from botocore.exceptions import ClientError


dataset, buck, instructions = intrf.usr_input()
print(dataset)
print(instructions)
data = wrkr.datagrabbr(dataset)

#prntr.doit(data, buck)


