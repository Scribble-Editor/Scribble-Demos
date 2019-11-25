from ScribbleBase import delRow

database_id = '8'
secret = '2e4e81f3fb6641f9b542ce564dd06a50'
comparison_column = 'id'
comparison = 'IS_EQUAL_TO'
operand = '6'

response = delRow(database_id, secret, comparison_column, comparison, operand)

if response.status_code == 200:
    print("Row(s) deleted!")
    print(response.text)
else:
    print("Failed to delete row(s)")
    print(response.text)