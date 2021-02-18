
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
from db.skill_models import SkillBonus, SkillAbility, SkillCheck, SkillMove, SkillCirc, SkillDC, SkillDegree, SkillMod, SkillOpposed, SkillTime
from db.vehicle_models import Vehicle, VehFeature, VehicleSize, VehicleType, VehPower
from db.weapon_models import WeaponType, WeaponCat, WeapBenefit, WeapCondition, WeapDescriptor, Weapon 

from flask_sqlalchemy import SQLAlchemy
from copy import deepcopy

db = SQLAlchemy()

from post_functions import name, action_convert, math_convert, extra_name, descriptor_name, integer_convert, select_multiple, selects, string, check_convert, width, send, delete_row, grid_columns, vcell_add, vcell, check_cell, cell, mod_create, mod_cell, mod_add, variable_value, add_plus, check_string, variable_trait, get_name, get_circ, int_word, one_of, trait_select, string_value, string_value_else, get_keyword, int_word



stylesheets = [{"style": "/static/css/template/template.css"}, {"style": "/static/css/template/sidebar.css"}, {"style": "/static/css/icons.css"}]
meta_name="DC Adventures Online"
meta_content="An online DC Comics Roleplaying game. Play as your favorite character or create your own hero."
title = 'DC Adventures Online Roleplaying Game'
sidebar = ["rules", "games", "stories", "heroes","npcs", "locations", "skills", "abilities", "powers", "flaws", "equipment", "devices", "armor", "weapons", "vehicles", "constructs", "help"]

bonus_circ = []
entries = SkillCirc.query.all
for e in entries:
	bonus_name = db.session.query(SkillBonus).filter_by(id = e.skill_id).one()
	bonus_circ.append({'id': e.id, 'name': bonus_name + ' ' + e.keyword})

bonus_dc = []
entries = SkillCirc.query.all
for e in entries:
	bonus_name = db.session.query(SkillBonus).filter_by(id = e.skill_id).one()
	bonus_dc.append({'id': e.id, 'name': bonus_name + ' ' + e.keyword})

bonus_degree = []
entries = SkillCirc.query.all
for e in entries:
	bonus_name = db.session.query(SkillBonus).filter_by(id = e.skill_id).one()
	bonus_degree.append({'id': e.id, 'name': bonus_name + ' ' + e.keyword})

bonus_opposed = []
entries = SkillCirc.query.all
for e in entries:
	bonus_name = db.session.query(SkillBonus).filter_by(id = e.skill_id).one()
	bonus_opposed.append({'id': e.id, 'name': bonus_name + ' ' + e.keyword})

