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


class Posicao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    idadeInfo = db.Column(db.String)
    data = db.Column(db.String)
    altitude = db.Column(db.Float)
    velocidade = db.Column(db.Float)
    sentido = db.Column(db.Integer)
    satelites = db.Column(db.Integer)
    precisao = db.Column(db.Integer)

    @property
    def serialize(self):
        return{
            'id': self.id,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'idadeInfo': self.idadeInfo,
            'data': self.data,
            'altitude': self.altitude,
            'velocidade': self.velocidade,
            'sentido': self.sentido,
            'satelites': self.satelites,
            'precisao': self.precisao,
        }
