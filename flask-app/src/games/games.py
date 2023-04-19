from flask import Blueprint, request
from utils import get_query, submit_query

games = Blueprint('game', __name__)

@games.route('/game', methods=['GET'])
def game_name(name):
    if request.method == 'GET':
        return get_query(f"SELECT gameId FROM Game;")

@games.route('/game/<name>', methods=['GET','DELETE'])
def game_name(name):
    if request.method == 'GET':
        return get_query(f"SELECT * FROM Game WHERE gameName = '{name}';")
    
@games.route('/game/<name>/<difficulty>/<projName>', methods=['GET','POST'])
def specific_game(name,difficulty,projName):
    if request.method == 'GET':
        return get_query(f"SELECT * FROM Game WHERE gameName = '{name}' and projectCodeName = '{projName}'\
                              and difficulty = {difficulty};")
    elif request.method == 'POST':
        query = f"INSERT INTO Game (gameName, projectCodeName, difficulty) VALUES('{name}', '{projName}', {difficulty})"
        return submit_query(query, "Inserted")
        
