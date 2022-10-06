SIZES = [
    {
        "id": 1,
        "carets": 1,
        "price": 1300    
    },
    {
        "id": 2,
        "carets": 4,
        "price": 5200    
    },
    {
        "id": 3,
        "carets": 2,
        "price": 2600    
    }
]

def get_all_sizes():
    return SIZES

# Function with a single parameter
def get_single_size(id):
    # Variable to hold the found metal, if it exists
    requested_size = None

    # Iterate the METALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for size in SIZES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if size["id"] == id:
            requested_size = size

    return requested_size