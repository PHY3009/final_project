import pandas as pd
import sys

savename = sys.argv[1]

filename_1990 = 'data/Earthquake_Datasets/EQCanOB_1990.csv'
filename_2004 = 'data/Earthquake_Datasets/EQCanOB_2004.csv'
filename_2006 = 'data/Earthquake_Datasets/EQCanOB_2006.csv'
filename_2008 = 'data/Earthquake_Datasets/EQCanOB_2008.csv'
filename_2010 = 'data/Earthquake_Datasets/EQCanOB_2010.csv'
filename_2012 = 'data/Earthquake_Datasets/EQCanOB_2012.csv'

earthquakes_1990 = pd.read_csv(filename_1990, sep = ',')
earthquakes_2004 = pd.read_csv(filename_2004, sep = ',')
earthquakes_2006 = pd.read_csv(filename_2006, sep = ',')
earthquakes_2008 = pd.read_csv(filename_2008, sep = ',')
earthquakes_2010 = pd.read_csv(filename_2010, sep = ',')
earthquakes_2012 = pd.read_csv(filename_2012, sep = ',')

def main ():

	all_earthquakes = (earthquakes_1990, earthquakes_2004, earthquakes_2006, earthquakes_2008, earthquakes_2010, earthquakes_2012)

	#loop munge data over all dataframes by calling functions
	for dataframe in all_earthquakes:
		munge (dataframe)

	df_all_earthquakes = pd.concat([earthquakes_1990, earthquakes_2004, earthquakes_2006, earthquakes_2008, earthquakes_2010, earthquakes_2012], ignore_index=True)

	df_all_earthquakes.to_csv(savename)

def munge (data):
    data.ix[:,4] = data.ix[:,4].str.extract('([0-9.]*)').replace('%','',regex=True).astype('float')
    data.ix[:,5] = data.ix[:,5].str.extract('([0-9.]*)').replace('%','',regex=True).astype('float')
    del data['Time(UT)']
    return data

main()