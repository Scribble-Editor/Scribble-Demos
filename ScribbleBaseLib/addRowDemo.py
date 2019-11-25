from ScribbleBase import addRow

database_id = '<DATABASE_ID>'
secret = '<SECRET>'
row = { "firstname": "John", "lastname": "Smith", "salary": "$60,000" }

response = addRow(database_id, secret, row)

if response.status_code == 200:
    print("Row successfully inserted")
else:
    print("Failed to add row")
    print(response.text)