from flask import Blueprint, request
from utils import submit_query, get_query

clues = Blueprint('clues', __name__)

# Get all customers from the DB
@clues.route('/clues/<gameId>', methods=['GET'])
def get_clues_from_game(gameId):
    return get_query(f"SELECT valueRow, valueColumn, clue, isDown FROM Clues WHERE gameId = {gameId};")

@clues.route('/clues/<gameId>/<valueRow>/<valueColumn>', methods=['GET',"PUT","POST","DELETE"])
def get_clue_from_game(gameId,valueRow,valueColumn):
    if request.method == "GET":
        return get_query(f"SELECT valueRow, valueColumn, clue, isDown FROM Clues WHERE gameId = {gameId}\
                       AND valueRow = {valueRow} AND valueColumn = {valueColumn};")
    elif request.method == "POST":
        data = request.json
        query = f"REPLACE INTO Clues (gameId, valueRow, valueColumn, clue, isDown) VALUES ({gameId}, {valueRow}, {valueColumn},\
            '{data['clue']}', {data['isDown']});"
        
        return submit_query(query, "Inserted")
    elif request.method == "PUT":
        data = request.json
        query = query = f"UPDATE Clues SET clue = '{data['clue']}' WHERE gameId = {gameId} and valueRow\
              = {valueRow} and valueColumn = {valueColumn}"
        return submit_query(query, "Updated")
    elif request.method == "DELETE":
        query = f"DELETE FROM Clues WHERE gameId = {gameId} and valueRow = {valueRow} and\
              valueColumn = {valueColumn};"
        return submit_query(query, "Deleted")
    