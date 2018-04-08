import csv

# Read file in binary mode(improve portability)
with open('DART_Bus_Stops.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)

    # First row is file header
    header = next(reader)
    print (' '.join(column for column in header))

    # Take input from user
    print ('Please provide bus no to see the stop names for that particular bus!')
    bus_no = input('Enter the bus number: ' )

    # Scan the csv data
    for row in reader:
        print row
