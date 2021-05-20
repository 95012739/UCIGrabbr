#move to place they should be
import os
import uuid as ud
import boto3 as b3
import pandas
import bs4 #beautifulsoup4
import requests

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from redis import Redis
from rq import Queue
#from worker import runTask

import pyfiles.interface as intrf
import pyfiles.worker as wrkr
import pyfiles.printr as prntr
import logging
from botocore.exceptions import ClientError

app = FastAPI()
redis_conn = Redis(host='my_redis', port=6379, db=0)
q = Queue('my_queue', connection=redis_conn)

dataset, buck = intrf.usr_input()
print(dataset)

data = wrkr.datagrabbr(dataset)

prntr.doit(data, buck)

#chord-progressions
