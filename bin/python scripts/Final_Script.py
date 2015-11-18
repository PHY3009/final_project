##Jessica O'Sullivan, 2015-11-18
## a script for munging and plotting data input by the user. 

# import libraries
import pandas as pd
import matplotlib.pyplot as plt
import sys

#define the main function
def main ():

	#set variables for user input
	input_file = sys.argv[1]
	savename = sys.argv[2]
	savename_2 = sys.argv[3]
	scatter_save = sys.argv[4]
	
	#set variable for the user inputted data
	earthquake = upload_file(filename = input_file)
	
	#run function, date_time, to change column to DateTime dtype
	date_time (earthquake)
	
	munge (earthquake)
	
	#run function to plot magnitude by date and save the figure
	magnitude_over_time (earthquake, savename)
	
	#change the index of the dataset to DateTime
	index (earthquake)
	
	#plot a map scatter plot in which area of bubbles represent the magnitudes of earth-
	#quakes set to coordinates on a map of the area
	scatter_plot (earthquake, scatter_save)

#uploads data to be used to set variables
def upload_file(filename):
	data = pd.read_csv(filename, sep = ',')
	return data

#change the first column of the dataset to a DateTime dtype
def date_time (data):
    data = pd.to_datetime(data.ix[:,0], )   
    return data

def munge (data):
    data.ix[:,4] = data.ix[:,4].str.extract('([0-9.]*)').replace('%','',regex=True).astype('float')
    data.ix[:,5] = data.ix[:,5].str.extract('([0-9.]*)').replace('%','',regex=True).astype('float')
    del data['Time(UT)']
    return data

#plot the Date and Magnitude of earthquakes as a linegraph
def magnitude_over_time (data, savename):
	plt.figure(figsize=(14,6))
	myplot = plt.plot(data.index, data.Mag)
	#provide labels and titles for the graph
	plt.title ('Magnitude of Earthquakes over Time')
	plt.xlabel ('Date')
	plt.ylabel ('Magnitude')
	plt.savefig(savename)

#groupby year so we can access the summary of a year of data if we want
def index (data):
	year = pd.DatetimeIndex(data['Date']).year
	data.groupby(year)
	return data


#creates a scatter plot that will show magnitude and locations of earthquakes
def scatter_plot(data, scatter_save):
    
    #set the x and y as longitude and latitude so points inside graph correlate with
    #coordinates of earthquakes. The area of a bubble is determined by the Magnitude of
    #the earthquake. *1000 increases visibility but relative size is still accurate
    x = (data.Long)
    y = (data.Lat)
    colors = 'c'
    area = (data.Mag)*1000

    fig = plt.figure(figsize=(30,20))

    ax = fig.add_subplot(1,1,1)
    
    #set the background of the plot to represent an accurate map to coordinates
    im = plt.imread('map_background_copy.jpg')
    implot = plt.imshow(im, extent=[-128, -120, 53, 59])
     
    #change plot size to focus in on region of interest and align the sides of the 
    #map with coordinates so earthquakes will be plotted accurately.            
    ax.scatter(x, y, s=area, c=colors)
    plt.xlim(-128, -120)
    plt.ylim(53, 59)

    plt.savefig(scatter_save)

main()