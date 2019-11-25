from ScribbleBase import findRow

database_id = '8'
secret = '2e4e81f3fb6641f9b542ce564dd06a50'
requested_columns = '["lastname", "age"]'
comparison_column = 'age'
comparison = 'IS_LESS_THAN'
operand = '40'

response = findRow(database_id, secret, requested_columns, comparison_column, comparison, operand)

if response.status_code == 200:
    print("Row(s) found!")
    print(response.text)
else:
    print("Failed to find row(s)")
    print(response.text)