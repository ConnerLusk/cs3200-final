from flask import Blueprint, request
from utils import get_query, submit_query, bulk_submit_query
import math

answers = Blueprint('answers', __name__)


@answers.route('/answers/<gameId>', methods=['GET','DELETE'])
def get_all_answers(gameId):
    if request.method == 'GET':
        return get_query(f'SELECT * FROM Answers WHERE gameId = {gameId}')
    


@answers.route('/answers/<gameId>/<ValueRow>/<ValueColumn>', methods=['GET','PUT','DELETE'])
def specific_answer(gameId, ValueRow, ValueColumn):
    if request.method == 'GET':
        return get_query(f'SELECT * FROM Answers WHERE gameId = {gameId} and valueRow = {ValueRow} and valueColumn = {ValueColumn}')
    
    elif request.method == 'PUT':
        the_data = request.json

        gameId = the_data["gameId"]
        gameName = the_data["gameName"]
        ValueRow = the_data["valueRow"]
        ValueColumn = the_data["valueColumn"]
        charValue = the_data["charValue"]


        # use cursor to update answers
        query = f"UPDATE Answers SET gameName = '{gameName}'"
        query += f", charValue = '{charValue}'"
        query += f"WHERE gameId = {gameId} and valueRow = {ValueRow} and valueColumn = {ValueColumn}"

        return submit_query(query, "Updated")
    
    elif request.method == 'DELETE':
        query = f'DELETE FROM Answers WHERE gameId = {gameId} and valueRow = {ValueRow} and valueColumn = {ValueColumn};'
        return submit_query(query, "Deleted")
    
@answers.route('/answers/bulk/<gameId>/<gameName>', methods=['POST'])
def bulkAdd(gameId,gameName):
    data = request.json
    charVals = data["answers"]
    query = []
    for i, val in enumerate(charVals):
        if val != "":
            row = math.floor(i/5)
            col = i % 5
            query.append(f"INSERT INTO Answers (gameId, gameName, valueRow, valueColumn, charValue) VALUES ({gameId}, '{gameName}',{row},{col},'{val}');")
    return bulk_submit_query(query, "Inserted")
