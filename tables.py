from flask import Blueprint
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

from models import setup_db

from models import Modifier, ModifierTable, LevelType, Levels, Damage, DamageType
from db.rule_models import Ability, Defense, Action, ConflictAction, Skill, Check, Condition, Maneuver, Ranged, Sense, SubSense, Light, Ground, Range, Consequence, Material, Complex, Cover, Conceal, Phase, SkillTable, SkillType
from db.measure_models import MeasureType, Unit, Math, Rank, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert
from db.user_rules import Nature, Emotion, Environment, Job, Creature

from db.advanrtage_modeks import Advantage, Benefit, AdvCheck, AdvCirc, AdvCombined, AdvCondition, AdvDC, AdvDegree, AdvEffort, AdvMinion, AdvMod, AdvOpposed, AdvPoints, AdvPoints, AdvResist, AdvRounds, AdvSkill, AdvTime, AdvVariable, AdvantageType, AdvMove
from db.armor_models import Armor, ArmorType, ArmDefense, ArmDescriptor
from db.descriptor_models import Descriptor, Origin, Source, Medium, MediumSubType, MediumType
from db.equipment_models import Equipment, EquipBelt, EquipCheck, EquipDamage, EquipDescriptor, EquipEffect, EquipLimit, EquipMod, EquipOpposed, EquipType
from db.headquarters_models import Headquarters, HeadCharFeat, HeadFeatAddon, HeadFeature, HeadSize
from db.power_models import Extra, Power, PowerDuration, PowerAction, PowerCheck, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegree, PowerDes, PowerEnv, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSenseEffect, PowerTime, PowerType
from db.skill_models import SkillBonus, SkillAbility, SkillCheck, SkillCirc, SkillDC, SkillDegree, SkillMod, SkillOpposed, SkillTime
from db.vehicle_models import Vehicle, VehFeature, VehicleSize, VehicleType, VehPower
from db.weapon_models import WeaponType, WeaponCat, WeapBenefit, WeapCondition, WeapDescriptor, Weapon 

from decimal import *
from measurements import decRound, divide, multiply, measure
import sys
from dotenv import load_dotenv

load_dotenv()

import os

db_path = os.environ.get("db_path")


tables = Blueprint('tables', __name__)

@tables.route('/abilities')
def abilities():

	title = 'Abilities'
	size = 'h1' 
	table = Ability.query.all()

	return render_template('tables/table.html', table=table, title=title, size=size)

@tables.route('/defense')
def defense():

	title = 'Defense'
	size = 'h2'
	table = Defense.query.all()

	return render_template('tables/table.html', table=table, title=title, size=size)

@tables.route('/modifiers')
def modifiers():

	title = 'Modifiers'
	
	size = 'h1'

	table = Modifier.query.all()

	return render_template('tables/table.html', table=table, title=title, size=size)

@tables.route('/actions')
def actions():

	title = 'Actions'
	
	size = 'h1'

	table = Action.query.all()

	return render_template('tables/table.html', table=table, title=title, size=size)

@tables.route('/skills')
def skills():

	title = 'Skills'
	
	size = 'h1'

	table = Skill.query.all()

	return render_template('tables/table.html', table=table, title=title, size=size)

@tables.route('/skill/type')
def skill_type():

	title = 'Skill Type'
	
	size = 'h1'

	table = SkillType.query.all()

	return render_template('tables/table.html', table=table, title=title, size=size)

@tables.route('/checks')
def checks():

	title = 'Check Types'
	
	size = 'h1'

	table = Check.query.all()

	return render_template('tables/table.html', table=table, title=title, size=size)

@tables.route('/conditions')
def conditions():

	title = 'Basic Conditions'
	
	size = 'h1'

	table = Condition.query.all()

	return render_template('tables/table.html', table=table, title=title, size=size)

@tables.route('/phases')
def phases():

	title = 'Phases'
	
	size = 'h1'

	table = Phase.query.all()

	return render_template('tables/table.html', table=table, title=title, size=size)

@tables.route('/senses')
def senses():

	title = 'Senses'
	
	size = 'h1'

	table = Sense.query.all()

	return render_template('tables/table.html', table=table, title=title, size=size)

@tables.route('/measuretype')
def measurement_type():

	title = 'Measurement Type'
	
	size = 'h1'

	table = MeasureType.query.all()

	return render_template('tables/table.html', table=table, title=title, size=size)

@tables.route('/units')
def unit_type():

	title = 'Measurement Units'
	
	size = 'h1'

	table = Unit.query.all()

	return render_template('tables/units.html', table=table, title=title, size=size)

@tables.route('/ranks')
def rank_type():

	title = 'Measurement Units'
	
	size = 'h1'

	table = Rank.query.all()

	return render_template('tables/ranks.html', table=table, title=title, size=size)


@tables.route('/math')
def math_type():

	title = 'Measurement Units'
	
	size = 'h1'

	table = Math.query.all()

	return render_template('tables/table.html', table=table, title=title, size=size)

@tables.route('/measurements')
def measurements():

	title = 'Measurements Table'
	
	size = 'h3'

	measurements = Measurement.query.all()

	formatted = [measurement.format() for measurement in measurements]
	
	print (formatted)

	table = measure(formatted)

	return render_template('tables/measurements.html', table=table, title=title, size=size)

@tables.route('/senses')
def sense_type():

	title = 'Senses'
	
	size = 'h1'

	table = Sense.query.all()

	return render_template('tables/table.html', table=table, title=title, size=size)

@tables.route('/materials')
def materials():

	title = 'Materials'
	
	size = 'h1'

	table = Material.query.all()

	return render_template('tables/table.html', table=table, title=title, size=size)

@tables.route('/complexity')
def complexity():

	title = 'Complexity'
	
	size = 'h1'

	table = Complex.query.all()

	return render_template('tables/table.html', table=table, title=title, size=size)


@tables.route('/mediumsubtype')
def mediumsubtype():

	title = 'Complexity'
	
	size = 'h1'

	table = MediumSubType.query.all()

	return render_template('tables/table.html', table=table, title=title, size=size)