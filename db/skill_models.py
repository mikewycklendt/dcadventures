from flask import Flask, render_template, request, Response, flash, redirect, url_for
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

load_dotenv()


import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

os.chdir('../')
from models import *



class SkillAbility(db.Model):
	__tablename__ = 'skill_ability'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	skill_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))

	def format(self):
		return {
			'id': self.id,
			'skill_id': self.skill_id
		}

class SkillCheck(db.Model):
	__tablename__ = 'skill_check'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	skill_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))

	def format(self):
		return {
			'id': self.id,
			'skill_id': self.skill_id
		}

class SkillCirc(db.Model):
	__tablename__ = 'skill_circ'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	skill_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))

	def format(self):
		return {
			'id': self.id,
			'skill_id': self.skill_id
		}

class SkillDC(db.Model):
	__tablename__ = 'skill_dc'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	skill_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))

	def format(self):
		return {
			'id': self.id,
			'skill_id': self.skill_id
		}

class SkillDegree(db.Model):
	__tablename__ = 'skill_degree'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	skill_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))

	def format(self):
		return {
			'id': self.id,
			'skill_id': self.skill_id
		}

class SkillMod(db.Model):
	__tablename__ = 'skill_mod'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	skill_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))

	def format(self):
		return {
			'id': self.id,
			'skill_id': self.skill_id
		}

class SkillOpposed(db.Model):
	__tablename__ = 'skill_opposed'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	skill_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))

	def format(self):
		return {
			'id': self.id,
			'skill_id': self.skill_id
		}

class SkillTime(db.Model):
	__tablename__ = 'skill_time'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	skill_id = db.Column(db.Integer, db.ForeignKey('skill_bonus.id'))

	def format(self):
		return {
			'id': self.id,
			'skill_id': self.skill_id
		}