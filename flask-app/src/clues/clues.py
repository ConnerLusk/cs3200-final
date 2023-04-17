from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db
from utils import cursor_to_json, submit_query

clues = Blueprint('clues', __name__)

# Get all customers from the DB
@clues.route('/clues', methods=['GET'])
def get_clues():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT gameId, clue FROM Clues;')
    return cursor_to_json(cursor)

# Get all customers from the DB
@clues.route('/clues/<gameId>', methods=['GET'])
def get_clues_from_game(gameId):
    cursor = db.get_db().cursor()
    cursor.execute(f'SELECT valueRow, valueColumn, clue, isDown FROM Clues WHERE gameId = {gameId};')
    return cursor_to_json(cursor)

@clues.route('/clues/<gameId>/<valueRow>/<valueColumn>', methods=['GET',"PUT","POST","DELETE"])
def get_clue_from_game(gameId,valueRow,valueColumn):
    cursor = db.get_db().cursor()
    if request.method == "GET":
        cursor.execute(f'SELECT valueRow, valueColumn, clue, isDown FROM Clues WHERE gameId = {gameId}\
                   AND valueRow = {valueRow} AND valueColumn = {valueColumn};')
        return cursor_to_json(cursor)
    elif request.method == "PUT":
        data = request.json
        query = f'''INSERT INTO Clues (gameId, valueRow, valueColumn, clue, isDown) VALUES ({gameId}, {valueRow}, {valueColumn}, '{data["clue"]}', {data["isDown"]})'''
        return submit_query(query, "Inserted")
    elif request.method == "POST":
        print("post")
    elif request.method == "DELETE":
        data = request.json
        query = f"DELETE FROM Clues WHERE gameId = {gameId} and valueRow = {valueRow} and valueColumn = {valueColumn};"
        return submit_query(query, "Deleted")