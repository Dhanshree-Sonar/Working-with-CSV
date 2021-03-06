import petl as etl

table = (
    etl
    .fromcsv('Credit_Card_Transactions_for_FY_2017_by_Department.csv')
    .convert('DEPT_NAME', 'lower')
    .addfield('APPROX_AMT_K', lambda row: int(round(float(row.MERCHANDISE_AMT[1:]) / 1000, 0)))
    .addfield('APPROX_AMT', lambda row: '$' + str(row.APPROX_AMT_K) + 'K')
)

new_table = table.cut('DEPT_NAME','APPROX_AMT')

sort_table = etl.sort(new_table, key=['DEPT_NAME'])

print '\nDepartment wise credit transaction for year 2017'
print sort_table


##Sample Output:
##
##Department wise credit transaction for year 2017
##+--------------------------------+------------+
##| DEPT_NAME                      | APPROX_AMT |
##+================================+============+
##| academia antonia alonso        | $18K       |
##+--------------------------------+------------+
##| advisory counc exceptnl citizn | $2K        |
##+--------------------------------+------------+
##| appoquinimink school district  | $774K      |
##+--------------------------------+------------+
##| auditor of accounts            | $78K       |
##+--------------------------------+------------+
##| brandywine school district     | $146K      |
##+--------------------------------+------------+
##
