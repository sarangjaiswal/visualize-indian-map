# import library (if these are not installed then install them using requirements.txt)
import pandas as pd
import os
import sqlite3

# get current directory path
cur_dir = os.path.dirname(os.path.realpath(__file__))

# sqlite3 db path
db = sqlite3.connect(cur_dir + '/db/india_geonames.db')

# reading a txt the data and adding the data into sqlite3 db
chunks = pd.read_csv(cur_dir + '/data/IN/IN.txt', sep='\t', header=None, chunksize=1000)
for chunk in chunks:
    chunk.to_sql('india', db, if_exists='replace')
