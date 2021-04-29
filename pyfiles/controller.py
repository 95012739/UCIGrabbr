
import os
directory = "seeds"
cwd = os.getcwd()
local_directory = cwd + "/uci" + str(directory)
os.makedirs(local_directory)