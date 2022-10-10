import csv
fs



def readcsv_file(screen.csv):
    #create an empty list
    datalist = []
    
    #open csv file
    csvdata = open(screen.csv, "r")
    
    #create a reader
    reader = csv.reader(csvdata)
    
    #skip the header
    next(reader)
    #add csv row to the list
    for rows in reader:
        datalist.append(row)
    return datalist
    
    
print(readcsv_file(screen.csv))