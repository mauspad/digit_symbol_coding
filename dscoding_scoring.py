# -*- coding: utf-8 -*-
"""
mar 1 2023

@author: mauspad
"""
print("This script loops over every csv in the data directory. IF YOU GET AN ERROR, CHECK TO SEE IF THE CSV IS BUGGED")

#import packages
import pandas as pd
import glob

#set directory
path = "data/*.csv"
for fname in glob.glob(path):

	# turn csv into dataframe
	df = pd.read_csv(fname)

	# list all key responses
	key_resp = df["key_resp.corr"].tolist()

	#sum the correct answers
	Score = sum(key_resp)
	print(fname)
	print(Score)
	