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