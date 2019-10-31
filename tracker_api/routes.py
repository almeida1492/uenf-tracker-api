# -*- coding: utf-8 -*- a
from flask import Blueprint, jsonify, request

from .extensions import db
from .models import Location, Posicao

main = Blueprint('main', __name__)


@main.route('/')
def root():
    return jsonify(location={
        'coordinateX': 0,
        'coordinateY': 0,
    })


@main.route('/locations')
def locations():
    locations = db.session.query(Location).all()
    if len(locations) > 0:
        return jsonify(locations=[l.serialize for l in locations])
    else:
        return "Empty database"


@main.route('/send', methods=['POST'])
def send():
    body = request.get_json()
    coordinateX = body['coordinateX']
    coordinateY = body['coordinateY']
    location = Location(
        coordinateX=coordinateX,
        coordinateY=coordinateY
    )
    db.session.add(location)
    db.session.commit()

    return jsonify(response={
        'status': 200,
        'message': "Success",
    })


@main.route('/busca')
def busca():
    posicao = db.session.query(Posicao).all()
    if len(posicao) > 0:
        return jsonify(posicao=[p.serialize for p in posicao])
    else:
        return "Não há nada registrado."


@main.route('/atualizas', methods=['POST'])
def envia():
    body = request.get_json()

    latitude = body['latitude']
    longitude = body['longitude']
    idadeInfo = body['idadeInfo']
    data = body['data']
    altitude = body['altitude']
    velocidade = body['velocidade']
    sentido = body['sentido']
    satelites = body['satelites']
    precisao = body['precisao']

    posicao = db.session.query(Posicao).filter_by(id=1).one()

    if len(posicao) > 0:
        posicao.latitude = latitude
        posicao.longitude = longitude
        posicao.idadeInfo = idadeInfo
        posicao.data = data
        posicao.altitude = altitude
        posicao.velocidade = velocidade
        posicao.sentido = sentido
        posicao.satelites = satelites
        posicao.precisao = precisao
    else:
        posicao = Posicao(
            latitude=latitude,
            longitude=longitude,
            idadeInfo=idadeInfo,
            data=data,
            altitude=altitude,
            velocidade=velocidade,
            sentido=sentido,
            satelites=satelites,
            precisao=precisao
        )
        db.session.add(posicao)

    db.session.commit()

    return jsonify(response={
        'status': 200,
        'message': "Success"
    })
