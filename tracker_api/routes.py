# -*- coding: utf-8 -*- a
from flask import Blueprint, jsonify

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
    if locations.__(len)__ > 0:
        return jsonify(locations=[location.serialize for location in locations])
    else:
        return "Empty database"


# @main.route('/sendLocation', methods=['POST'])
# def sendLocation():
#     location = Location(1, 229035, 43209622)
#     db.session.add(location)
#     db.commit()

#     return jsonify(location={
#         'coordinateX': 229035,
#         'coordinateY': 43209622,
#     })
    
