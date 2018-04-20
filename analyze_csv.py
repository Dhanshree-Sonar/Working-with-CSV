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

##Sample Output:
##
##BJECTID STOPNAME SHAPE STOPID STOPABBR BENCH SHELTER ROUTES COUNTY LON LAT
##Please provide bus no to see the stop names for that particular bus!
##Enter the bus number: 10
##10 number bus stops at 323 stops:
##
##AMTRAK STATION & ML KING-FRENCH
##10TH ST @ MARKET ST
##DEL RT 10 @ LIBERTO IND PARK
##DEL RT 10 & MOORES LAKE SC
##DEL RT 10 & OP MOORES LAKE SC
##DEL RT 10 OP RT 10 PLAZA
##DEL RT 10 @ RT 10 PLAZA
##10TH ST & TATNALL ST
##DEL RT 10 @ WAWA
##BAY RD & BLUE HEN MALL
##PRESIDENT DR @ BAY RD
