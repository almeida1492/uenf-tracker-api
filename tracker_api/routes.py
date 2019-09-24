# -*- coding: utf-8 -*- a
from flask import Blueprint, jsonify, request

from .extensions import db
from .models import Location

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
        return jsonify(locations=[location.serialize for location in locations])
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

    return jsonify(location={
        'coordinateX': coordinateX,
        'coordinateY': coordinateY,
    })
