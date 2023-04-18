from flask import Blueprint
from utils import get_query


gameType = Blueprint('gameType', __name__)

# Get all the game attempts from the database
@gameType.route('/', methods=['GET'])
def game_types():
    return get_query("SELECT * FROM GameType")