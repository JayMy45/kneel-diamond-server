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

def get_all_orders():
    return ORDERS

#refer to metal_request.py for function details
def get_single_order(id):
    requested_order = None
    for order in ORDERS:
        if order["id"] == id:
            requested_order = order

    return requested_order

def create_order(order):
    # Get the id value of the last order in the list
    max_id = ORDERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the order dictionary
    order["id"] = new_id

    # Add the order dictionary to the list
    ORDERS.append(order)

    #  Return the dictionary with `id` property added
    return order