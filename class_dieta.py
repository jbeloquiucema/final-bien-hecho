class Dieta:

    def __init__(self, id, restriction, restriccion, USD) -> None:
        self.id = id
        self.restriction = restriction
        self.restriccion = restriccion
        self.USD = USD

    def serialize(self):
        return {
            'id': self.id,
            'restriction': self.restriction,
            'restriccion': self.restriccion,
            'USD': self.USD
        }

    def serialize_details(self):
        return {
            'id': self.id,
            'restriccion': self.restriccion,
            'USD': self.USD
        }
