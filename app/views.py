import json

import pyautogui as pg
from flask import Blueprint, render_template, request, jsonify

from app.helpers import handle_cursor_movement

views = Blueprint('views', __name__)


@views.route('/')
def home():
    screen_size = pg.size()
    return render_template('home.html', screen_size=screen_size)


@views.route('/start', methods=['POST'])
def move_cursor():
    toggle = json.loads(request.data)['toggle']

    handle_cursor_movement(toggle)
    return jsonify()
