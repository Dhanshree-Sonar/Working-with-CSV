import petl as etl
table = (
    etl
    .fromcsv('Credit_Card_Transactions_for_FY_2017_by_Department.csv')
    .convert('DEPT_NAME', 'lower')
    .addfield('APPROX_AMT(K)', lambda row: int(round(float(row.MERCHANDISE_AMT[1:]) / 1000, 0)))
)

new_table = table.cut('DEPT_NAME', 'APPROX_AMT(K)')

print '\nDepartment wise Credit transaction for year 2017'
print new_table
