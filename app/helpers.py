import pyautogui as pg
from flask import jsonify


def cursor_movement():
    pg.move(5, 0)
    pg.move(5, 0)
    pg.move(5, 0)
    pg.move(-5, 0)
    pg.move(-5, 0)
    pg.move(-5, 0)


def handle_cursor_movement(toggle):
    pg.FAILSAFE_POINTS = [(0, 0)]

    while True:
        x, y = pg.position()
        try:
            if not toggle and pg.onScreen(x, y):
                pg.FAILSAFE_POINTS.append((x, y))
                pg.moveTo(x, y)

            cursor_movement()

        except pg.FailSafeException:
            return jsonify({})