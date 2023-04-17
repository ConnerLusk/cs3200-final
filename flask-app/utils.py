from flask import jsonify, make_response,render_template
from src import db

def cursor_to_json(query):
    cursor = db.get_db().cursor()
    cursor.execute(query)

    column_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()

    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

def submit_query(query, message):
    try:
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        myResponse = make_response(message)
        myResponse.status_code = 200
        return myResponse
    except:
        myResponse = make_response("Error")
        myResponse.status_code = 400
        return myResponse