
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
from sqlalchemy.sql import literal_column
from copy import deepcopy

db = SQLAlchemy()

def user_item(table, name, value, new, field, body, name_check=True, class_check=False):

	new_items = body['new_items']
	error_msgs = body['error_msgs']

	if value == 'other':
		try:
			if name_check:
				name_check = db.session.query(table).filter_by(name=new, show=True).first()
				if name_check is not None:
					body['success'] = False
					message = 'There is already a ' + name + ' with that name'
					error_msgs.append(message)
					body['error_msgs'] = error_msgs
					return (body)

			entry = table(name=new)
			db.session.add(entry)
			db.session.commit()
			value = entry.id
			item = {}
			body['new'] = True
			item['id'] = entry.id
			item['name'] = entry.name
			item['class'] = class_check
			item['field'] = field
			new_items.append(item)
			db.session.close()
		except:
			body['success'] = False
			message = 'Could not create that ' + name + '.'
			error_msgs.append(message)

	body['output'] = value
	body['new_items'] = new_items
	body['error_msgs'] = error_msgs

	return (body)