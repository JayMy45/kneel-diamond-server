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
    return STYLES

def get_single_style(id):
    requested_style = None
    for style in STYLES:
        if style["id"] == id:
            requested_style = style

    return requested_style