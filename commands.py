import click

from .extensions import db
from .models import Location


@click.command(name='create_tables')
def create_tables():
    db.create_all()
