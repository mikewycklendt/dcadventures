from flask import Flask, render_template, request, Response, flash, redirect, url_for
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

from models import setup_db
from models import db

load_dotenv()

import os

db_path = os.environ.get("db_path")

app = Flask(__name__)
moment = Moment(app)
#app.config.from_object('config')
project_dir = os.path.dirname(os.path.abspath(__file__))
database_path = db_path
app.config["SQLALCHEMY_DATABASE_URI"] = database_path

setup_db(app)


migrate = Migrate(app, db)

class WeaponCat(db.Model):
	__tablename__ = 'weapon_category'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())

	def format(self):
		return {
			'id': self.id,
			'name': self.name
		}

class WeaponType(db.Model):
	__tablename__ = 'weapon_type'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	type_id = db.Column(db.Integer, db.ForeignKey('weapon_category.id'))


	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'type_id': self.type_id
		}

class Weapon(db.Model):
	__tablename__ = 'weapons'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String())
	cat_id = db.Column(db.Integer, db.ForeignKey('weapon_category.id'))
	type_id = db.Column(db.Integer, db.ForeignKey('weapon_type.id'))
	cost = db.Column(db.Integer)
	description = db.Column(db.String())
	critical = db.Column(db.Integer)
	damage = db.Column(db.Integer)
	toughness = db.Column(db.Integer)
	material = db.Column(db.Integer, db.ForeignKey('materials.id'))
	length = db.Column(db.Integer)
	length_units = db.Column(db.Integer, db.ForeignKey('unit_type.id'))
	resist_dc = db.Column(db.Integer)
	resistance = db.Column(db.Integer, db.ForeignKey('defense.id'))
	power_rank = db.Column(db.Integer)
	power = db.Column(db.String())
	hands = db.Column(db.Integer)
	strength = db.Column(db.Boolean)
	thrown = db.Column(db.Boolean)
	unarmed = db.Column(db.Boolean)
	reach = db.Column(db.Integer)
	ranged_attack_bonus = db.Column(db.Integer)
	protect = db.Column(db.Integer)
	ranged_area = db.Column(db.String())
	ranged_burst = db.Column(db.Integer)
	ranged_area_damage = db.Column(db.Integer)
	penetrate = db.Column(db.Boolean)
	attack_bonus = db.Column(db.Integer)
	subtle = db.Column(db.Boolean)
	perception_dc = db.Column(db.Integer)
	advantage = db.Column(db.String())
	grenade_area = db.Column(db.String())
	grenade_burst = db.Column(db.Integer)
	grenade_area_damage = db.Column(db.Integer)
	conceal = db.Column(db.Integer, db.ForeignKey('concealment.id'))
	sense = db.Column(db.Integer, db.ForeignKey('senses.id'))
	double = db.Column(db.Boolean)
	double_mod = db.Column(db.Integer)
	benefit = db.Column(db.Boolean)
	condition = db.Column(db.Boolean)
	descriptor = db.Column(db.Boolean)

	def format(self):
		return {
			'id': self.id,
			'name': self.name,
			'cat_id': self.cat_id,
			'type_id': self.type_id,
			'cost': self.cost,
			'description': self.description,
			'critical': self.critical,
			'damage': self.damage,
			'toughness': self.toughness,
			'material': self.material,
			'length': self.length,
			'length_units': self.length_units,
			'resist_dc': self.resist_dc,
			'resistance': self.resistance,
			'power_rank': self.power_rank,
			'power': self.power,
			'hands': self.hands,
			'strength': self.strength,
			'thrown': self.thrown,
			'unarmed': self.unarmed,
			'reach': self.reach,
			'ranged_attack_bonus': self.ranged_attack_bonus,
			'protect': self.protect,
			'ranged_area': self.ranged_area,
			'ranged_burst': self.ranged_burst,
			'ranged_area_damage': self.ranged_area_damage,
			'penetrate': self.penetrate,
			'attack_bonus': self.attack_bonus,
			'subtle': self.subtle,
			'perception_dc': self.perception_dc,
			'advantage': self.advantage,
			'grenade_area': self.grenade_area,
			'grenade_burst': self.grenade_burst,
			'grenade_area_damage': self.grenade_area_damage,
			'conceal': self.conceal,
			'sense': self.sense,
			'double': self.double,
			'double_mod': self.double_mod,
			'benefit': self.benefit,
			'condition': self.condition,
			'descriptor': self.descriptor
		}
