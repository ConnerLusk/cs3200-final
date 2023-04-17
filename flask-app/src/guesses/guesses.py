from flask import Blueprint, request
from utils import cursor_to_json, submit_query


guesses = Blueprint('guesses', __name__)

@guesses.route('/', methods=['GET'])
def guesses():
    return cursor_to_json("SELECT * FROM Guesses")


@guesses.route('/guesses/<attemptId>', methods=['GET'])
def guesses_for_attempt(attemptId):
    return cursor_to_json(f"SELECT * FROM Guesses WHERE attemptId = {attemptId};")

@guesses.route('/guesses/<attemptId>/<submissionNumber>/<row>/<col>', methods=['GET','POST','PUT','DELETE'])
def guesses_for_attempt_specific(attemptId, submissionNumber, row, col):
    if request.method == 'GET':
        return cursor_to_json(f"SELECT * FROM Guesses WHERE attemptId = {attemptId} and valueRow = {row} and\
                              valueColumn = {col} and submissionNumber = {submissionNumber};")
    elif request.method == 'POST':
        data = request.json
        query = f"INSERT INTO Guesses (submissionNumber, attemptId, valueRow, valueColumn, charValue) VALUES \
            ({submissionNumber}, {attemptId}, {row}, {col}, '{data['charValue']}');"
        return submit_query(query, "Updated")
    elif request.method == 'PUT':
        data = request.json
        query = f"UPDATE Guesses SET charValue = '{data['charValue']}' WHERE attemptId = {attemptId} and valueRow = {row} and\
            valueColumn = {col} and submissionNumber = {submissionNumber};"
        return submit_query(query, "Updated")
    elif request.method == 'DELETE':
        query = f"DELETE FROM Guesses WHERE attemptId = {attemptId} and valueRow = {row} and\
            valueColumn = {col} and submissionNumber = {submissionNumber};"
        return submit_query(query, "Deleted")
    
