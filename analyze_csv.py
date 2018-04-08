import csv

# Read file in binary mode(improve portability)
with open('DART_Bus_Stops.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)

    # First row is file header
    header = next(reader)
    print (' '.join(column for column in header))

    # Take input from user
    print ('Please provide bus no to see the stop names for that particular bus!')
    bus_no = str(input('Enter the bus number: ' ))

    # Scan the csv data
    stop_names = []
    for row in reader:
        # row[7] (routes) has bus nos which stops at particular bus stop
        if bus_no in row[7]:
            stop_names.append(row[1])

    if stop_names:
        print (bus_no + ' number bus stops at ' + str(len(stop_names))+ ' stops:\n')
        print ('\n'.join(name for name in stop_names))
    else:
        print (bus_no + ' number bus\' stops data not available')
