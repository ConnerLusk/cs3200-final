from flask import jsonify
from src import db

def cursor_to_json(cursor):
    column_headers = [x[0] for x in cursor.description]
    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))
    
    return jsonify(json_data)

def submit_query(query, message):
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    return message