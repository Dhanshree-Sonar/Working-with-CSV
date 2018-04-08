import csv

# Read file in binary mode(improve portability)
with open('DART_Bus_Stops.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)

    # First row is file header
    header = next(reader)
    print (" ".join(column for column in header))

    # Scan the csv data
    for row in reader:
        print row
