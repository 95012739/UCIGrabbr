# Import necessary libraries and modules
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from redis import Redis
from rq import Queue
# Uncomment the line below if 'runTask' is defined in 'worker.py'
# from worker import runTask

import pyfiles.interface as intrf  # Import user interface module
import pyfiles.worker as wrkr        # Import worker module for data processing
import pyfiles.printr as prntr       # Import printer module for printing

import logging                       # Import logging module for logging
from botocore.exceptions import ClientError  # Import ClientError from botocore.exceptions

# Create an instance of FastAPI
app = FastAPI()

# Create a connection to Redis
redis_conn = Redis(host='my_redis', port=6379, db=0)

# Create a queue for tasks using RQ and the Redis connection
q = Queue('my_queue', connection=redis_conn)

# Get user input for dataset name and S3 bucket name
dataset, buck = intrf.usr_input()

# Print the dataset name for reference
print(dataset)

# Fetch data based on the dataset name
data = wrkr.datagrabbr(dataset)

# Perform data processing and upload to the specified S3 bucket
prntr.doit(data, buck)

# The following line seems to be a comment or a placeholder for future work
# chord-progressions
