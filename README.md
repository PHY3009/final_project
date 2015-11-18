Final Project
Jessica O'Sullivan, 2015-10-27

To run the program, call the Final_Script.py and pass it the file you want to run, and give it three plot names.

This is the parent file for the final project in Computation for the Physical
Sciences.

The aim of my program is to measure the relationship between fracking in British Columbia,
and earthquakes. I will be examining the relative proximity of earthquake epicenters and 
the fracking sites. I would like to compare the depth of the well and the magnitude of 
the regional earthquakes.
 
The flow of the program is a simple comparison algorithm. In theory, it should be 
applicable to any comparable data. For my own purposes, I will be munging the data with 
separate code attached but not integrated into the comparison code. This munging process 
will be unique to the organization and problems for each data set, and therefore not an 
integral part of the code. This will involve standardizing the data, and making it 
applicable for a statistical comparison. 

Given the nature of my data, I will have the code run a comparison between all the 
possible variables. So if I have variables A, B, C and variables 1, 2, 3, then A will be 
compared with 1, 2 and 3: B will be compared with 1, 2 and 3, and so on. I will be
using an if, than function to sort through data as it is analysed. Therefore, if the 
comparison shows statistical significance, than the analysis will be shown through a 
stats summary and plot. If the comparison is not significant, the data will be stored in
a separate folder. The variables that yield significant results will be scatter plotted, and a
linear regression model will be superimposed on the plot to show the statistical 
significance. 

The variables I will be checking within the earthquake data is: magnitude, depth,
epicenter location and the date. There is also limited information of whether an earthquake 
is induced or natural. If the data suggests the earthquake is induced, I will specifically
be looking at the relationship between the induction and the magnitude of the earthquake.
For the fracking sites, I will be looking at the dates of fracking, the location, and 
(if data is obtainable) the force and depth of the fracking activity.

Dependencies:
1. Bash
2. Python 3.4
