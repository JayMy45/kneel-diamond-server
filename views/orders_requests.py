import sqlite3
import json
from models import Orders
from views.sizes_requests import get_single_size
from views.styles_requests import get_single_style
from views.metal_request import get_single_metal

# from sizes_requests import get_single_size

ORDERS = [
    {
        "id": 1,
        "styleId": 1,
        "sizeId": 3,
        "metalId": 2,
        "timestamp": 1665087278
    },
    {
        "id": 2,
        "styleId": 2,
        "sizeId": 1,
        "metalId": 1,
        "timestamp": 1665087278   
    } 
]

# Get All Orders (GET)
def get_all_orders():
    with sqlite3.connect("./kneel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            o.id,
            o.style_id,
            o.size_id,
            o.metal_id,
            o.price,
            o.timestamp
        FROM Orders o
        """)

        orders = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            order = Orders(row['id'],
                           row['style_id'],
                           row['size_id'],
                           row['metal_id'],
                           row['price'],
                           row['timestamp'])
                           
            orders.append(order.__dict__)
    
    return orders

# Get Single order (GET)
def get_single_order(id):
       with sqlite3.connect("./kneel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            o.id,
            o.style_id,
            o.size_id,
            o.metal_id,
            o.price,
            o.timestamp
        FROM Orders o
        WHERE o.id = ?
        """, ( id, ))

        data = []

        data = db_cursor.fetchone()

        order = Orders(data['id'],
                        data['style_id'],
                        data['size_id'],
                        data['metal_id'],
                        data['price'],
                        data['timestamp'])
                           
        return order.__dict__   

# Create New Orders (POST)
def create_order(new_order):
    with sqlite3.connect("./kneel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Orders
            (style_id, size_id, metal_id, price, timestamp)
        VALUES
            ( ?, ?, ?, ?, ?);
        """, (new_order['style_id'],
              new_order['size_id'],
              new_order['metal_id'],
              new_order['price'],
              new_order['timestamp'], ))
        id = db_cursor.lastrowid
        new_order['id'] = id

    return new_order

# Delete Single Orders (DELETE)
def delete_order(id):
    with sqlite3.connect("./kneel.sqlite3") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        DELETE FROM orders
        WHERE id = ?
        """, (id,))

# Update Orders (PUT)
def update_order(id, new_order):
    with sqlite3.connect("./kneel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Orders
            SET
                style_id = ?,
                size_id = ?,
                metal_id = ?,
                price = ?,
                timestamp = ?
        WHERE id = ?
        """, (new_order['style_id'],
                new_order['size_id'],
                new_order['metal_id'],
                new_order['price'],
                new_order['timestamp'],
                id, ))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True













# def get_single_order(id):
#     requested_order = None
#     for order in ORDERS:
#         if order["id"] == id:
#             requested_order = order
#             #~* be sure to indent matching below with line of code above

#             #! update single order to include metal details in place of metalId
#             # 1. store matching metal in variable (invoke get_single_metal passing request_order Key: metalId]
#             matching_metals = get_single_metal(requested_order["metalId"])
#             # 2. store results in new key add to requested_order variable.
#             requested_order["metal"] = matching_metals
#             # 3. delete metalId key using del keyword (use order as it is the iterator)
#             del order["metalId"]

#             #! update single order to include metal details in place of metalId
#             matching_styles = get_single_style(requested_order["styleId"])
#             requested_order["style"] = matching_styles
#             del order["styleId"]

#             #! update single order to include metal details in place of metalId
#             matching_sizes = get_single_size(requested_order["sizeId"])
#             requested_order["size"] = matching_sizes
#             del order["sizeId"]

#     return requested_order