from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db
from utils import submit_query, submit_query

clues = Blueprint('clues', __name__)

# Get all customers from the DB
@clues.route('/clues', methods=['GET'])
def get_clues():
    return submit_query("SELECT * FROM Clues;")

# Get all customers from the DB
@clues.route('/clues/<gameId>', methods=['GET'])
def get_clues_from_game(gameId):
    return submit_query(f"SELECT valueRow, valueColumn, clue, isDown FROM Clues WHERE gameId = {gameId};")

@clues.route('/clues/<gameId>/<valueRow>/<valueColumn>', methods=['GET',"PUT","POST","DELETE"])
def get_clue_from_game(gameId,valueRow,valueColumn):
    if request.method == "GET":
        return submit_query(f"SELECT valueRow, valueColumn, clue, isDown FROM Clues WHERE gameId = {gameId}\
                       AND valueRow = {valueRow} AND valueColumn = {valueColumn};")
    elif request.method == "POST":
        data = request.json
        query = f"INSERT INTO Clues (gameId, valueRow, valueColumn, clue, isDown) VALUES ({gameId},\
              {valueRow}, {valueColumn}, '{data['clue']}', {data['isDown']})"
        return submit_query(query, "Inserted")
    elif request.method == "PUT":
        data = request.json
        query = query = f"UPDATE Clues SET clue = '{data['clue']}' WHERE gameId = {gameId} and valueRow\
              = {valueRow} and valueColumn = {valueColumn}"
        return submit_query(query, "Updated")
    elif request.method == "DELETE":
        data = request.json
        query = f"DELETE FROM Clues WHERE gameId = {gameId} and valueRow = {valueRow} and\
              valueColumn = {valueColumn};"
        return submit_query(query, "Deleted")
    




{"charValue":"f","gameId":2,"gameName":"Crossword","valueColumn":1,"valueRow":0}
[{"charValue":"f","gameId":2,"gameName":"Crossword","valueColumn":1,"valueRow":0}]