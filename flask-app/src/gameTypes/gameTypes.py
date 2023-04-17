from flask import Blueprint, request, jsonify, make_response, current_app
from utils import cursor_to_json


gameType = Blueprint('gameType', __name__)

# Get all the game attempts from the database
@gameType.route('/', methods=['GET'])
def game_types():
    return cursor_to_json("SELECT * FROM GameType")