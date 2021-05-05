
import os
from interface import *
from  worker import *
from printr import *
directory = "seeds"
cwd = os.getcwd()
local_directory = cwd + "/uci" + str(directory)
os.makedirs(local_directory)
dataset, buck, instructions = worker.usr_input()

data = worker.datagrabbr(dataset)
print.doit(data, buck)


