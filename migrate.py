from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from dotenv import load_dotenv

load_dotenv()

import os



db_path = os.environ.get("db_path")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_path

db = SQLAlchemy(app)

# Import database models with app context
with app.app_context():
  from db.models import setup_db, Ability, Power, Extra, ConflictAction, Damage, DamageType, Descriptor, Origin, Source, Medium, MediumSubType, PowerDes, MediumType, Range, Defense, Modifier, Complex, Emotion, Action, Ground, Skill, SkillType, Material, Check, SkillTable, Condition, Phase, Sense, SubSense, Measurement, MassCovert, TimeCovert, DistanceCovert, VolumeCovert, ModifierTable, MeasureType, Unit, Math, Rank, SkillBonus
  from db.models import Advantage, Consequence, Benefit, Environment, Job, Creature, Maneuver, Cover, Conceal, Ranged, WeaponType, WeaponCat, Benefit, AdvAltCheck, AdvCirc, AdvCombined, AdvCondition, AdvDC, AdvDegree, AdvEffort, AdvMinion, AdvMod, AdvOpposed, AdvPoints, AdvPoints, AdvResist, AdvRounds, AdvSkill, AdvTime, AdvVariable
  from db.models import Levels, LevelType, PowerAltCheck, PowerAction, PowerChar, PowerCirc, PowerCreate, PowerDamage, PowerDC, PowerDefense, PowerDegMod, PowerDegree, PowerEnv, PowerMinion, PowerMod, PowerMove, PowerOpposed, PowerRanged, PowerResist, PowerResistBy, PowerReverse, PowerSenseEffect, PowerTime 
  from db.models import Equipment, Light, EquipType, Feature, WeaponCat, Weapon, EquipEffect, EquipBelt, EquipCheck, EquipDamage, EquipDescriptor, EquipLimit, EquipMod, EquipOpposed
  from db.models import WeapBenefit, WeapCondition, WeapDescriptor 
  from db.models import Armor, ArmorType, ArmDescriptor, ArmDefense
  from db.models import Vehicle, VehicleType, PowerType, VehicleSize, VehPower, VehFeature
  from db.models import Headquarters, HeadFeature, HeadFeatAddon, HeadSize, HeadCharFeat
  from db.skill_models import *

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

'''
sudo python3 migrate.py db migrate
sudo python3 migrate.py db upgrade

DROP TABLE alembic_version;
sudo python3 migrate.py db stamp heads

'''