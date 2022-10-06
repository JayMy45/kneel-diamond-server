class Orders():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, styleId, sizeId, metalId, timestamp):
        self.id = id
        self.styleId = styleId
        self.sizeId = sizeId
        self.metalId = metalId
        self.timestamp = timestamp