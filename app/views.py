import json

import pyautogui as pg
from flask import Blueprint, render_template, request, jsonify

views = Blueprint('views', __name__)


@views.route('/')
def home():
    screen_size = pg.size()
    return render_template('home.html', screen_size=screen_size)


@views.route('/start', methods=['POST'])
def move_cursor():
    toggle = json.loads(request.data)['toggle']
    pg.FAILSAFE_POINTS = [(0, 0)]

    while True:
        x, y = pg.position()
        try:
            if not toggle and pg.onScreen(x, y):
                pg.FAILSAFE_POINTS.append((x, y))
                pg.moveTo(x, y)

            pg.move(0, 5)

        except pg.FailSafeException:
            return jsonify({})
