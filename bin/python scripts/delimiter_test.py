import sys

def main():

	input_file = sys.argv[1]

	print ('The delimiter is:', detectDelimiter(input_file))


#figure out what kind of delimiter we have with my current data set for ease of data
#upload configurations

def detectDelimiter(csvFile):
    with open(csvFile, 'r') as myCsvfile:
        header=myCsvfile.readline()
        if header.find(";")!=-1:
            return ";"
        if header.find(",")!=-1:
            return ","
        if header.find("\s+"):
            return "\s+"
        if header.find(''):
            return ""
    #default delimiter (MS Office export)
    return "Other"
    
main()