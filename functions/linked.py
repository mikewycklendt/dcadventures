
from models import Modifier, ModifierTable, LevelType, Levels, Damage, DamageType
from db.rule_models import Ability, Defense, Action, ConflictAction, Skill, Check, Condition, Maneuver, Ranged, Sense, SubSense, Light, Ground, Range, Consequence, Material, Complex, Cover, Conceal, Phase, SkillTable, SkillType
from db.measure_models import MeasureType, Unit, Math, Rank, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert
from db.user_rules import Nature, Emotion, Environment, Job, Creature

from db.advanrtage_modeks import Advantage, Benefit, AdvAltCheck, AdvCirc, AdvCombined, AdvCondition, AdvDC, AdvDegree, AdvEffort, AdvMinion, AdvMod, AdvOpposed, AdvPoints, AdvPoints, AdvResist, AdvRounds, AdvSkill, AdvTime, AdvVariable, AdvantageType
from db.armor_models import Armor, ArmorType, ArmDefense, ArmDescriptor
from db.descriptor_models import Descriptor, Origin, Source, Medium, MediumSubType, MediumType
from db.equipment_models import Equipment, EquipBelt, EquipCheck, EquipDamage, EquipDescriptor, EquipEffect, EquipLimit, EquipMod, EquipOpposed, EquipType
from db.headquarters_models import Headquarters, HeadCharFeat, HeadFeatAddon, HeadFeature, HeadSize
from db.power_models import Extra, Power, PowerAction, PowerAltCheck, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegMod, PowerDegree, PowerDes, PowerEnv, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSenseEffect, PowerTime, PowerType
from db.skill_models import SkillBonus, SkillAbility, SkillCheck, SkillCirc, SkillDC, SkillDegree, SkillMod, SkillOpposed, SkillTime
from db.vehicle_models import Vehicle, VehFeature, VehicleSize, VehicleType, VehPower
from db.weapon_models import WeaponType, WeaponCat, WeapBenefit, WeapCondition, WeapDescriptor, Weapon 

from flask_sqlalchemy import SQLAlchemy
from copy import deepcopy

db = SQLAlchemy()

def linked_time(table, value, name, errors):
	
	error_msgs = errors['error_msgs']
	error = False

	if value != '':
		try:
			value = int(value)
			edit = db.session.query(table).filter(table.id == value).one()
			edit.time_table = True
			db.session.commit()
		except:
			error = True
			error = True
			message = 'There was an error processing that ' + name
			error_msgs.append(message)
			db.session.rollback()
		finally:
			db.session.close()

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def linked_move(table, value, name, errors):
	
	error_msgs = errors['error_msgs']
	error = False

	if value != '':
		try:
			value = int(value)
			edit = db.session.query(table).filter(table.id == value).one()
			edit.move_table = True
			db.session.commit()
		except:
			error = True
			error = True
			message = 'There was an error processing that ' + name
			error_msgs.append(message)
			db.session.rollback()
		finally:
			db.session.close()

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)


def linked_options(table, trait, column):
	options = []
		
	entries = db.session.query(table).all()
	for e in entries:
		if e.keyword is None:
			keyword = ''
		else:
			keyword = e.keyword
		id = e.c[column]
		entry_name = db.session.query(trait).filter(trait.id == id).one()
		options.append({'id': e.id, 'name': str(e.id) +  entry_name.name + ' ' + keyword})

	return (options)

def linked_options_power(table):
	options = []
	
	entries = db.session.query(table).all()
	for e in entries:
		id = e.power_id
		entry_name = db.session.query(Power).filter(Power.id == id).one()
		options.append({'id': e.id, 'name': str(e.id) + entry_name.name + ' ' + e.keyword})

	return (options)
	
def linked_options_advantage(table):
	options = []

	entries = db.session.query(table).all()
	for e in entries:
		id = e.advantage_id
		entry_name = db.session.query(Advantage).filter(Advantage.id == id).one()
		options.append({'id': e.id, 'name': entry_name.name + ' ' + e.keyword})
		
	return (options)

def level_reference(value, column, errors):
	
	error_msgs = errors['error_msgs']
	error = False

	if value != '':
		try:
			value = int(value)
			edit = db.session.query(Levels).filter(Levels.id == value).one()
			edit.c[column] = True
			db.session.commit()
		except:
			error = True
			error = True
			message = 'There was an error processing that Level.'
			error_msgs.append(message)
			db.session.rollback()
		finally:
			db.session.close()

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def level_adv_circ(value, errors):
	
	error_msgs = errors['error_msgs']
	error = False

	if value != '':
		try:
			value = int(value)
			edit = db.session.query(Levels).filter(Levels.id == value).one()
			edit.advantage_citc = True
			db.session.commit()
		except:
			error = True
			error = True
			message = 'There was an error processing that ' + name
			error_msgs.append(message)
			db.session.rollback()
		finally:
			db.session.close()

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def level_adv_dc(value, errors):
	
	error_msgs = errors['error_msgs']
	error = False

	if value != '':
		try:
			value = int(value)
			edit = db.session.query(Levels).filter(Levels.id == value).one()
			edit.advantage_dc = True
			db.session.commit()
		except:
			error = True
			error = True
			message = 'There was an error processing that ' + name
			error_msgs.append(message)
			db.session.rollback()
		finally:
			db.session.close()

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def level_adv_degree(value, errors):
	
	error_msgs = errors['error_msgs']
	error = False

	if value != '':
		try:
			value = int(value)
			edit = db.session.query(Levels).filter(Levels.id == value).one()
			edit.advantage_degree = True
			db.session.commit()
		except:
			error = True
			error = True
			message = 'There was an error processing that ' + name
			error_msgs.append(message)
			db.session.rollback()
		finally:
			db.session.close()

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def level_bonus_circ(value, errors):
	
	error_msgs = errors['error_msgs']
	error = False

	if value is not None:
		try:
			edit = db.session.query(Levels).filter(Levels.id == value).one()
			edit.bonus_circ = True
			db.session.commit()
		except:
			error = True
			error = True
			message = 'There was an error processing that ' + name
			error_msgs.append(message)
			db.session.rollback()
		finally:
			db.session.close()

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)
	
def level_bonus_dc(value, errors):
	
	error_msgs = errors['error_msgs']
	error = False

	if value != '':
		try:
			value = int(value)
			edit = db.session.query(Levels).filter(Levels.id == value).one()
			edit.bonus_dc = True
			db.session.commit()
		except:
			error = True
			error = True
			message = 'There was an error processing that ' + name
			error_msgs.append(message)
			db.session.rollback()
		finally:
			db.session.close()

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def level_bonus_degree(value, errors):
	
	error_msgs = errors['error_msgs']
	error = False

	if value != '':
		try:
			value = int(value)
			edit = db.session.query(Levels).filter(Levels.id == value).one()
			edit.bonus_degree = True
			db.session.commit()
		except:
			error = True
			error = True
			message = 'There was an error processing that ' + name
			error_msgs.append(message)
			db.session.rollback()
		finally:
			db.session.close()

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def level_power_circ(value, errors):
	
	error_msgs = errors['error_msgs']
	error = False

	if value != '':
		try:
			value = int(value)
			edit = db.session.query(Levels).filter(Levels.id == value).one()
			edit.power_citc = True
			db.session.commit()
		except:
			error = True
			error = True
			message = 'There was an error processing that ' + name
			error_msgs.append(message)
			db.session.rollback()
		finally:
			db.session.close()

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def level_power_dc(value, errors):
	
	error_msgs = errors['error_msgs']
	error = False

	if value != '':
		try:
			value = int(value)
			edit = db.session.query(Levels).filter(Levels.id == value).one()
			edit.power_dc = True
			db.session.commit()
		except:
			error = True
			error = True
			message = 'There was an error processing that ' + name
			error_msgs.append(message)
			db.session.rollback()
		finally:
			db.session.close()

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)

def level_power_degree(value, errors):
	
	error_msgs = errors['error_msgs']
	error = False

	if value != '':
		try:
			value = int(value)
			edit = db.session.query(Levels).filter(Levels.id == value).one()
			edit.power_degree = True
			db.session.commit()
		except:
			error = True
			error = True
			message = 'There was an error processing that ' + name
			error_msgs.append(message)
			db.session.rollback()
		finally:
			db.session.close()

	errors['error_msgs'] = error_msgs
	if error:
		errors['error'] = error

	return (errors)


