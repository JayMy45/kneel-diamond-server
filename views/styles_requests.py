import sqlite3
import json
from models import Styles

STYLES = [
    {
        "id": 1,
        "styles": "Solitaire",
        "price": 500    
    },
    {
        "id": 2,
        "styles": "Princess",
        "price": 1000    
    },
    {
        "id": 3,
        "styles": "Emerald",
        "price": 1500    
    }
]

def get_all_styles():
    with sqlite3.connect("./kneel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
                s.id,
                s.style,
                s.price
        FROM Styles s
        """)
        styles = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            style = Styles(row['id'],
                           row['style'],
                           row['price'])
            styles.append(style.__dict__)
    return styles

def get_single_style(id):
    requested_style = None
    for style in STYLES:
        if style["id"] == id:
            requested_style = style

    return requested_style

def update_style(id, new_style):
    with sqlite3.connect("./kneel.sqlite3") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        UPDATE Styles
            SET
                style = ?,
                price = ?
        WHERE id = ?
        """, (new_style['style'],
              new_style['price'],
              id, ))
        rows_affected = db_cursor.rowcount

        if rows_affected == 0:
            return False
        else:
            return True
        