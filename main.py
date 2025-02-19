import csv, sys, NeedlemanWunschAlgorithm as nwa

# Example of an valid input: py main.py test1.csv

try:
    if(len(sys.argv) > 1):
        with open(sys.argv[1]) as file:
            # This makes sure that the lines are read as an csv file.
            csvFile = csv.reader(file)

            # This omits the first row on the csv document.
            file.readline()

            for lines in csvFile: 
                nwa.printOutput(lines)
        file.close()
    else:
        print("Invalid input; this only works with a .csv file as an input on the command line.")
except:
    print('An error has ocurred while reading the previous input.')
