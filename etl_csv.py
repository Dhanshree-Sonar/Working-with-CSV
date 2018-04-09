import petl as etl
table = (
    etl
    .fromcsv('Credit_Card_Transactions_for_FY_2017_by_Department.csv')
    .convert('DEPT_NAME', 'lower')
)

print table
