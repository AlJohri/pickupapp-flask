from flask import Flask

# flask-peewee bindings
from flask_peewee.db import Database
from flask_peewee.rest import RestAPI, RestResource

# configure our database
DATABASE = {
    'name': 'database.db',
    'engine': 'peewee.SqliteDatabase',
}
DEBUG = True
SECRET_KEY = 'ssshhhh'

app = Flask(__name__)
app.config.from_object(__name__)

# instantiate the db wrapper "peewee"
db = Database(app)
api = RestAPI(app)

import datetime
from peewee import *

class User(db.Model):
    email = TextField(primary_key=True)
    name = TextField()
    password = TextField()

class Sport(db.Model):
    sport_id = IntegerField(primary_key=True)
    title = TextField()
    created = DateTimeField(default=datetime.datetime.now)

class Location(db.Model):
    location_id = IntegerField(primary_key=True)
    title = TextField()
    created = DateTimeField(default=datetime.datetime.now)

class Game(db.Model):
    game_id = IntegerField(primary_key=True)
    title = TextField()
    description = TextField()
    capacity = IntegerField()
    creator_id = ForeignKeyField(User)
    sport_id = ForeignKeyField(Sport)
    location_id = ForeignKeyField(Location)
    time = DateTimeField()
    duration = IntegerField() # should this only be hours?
    created = DateTimeField(default=datetime.datetime.now)

class UserResource(RestResource):
    paginate_by = 100
    exclude = ('password')
    def get_api_name(self):
        return "users"

class SportResource(RestResource):
    paginate_by = 100
    def get_api_name(self):
        return "sports"

class LocationResource(RestResource):
    paginate_by = 100
    def get_api_name(self):
        return "locations"

class GameResource(RestResource):
    paginate_by = 100
    def get_api_name(self):
        return "games"

api.register(User, UserResource)
api.register(Sport, SportResource)
api.register(Location, LocationResource)
api.register(Game, GameResource)

api.setup()

if __name__ == '__main__':
    app.run()
