from flask import Blueprint, request, jsonify, make_response
import json
from src import db


players = Blueprint('players', __name__)

# Get all players from the DB
@players.route('/players', methods=['GET'])
def get_players():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT fname, lname FROM Player;')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get player details for players with particular playerID
@players.route('/players/<playerID>', methods=['GET'])
def get_player(playerID):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Player where playerID = {0}'.format(playerID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response
\
# delete a player 
@players.route('/players/<playerID>', methods=['DELETE'])
def delete_player(playerID):
    cursor = db.get_db().cursor()
    cursor.execute('Delete * FROM Player where playerID = {0}'.format(playerID))
    
    return 'deleted'