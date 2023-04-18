from flask import Blueprint, request, request
from utils import get_query, submit_query


answers = Blueprint('answers', __name__)


@answers.route('/answers/<gameId>', methods=['GET','DELETE'])
def get_all_answers(gameId):
    if request.method == 'GET':
        return get_query(f'SELECT * FROM Answers WHERE gameId = {gameId}')
    elif request.method == 'DELETE':
        return submit_query(f'DELETE * FROM Answers WHERE gameId = {gameId}', "Deleted")
    


@answers.route('/answers/<gameId>/<ValueRow>/<ValueColumn>', methods=['GET','POST','PUT','DELETE'])
def specific_answer(gameId, ValueRow, ValueColumn):
    if request.method == 'GET':
        return get_query(f'SELECT * FROM Answers WHERE gameId = {gameId} and ValueRow = {ValueRow} and {ValueColumn}')
    
    elif request.method == 'POST':
        the_data = request.json

        gameId = the_data["gameId"]
        gameName = the_data["gameName"]
        ValueRow = the_data["valueRow"]
        ValueColumn = the_data["valueColumn"]
        charValue = the_data["charValue"]

        query = "INSERT INTO Answers (gameId, gameName, ValueRow, ValueColumn, charValue) VALUES ("
        query += f"{gameId}, '{gameName}', {ValueRow}, {ValueColumn}, '{charValue}')"
        
        return submit_query(query, "Inserted")
    
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
        query = f'DELETE * FROM Answers WHERE gameId = {gameId})'
        return submit_query(query, "Deleted")
