from app import app,db
from peewee import *

from app import User
from app import Sport
from app import Location
from app import Game

User.create_table(fail_silently=True)
Sport.create_table(fail_silently=True)
Location.create_table(fail_silently=True)
Game.create_table(fail_silently=True)

User.create(email="al.johri@gmail.com", name="Al Johri", password="")
User.create(email="bmplatta@gmail.com", name="Ben Platta", password="")
User.create(email="mikeqhan@gmail.com", name="Mike Han", password="")
User.create(email="tigistdiriba2016@u.northwestern.edu", name="Tigist Diriba", password="")
User.create(email="tedwu2016@u.northwestern.edu", name="Ted Wu", password="")

Sport.create(title="soccer")
Sport.create(title="basketball")
Sport.create(title="hockey")
Sport.create(title="football")
Sport.create(title="volleyball")
Sport.create(title="badminton")
Sport.create(title="ultimate frisbee")
Sport.create(title="weight lifting")
Sport.create(title="other")

Location.create(title="SPAC")
Location.create(title="Blomquist")
Location.create(title="Patten")
Location.create(title="Long Field")
Location.create(title="Lakeside Field")

Game.create(
  title="Al's Awesome Soccer Game", 
  description="This game is the awesomest of games.",
  capacity=4,
  creator_id=User.get_or_create(email="al.johri@gmail.com"),
  sport_id=Sport.get_or_create(title="soccer"),
  location_id=Location.get_or_create(title="SPAC"),
  time="5:00 PM",
  duration=1
)

