from .extensions import db

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    coordinateX = db.Column(db.Integer)
    coordinateY = db.Column(db.Integer)

    @property
    def serialize(self):
        return{
            'id': self.id,
            'coordinateX': self.coordinateX,
            'coordinateY': self.coordinateY,
        }