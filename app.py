import json
import dateutil.parser
import babel
from flask import Flask, render_template, request, Response, flash, redirect, url_for, jsonify
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from flask_migrate import Migrate
from datetime import datetime
from models import setup_db, Ability, Defense, Modifier, Action, Skill, SkillType, Check, SkillTable, Condition, Phase, Sense, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert
from decimal import *
import sys

from dotenv import load_dotenv

load_dotenv()

import os

db_path = os.environ.get("db_path")

#db_drop_and_create_all()

app = Flask(__name__)
moment = Moment(app)
app.config['SQLALCHEMY_DATABASE_URI'] = db_path
db = SQLAlchemy()
setup_db(app)
migrate = Migrate(app, db)

def decRound(value):
	decimal = Decimal(value).quantize(Decimal('.001'), rounding=ROUND_UP)
	return decimal

def divide(value1, value2):
	value = Decimal(value1) / Decimal(value2)
	decimal = Decimal(value).quantize(Decimal('.001'), rounding=ROUND_UP)
	return decimal

def multiply(value1, value2):
	value = Decimal(value1) * Decimal(value2)
	decimal = Decimal(value).quantize(Decimal('.01'), rounding=ROUND_UP)
	return decimal

def measure(measurements):

	for measurement in measurements:
		mass = measurement['mass']
		time = measurement['time']
		distance = measurement['distance']
		volume = measurement['volume']

		measurement['mass'] = Decimal(mass).quantize(Decimal('.01'))
		measurement['time'] = Decimal(time).quantize(Decimal('.01'))
		measurement['distance'] = Decimal(distance).quantize(Decimal('.01'))
		measurement['volume'] = Decimal(volume).quantize(Decimal('.01'))

	print (measurements)

	return measurements

@app.route('/')
def index():
	stylesheets = [{"style": "/static/css/template.css"}, {"style": "/static/css/sidebar.css"}]
	includehtml = 'home.html'
	title = 'DC Adventures Online Roleplqying Game'
	stylesheets.append({"style": "/static/css/home.css"})
	meta_name="DC Adventures Online"
	meta_content="An online DC Comics Roleplaying game. Play as your favorite character or create your own hero."
	return render_template('template.html', includehtml=includehtml, title=title, stylesheets=stylesheets, meta_name=meta_name, meta_content=meta_content)

@app.route('/abilities')
def abilities():

	title = 'Abilities'
	size = 'h1' 
	table = Ability.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/defense')
def defense():

	title = 'Defense'
	size = 'h2'
	table = Defense.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/modifiers')
def modifiers():

	title = 'Modifiers'
	
	size = 'h1'

	table = Modifier.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/actions')
def actions():

	title = 'Actions'
	
	size = 'h1'

	table = Action.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/skills')
def skills():

	title = 'Skills'
	
	size = 'h1'

	table = Skill.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/skill/type')
def skill_type():

	title = 'Skill Type'
	
	size = 'h1'

	table = SkillType.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/checks')
def checks():

	title = 'Check Types'
	
	size = 'h1'

	table = Check.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/conditions')
def conditions():

	title = 'Basic Conditions'
	
	size = 'h1'

	table = Condition.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/phases')
def phases():

	title = 'Phases'
	
	size = 'h1'

	table = Phase.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/senses')
def senses():

	title = 'Senses'
	
	size = 'h1'

	table = Sense.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/measurements')
def measurements():

	title = 'Measurements Table'
	
	size = 'h3'

	measurements = Measurement.query.all()

	formatted = [measurement.format() for measurement in measurements]
	
	print (formatted)

	table = measure(formatted)

	return render_template('measurements.html', table=table, title=title, size=size)



'''
@app.route('/debilitated/create')
def debilitated_create():

	entries = []

	entries.append({
		'name': 'Debilitated ',
		'effects': 
		'condition_id': 
		'actions':
		'controlled':
		'ability_id': 
		})
'''

@app.route('/condition/create')
def create_conditions():

	conditions = []

	conditions.append({
		'name': 'Compelled',
		'description': 'A compelled character is directed by an outside force, but struggling against it; the character is limited to a single standard action each turn, chosen by another, controlling, character. As usual, this standard action can be traded for a move or even free action. Controlled supersedes compelled',
		'phase': 1,
		'supercede': None,
		'specific': False,
		'time': None,
		'time_unit': None,
		'effects': None,
		'multiple': False
		})

	conditions.append({
		'name': 'Controlled',
		'description': 'A controlled character has no free will; the character’s actions each turn are dictated by another, controlling, character.',
		'phase': 1,
		'supercede': None,
		'specific': False,
		'time': None,
		'time_unit': None,
		'effects': None,
		'multiple': False
		})

	conditions.append({
		'name': 'Dazed',
		'description': 'A dazed character is limited to a single standard action per round, although the character may use that action to perform a move or free action, as usual. Stunned supersedes dazed.',
		'phase': 1,
		'supercede': 'Stunned',
		'specific': False,
		'time': None,
		'time_unit': None,
		'effects': None,
		'multiple': True 
		})

	conditions.append({
		'name': 'Debilitated',
		'description': 'The character has one or more abilities lowered below –5. (See Debilitated Abilities in the Abilities chapter.)',
		'phase': 1,
		'supercede': None,
		'specific': True,
		'time': None,
		'time_unit': None,
		'effects': None,
		'multiple': True
		})

	conditions.append({
		'name': 'Defenseless',
		'description': 'A defenseless character has active defense bonuses of 0. Attackers can make attacks on defenseless opponents as routine checks (see Routine Checks). If the attacker chooses to forgo the routine check and make a normal attack check, any hit is treated as a critical hit (see Critical Hit). Defenseless characters are often prone, providing opponents with an additional bonus to attack checks (see Prone, later in this section).',
		'phase': 1,
		'supercede': None,
		'specific': False,
		'time': None,
		'time_unit': None,
		'effects': None,
		'multiple':True
		})

	conditions.append({
		'name': 'Disabled',
		'phase': 4,
		'supercede': 'Debilitated',
		'specific': True,
		'multiple': True,
		'time': None,
		'time_unit': None,
		'effects': None,
		'description': 'A disabled character is at a –5 circumstance penalty on checks. If the penalty applies to specific checks, they are added to the name of the condition, such as Attack Disabled, Fighting Disabled, Perception Disabled, and so forth. Debilitated, if it applies to the same trait(s), supersedes disabled.',
		})

	conditions.append({
		'name': 'Fatigued',
		'phase': 1,
		'supercede': None,
		'specific': False,
		'multiple': False,
		'time': 1,
		'time_unit': 'hour',
		'effects': 'Hindered',
		'description': 'Fatigued characters are hindered. Characters recover from a fatigued condition after an hour of rest.'
		})

	conditions.append({
		'name': 'Hindered',
		'phase': 1,
		'supercede': 'Immobile',
		'specific': False,
		'multiple': False,
		'time': None,
		'time_unit': None,
		'effects': None,
		'description': 'A hindered character moves at half normal speed (–1 speed rank). Immobile supersedes hindered.'
		})

	conditions.append({
		'name': 'Immobile',
		'phase': 1,
		'supercede': None,
		'specific': False,
		'multiple': False,
		'time': None,
		'time_unit': None,
		'effects': None,
		'description': 'Immobile characters have no movement speed and cannot move from the spot they occupy, although they are still capable of taking actions unless prohibited by another condition.'
		})

	conditions.append({
		'name': 'Impaired',
		'phase': 4,
		'supercede': 'Disabled',
		'specific': True,
		'multiple': True,
		'time': None,
		'time_unit': None,
		'effects': None,
		'description': 'An impaired character is at a –2 circumstance penalty on checks. If the impairment applies to specific checks, they are added to the name of the condition, such as Fighting Impaired, Perception Impaired, and so forth. If it applies to the same trait(s), disabled supersedes impaired'
		})

	conditions.append({
		'name': 'Stunned',
		'phase': 1,
		'supercede': None,
		'specific': False,
		'multiple': False,
		'time': None,
		'time_unit': None,
		'effects': None,
		'description': 'Stunned characters cannot take any actions.'
		})


	conditions.append({
		'name': 'Transformed',
		'phase': 1,
		'supercede': None,
		'specific': True,
		'multiple': True,
		'time': None,
		'time_unit': None,
		'effects': None,
		'description': 'Transformed characters have some or all of their traits altered by an outside agency. This may range from a change in the character’s appearance to a complete change in trait ranks, even the removal of some traits and the addition of others! The primary limit on the transformed condition is the character’s power point total cannot increase, although it can effectively decrease for the duration of the transformation, such as when a powerful super hero is turned into an otherwise powerless mouse or frog (obviously based on considerably fewer power points).'
		})

	conditions.append({
		'name': 'Unaware',
		'phase': 1,
		'supercede': None,
		'specific': True,
		'multiple': True,
		'time': None,
		'time_unit': None,
		'effects': None,
		'description': 'The character is completely unaware of his surroundings, unable to make interaction or Perception checks or perform any action based on them. If the condition applies to a specific sense or senses, they are added to the name of the condition, such as visually unaware, tactilely unaware (or numb), and so forth. Subjects have full concealment from all of a character’s unaware senses.'
		})

	conditions.append({
		'name': 'Vulnerable',
		'phase': 1,
		'supercede': 'Defenseless',
		'specific': True,
		'multiple': True,
		'time': None,
		'time_unit': None,
		'effects': None,
		'description': 'Vulnerable characters are limited in their ability to defend themselves, halving their active defenses (round up the final value). Defenseless supersedes vulnerable.'
		})

	conditions.append({
		'name': 'Weakened',
		'phase': 1,
		'supercede': 'Debilitated',
		'specific': True,
		'multiple': False,
		'time': None,
		'time_unit': None,
		'effects': None,
		'description': 'The character has temporarily lost power points in a trait. See the Weaken effect in the Powers chapter for more. Debilitated supersedes weakened.'
		})

	for condition in conditions:
		name = condition['name']
		phase = condition['phase']
		supercede = condition['supercede']
		specific = condition['specific']
		multiple = condition['multiple']
		time = condition['time']
		unit = condition['time_unit']
		effects = condition['effects']
		description = condition['description']

		entry = Condition(name=name, phase=phase, supercede=supercede, specific=specific, multiple=multiple, time=time, unit=unit, effects=effects, description=description)
		db.session.add(entry)
		db.session.commit()

	results = Condition.query.all()

	for result in results:
		print (result.id)
		print (result.name)
		print (result.description)

	return ('conditions added')

@app.route('/defense/create')
def defense_create():

	defenses = []

	defenses.append({'name': 'Dodge',
						'ability_id': 3,
						'description': 'Dodge defense is based on Agility rank. It includes reaction time, quickness, nimbleness, and overall coordination, used to avoid ranged attacks or other hazards where reflexes and speed are important.'
						, 'modifier_id': 4})
	defenses.append({'name': 'Fortitude',
						'ability_id': 2,
						'description': 'Fortitude defense is based on Stamina and measures health and resistance to threats like poison or disease. It incorporates constitution, ruggedness, metabolism, and immunity.'
						, 'modifier_id': 4})
	defenses.append({'name': 'Parry',
						'ability_id': 5,
						'description': 'Parry defense is based on Fighting. It is the ability to counter, duck, or otherwise evade a foe’s attempts to strike you in close combat through superior fighting ability.'
						, 'modifier_id': 4})
	defenses.append({'name': 'Toughness',
						'ability_id': 2,
						'description': 'Toughness defense is based on Stamina and is resistance to direct damage or harm, and overall durability.'
						, 'modifier_id': 4 })
	defenses.append({'name': 'Will',
						'ability_id': 7,
						'description': 'Will defense is based on Awareness rank. It measures mental stability, level-headedness, determination, selfconfidence, self-awareness, and willpower, and is used to resist mental or spiritual attacks.'
						, 'modifier_id': 4 })
	for defense in defenses:
		name = defense['name']
		ability_id = defense['ability_id']
		description = defense['description']
		modifier_id = 4

		entry = Defense(name=name, ability_id=ability_id, description=description, modifier_id=modifier_id)
		db.session.add(entry)
		db.session.commit()

	additions = Defense.query.all()
	for addition in additions:
		defense_id = addition.id
		name = addition.name
		ability_id = addition.ability_id
		description = addition.description
		modifier = addition.modifier_id

		print (defense_id)
		print (name)
		print (ability_id)
		print (description)
		print (modifier)

	return ('defense')

@app.route('/measurements/create')
def measurements_create():

	measurements = []

	measurements.append({
		'rank': -5,
		'mass': Decimal(1.5),
		'mass_unit': 'pounds',
		'time': divide(1, 8),
		'time_unit': 'seconds',
		'distance': 6,
		'distance_unit': 'inches',
		'volume': divide(1, 32),
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': -4,
		'mass': 3,
		'mass_unit': 'pounds',
		'time': divide(1, 4),
		'time_unit': 'seconds',
		'distance': 1,
		'distance_unit': 'feet',
		'volume': divide(1, 16),
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': -3,
		'mass': 6,
		'mass_unit': 'pounds',
		'time': divide(1, 2),
		'time_unit': 'seconds',
		'distance': 3,
		'distance_unit': 'feet',
		'volume': divide(1, 8),
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': -2,
		'mass': 12,
		'mass_unit': 'pounds',
		'time': 1,
		'time_unit': 'seconds',
		'distance': 6,
		'distance_unit': 'feet',
		'volume': divide(1, 4),
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': -1,
		'mass': 25,
		'mass_unit': 'pounds',
		'time': 3,
		'time_unit': 'seconds',
		'distance': 15,
		'distance_unit': 'feet',
		'volume': divide(1, 2),
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': 0,
		'mass': 50,
		'mass_unit': 'pounds',
		'time': 6,
		'time_unit': 'seconds',
		'distance': 30,
		'distance_unit': 'feet',
		'volume': 1,
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': 1,
		'mass': 100,
		'mass_unit': 'pounds',
		'time': 12,
		'time_unit': 'seconds',
		'distance': 60,
		'distance_unit': 'feet',
		'volume': 2,
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': 2,
		'mass': 200,
		'mass_unit': 'pounds',
		'time': 30,
		'time_unit': 'seconds',
		'distance': 120,
		'distance_unit': 'feet',
		'volume': 4,
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': 3,
		'mass': 400,
		'mass_unit': 'pounds',
		'time': 1,
		'time_unit': 'minutes',
		'distance': 250,
		'distance_unit': 'feet',
		'volume': 8,
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': 4,
		'mass': 800,
		'mass_unit': 'pounds',
		'time': 2,
		'time_unit': 'minutes',
		'distance': 500,
		'distance_unit': 'feet',
		'volume': 15,
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': 5,
		'mass': 1600,
		'mass_unit': 'pounds',
		'time': 4,
		'time_unit': 'minutes',
		'distance': 900,
		'distance_unit': 'feet',
		'volume': 30,
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': 6,
		'mass': 3200,
		'mass_unit': 'pounds',
		'time': 8,
		'time_unit': 'minutes',
		'distance': 1800,
		'distance_unit': 'feet',
		'volume': 60,
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': 7,
		'mass': 3,
		'mass_unit': 'tons',
		'time': 15,
		'time_unit': 'minutes',
		'distance': divide(1, 2),
		'distance_unit': 'miles',
		'volume': 125,
		'volume_unit': 'cubic feet'
	})
	
	measurements.append({
		'rank': 8,
		'mass': 6,
		'mass_unit': 'tons',
		'time': 30,
		'time_unit': 'minutes',
		'distance': 1,
		'distance_unit': 'miles',
		'volume': 250,
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': 9,
		'mass': 12,
		'mass_unit': 'tons',
		'time': 1,
		'time_unit': 'hours',
		'distance': 2,
		'distance_unit': 'miles',
		'volume': 500,
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': 10,
		'mass': 25,
		'mass_unit': 'tons',
		'time': 2,
		'time_unit': 'hours',
		'distance': 4,
		'distance_unit': 'miles',
		'volume': 1000,
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': 11,
		'mass': 50,
		'mass_unit': 'tons',
		'time': 4,
		'time_unit': 'hours',
		'distance': 8,
		'distance_unit': 'miles',
		'volume': 2000,
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': 12,
		'mass': 100,
		'mass_unit': 'tons',
		'time': 8,
		'time_unit': 'hours',
		'distance': 16,
		'distance_unit': 'miles',
		'volume': 4000,
		'volume_unit': 'cubic feet'
	})
	
	measurements.append({
		'rank': 13,
		'mass': 200,
		'mass_unit': 'tons',
		'time': 16,
		'time_unit': 'hours',
		'distance': 30,
		'distance_unit': 'miles',
		'volume': 8000,
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': 14,
		'mass': 400,
		'mass_unit': 'tons',
		'time': 1,
		'time_unit': 'days',
		'distance': 60,
		'distance_unit': 'miles',
		'volume': 15000,
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': 15,
		'mass': 800,
		'mass_unit': 'tons',
		'time': 2,
		'time_unit': 'days',
		'distance': 120,
		'distance_unit': 'miles',
		'volume': 32000,
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': 16,
		'mass': 1600,
		'mass_unit': 'tons',
		'time': 4,
		'time_unit': 'days',
		'distance': 250,
		'distance_unit': 'miles',
		'volume': 65000,
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': 17,
		'mass': Decimal(3.2),
		'mass_unit': 'kilotons',
		'time': 1,
		'time_unit': 'weeks',
		'distance': 500,
		'distance_unit': 'miles',
		'volume': 125000,
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': 18,
		'mass': 6,
		'mass_unit': 'kilotons',
		'time': 2,
		'time_unit': 'weeks',
		'distance': 1000,
		'distance_unit': 'miles',
		'volume': 250000,
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': 19,
		'mass': 12,
		'mass_unit': 'kilotons',
		'time': 1,
		'time_unit': 'months',
		'distance': 2000,
		'distance_unit': 'miles',
		'volume': 500000,
		'volume_unit': 'cubic feet'
	})

	measurements.append({
		'rank': 20,
		'mass': 25,
		'mass_unit': 'kilotons',
		'time': 2,
		'time_unit': 'months',
		'distance': 4000,
		'distance_unit': 'miles',
		'volume': 1,
		'volume_unit': 'million cubic feet'
	})

	measurements.append({
		'rank': 21,
		'mass': 50,
		'mass_unit': 'kilotons',
		'time': 4,
		'time_unit': 'months',
		'distance': 8000,
		'distance_unit': 'miles',
		'volume': 2,
		'volume_unit': 'million cubic feet'
	})

	measurements.append({
		'rank': 22,
		'mass': 100,
		'mass_unit': 'kilotons',
		'time': 8,
		'time_unit': 'months',
		'distance': 16000,
		'distance_unit': 'miles',
		'volume': 4,
		'volume_unit': 'million cubic feet'
	})

	measurements.append({
		'rank': 23,
		'mass': 200,
		'mass_unit': 'kilotons',
		'time': Decimal(1.5),
		'time_unit': 'years',
		'distance': 32000,
		'distance_unit': 'miles',
		'volume': 8,
		'volume_unit': 'million cubic feet'
	})

	measurements.append({
		'rank': 24,
		'mass': 400,
		'mass_unit': 'kilotons',
		'time': 3,
		'time_unit': 'years',
		'distance': 64000,
		'distance_unit': 'miles',
		'volume': 15,
		'volume_unit': 'million cubic feet'
	})

	measurements.append({
		'rank': 25,
		'mass': 800,
		'mass_unit': 'kilotons',
		'time': 6,
		'time_unit': 'years',
		'distance': 125000,
		'distance_unit': 'miles',
		'volume': 32,
		'volume_unit': 'million cubic feet'
	})

	measurements.append({
		'rank': 26,
		'mass': 1600,
		'mass_unit': 'kilotons',
		'time': 12,
		'time_unit': 'years',
		'distance': 250000,
		'distance_unit': 'miles',
		'volume': 65,
		'volume_unit': 'million cubic feet'
	})

	measurements.append({
		'rank': 27,
		'mass': 3200,
		'mass_unit': 'kilotons',
		'time': 25,
		'time_unit': 'years',
		'distance': 500000,
		'distance_unit': 'miles',
		'volume': 125,
		'volume_unit': 'million cubic feet'
	})

	measurements.append({
		'rank': 28,
		'mass': 6400,
		'mass_unit': 'kilotons',
		'time': 50,
		'time_unit': 'years',
		'distance': 1,
		'distance_unit': 'million miles',
		'volume': 250,
		'volume_unit': 'million cubic feet'
	})

	measurements.append({
		'rank': 29,
		'mass': 12500,
		'mass_unit': 'kilotons',
		'time': 100,
		'time_unit': 'years',
		'distance': 2,
		'distance_unit': 'million miles',
		'volume': 500,
		'volume_unit': 'million cubic feet'
	})

	measurements.append({
		'rank': 30,
		'mass': 25000,
		'mass_unit': 'kilotons',
		'time': 200,
		'time_unit': 'years',
		'distance': 4,
		'distance_unit': 'million miles',
		'volume': 1,
		'volume_unit': 'billion cubic feet'
	})

	for measurement in measurements:
		rank = measurement['rank']
		mass = measurement['mass']
		mass_unit = measurement['mass_unit']
		time = measurement['time']
		time_unit = measurement['time_unit']
		distance = measurement['distance']
		distance_unit = measurement['distance_unit']
		volume = measurement['volume']
		volume_unit = measurement['volume_unit']

		entry = Measurement(rank=rank, mass=mass, mass_unit=mass_unit, time=time, time_unit=time_unit, distance=distance, distance_unit=distance_unit, volume=volume, volume_unit=volume_unit)
		db.session.add(entry)
		db.session.commit()

	for i in range(30, 101, 1):
		rank = i + 1
		mass = mass * 2
		mass_unit = 'kilotons'
		time = multiply(time, 2)
		time_unit = 'years'
		distance = multiply(distance, 2)
		distance_unit = 'million miles'
		volume = multiply(volume, 2)
		volume_unit = 'billion cubic feet'

		entry = Measurement(rank=rank, mass=mass, mass_unit=mass_unit, time=time, time_unit=time_unit, distance=distance, distance_unit=distance_unit, volume=volume, volume_unit=volume_unit)
		db.session.add(entry)
		db.session.commit()
		
	results = Measurement.query.all()

	for result in results:
		print (result.rank)
	
	return ('measurements added')


@app.route('/phases/create')
def phases_create():

	phases = []

	phases.append({
		'name': 'before anything'
	})

	phases.append({
		'name': 'before  actions'
	})

	phases.append({
		'name': 'after action'
	})

	phases.append({
		'name': 'before check'
	})

	phases.append({
		'name': 'after check'
	})

	for phase in phases:
		name = phase['name']

		entry = Phase(name=name)
		db.session.add(entry)
		db.session.commit()

	results = Phase.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('phases added')

@app.route('/senses/create')
def senses_create():

	senses = ['Sight', 'Hearing', 'Smell', 'Taste', 'Touch']

	for sense in senses:

		entry = Sense(name=sense)
		db.session.add(entry)
		db.session.commit()

	results = Sense.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('senses added')



	
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)