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
from models import setup_db, Ability, Defense, Modifier, Action
import sys

#db_drop_and_create_all()

app = Flask(__name__)
moment = Moment(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@3.134.26.61:5432/dc'
db = SQLAlchemy()
setup_db(app)
migrate = Migrate(app, db)



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
	size = 'h2' 
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
	
	size = 'h3'

	table = Modifier.query.all()

	return render_template('table.html', table=table, title=title, size=size)

@app.route('/actions')
def actions():

	title = 'Actions'
	
	size = 'h1'

	table = Action.query.all()

	return render_template('table.html', table=table, title=title, size=size)



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

@app.route('/action/create')
def action_create():

	actions = []

	actions.append({
		'name': 'Multiple Actions',
		'cost': True,
		'turn': True,
		'description': 'This kind of action takes more than one standard action and may take up multiple turns.'	
		})

	for action in actions:
		name = action['name']
		cost = action['cost']
		turn = action['turn']
		description= action['description']

		entry = Action(name=name, cost=cost, turn=turn, description=description)
		db.session.add(entry)
		db.session.commit()

	results = Action.query.all()

	for result in results:
		print (result.id)
		print (result.name)
		print (result.cost)
		print (result.turn)
		print (result.description)

	return ('Actions Added')



@app.route('/skills/create')
def skills_create():

	skills = []

	skills.append({
		'name': 'Acrobatics',
		'ability_id': 3,
		'untrained': False,
		'action_id': 1,
		'type': None,
		'tools': False,
		'description': 'Use Acrobatics to flip, dive, roll, tumble, and perform other acrobatic maneuvers, as well as keeping your balance under difficult circumstances.
		})

	skills.append({
		'name': 'Athletics',
		'ability_id': 1,
		'untrained': True,
		'action_id': 2,
		'type': None,
		'tools': False,
		'description': 'Use Athletics for physical feats like climbing, jumping, riding animal mounts, and swimming.'
		})

	skills.append({
		'name': 'Close Combat',
		'ability_id': 5,
		'untrained': True,
		'action_id': 1,
		'type': None,
		'tools': False,
		'description': 'You’re trained with a particular type of close attack, giving you a bonus to your attack checks with it equal to your skill rank (see Attack Check in The Basics and in the Action & Adventure chapter). Each close attack is a separate Close Combat skill with its own rank, and encompasses a single weapon or power, although an array may be considered one power, at the Gamemaster’s discretion (see Arrays in the Powers chapter for more information). \n\n So a hero might have Close Combat (Swords), but Close Combat (Melee Weapons) is too broad. Close Combat (Unarmed) is an option, meaning skill with unarmed strikes like punches and kicks. However, this bonus does not apply to other forms of unarmed combat maneuvers, including, but not limited to, grabbing or tripping. \n\n The bonus from a Close Combat skill applies only to attack checks with the particular attack, not to defenses. For a broader bonus to attack checks that is less than simply raising Fighting rank, see the Close Attack advantage in the Advantages chapter.'
		})

	skills.append({
		'name': 'Deception',
		'ability_id': 8,
		'untrained': True,
		'action_id': 1,
		'type': 1,
		'tools': False,
		'description': 'Deception is the skill of getting others to believe what you want them to believe. It covers things like acting, bluffing, fast-talk, trickery, and subterfuge. \n\n Deception takes as long as it takes to spin-out your story. Uses of Deception in action rounds are generally standard actions, although you can attempt to deceive as a move action by taking a –5 penalty to your check.' 
		})

	skills.append({
		'name': 'Expertise',
		'ability_id': 6,
		'untrained': False,
		'action_id': 5,
		'type': None,
		'tools': False,
		'description': 'Expertise is a broad skill encompassing knowledge and training in a variety of specialized fields, particularly professional disciplines and scholarship. Each is considered a separate skill and training in each is acquired separately, so a former police officer turned district attorney might have Expertise: Police Officer and Expertise: Law, each with their own ranks, for example. \n\n If you are trained in an Expertise, you can practice and make a living at it. You know how to use the tools of that trade, perform the profession’s daily tasks, supervise untrained helpers, and handle common problems. For example, someone trained in Expertise: Sailor knows how to tie basic knots, tend and repair sails, and stand a deck watch at sea. The GM sets DCs for specific tasks using the guidelines provided in The Basics chapter under Checks, keeping in mind that most job-related checks should be considered routine (see Routine Checks in that section). \n\nYou can also make Expertise checks to see if your character knows the answer to a particular question related to the area of expertise, such as a scientist confronted with a technical issue, or a lawyer considering a legal question. The DC is 10 for easy questions, 15 for basic questions, and 20 or higher for difficult questions. You can usually answer questions as a routine check, and the GM may make a check for you in secret, so you won’t know whether or not your character’s skill is entirely up to the task. \n\n Expertise covers all areas except those tasks specifically covered by other skills. So, for example, a police detective is going to be trained in Investigation (and probably Insight and Perception) in addition to Expertise: Police Officer, the same for an intrepid reporter with Expertise: Journalism. A scientist might be trained in Technology alongside Expertise: Science, a doctor needs training in Treatment along with Expertise: Physician, and a trial lawyer is going to want skill in Insight and Persuasion (and possibly Deception) along with the training in the law that comes with Expertise: Lawyer. \n\n The ability modifier for Expertise is typically Intellect, but some areas of expertise may call for different abilities, perhaps depending on the task involved. For example, a technical expert might rely on Intellect to answer questions and handle day-to-day procedures, but need Dexterity to perform the actual functions of the job. Performance skills, such as acting or music, may rely on Presence. The GM sets the ability modifier as needed for the specific Expertise check. \n\n Characters with expertise in a profession are also assumed to be licensed or certified to practice it, if necessary. Problems like licensing issues, professional rivalries, and so forth can be handled as complications (see Complications in the Secret Origins chapter). \n\nThe GM may allow some Expertise checks to be made untrained, especially for “unskilled” areas, measuring broad general knowledge and life experience, but even then an untrained Expertise check cannot be routine, and the character can only handle easy or basic tasks or questions (DC 10-15).' 
		})

	skills.append({
		'name': 'Insight',
		'ability_id': 7,
		'untrained': True,
		'action_id': 3,
		'type': None,
		'tools': False,
		'description': 'You can tell someone’s true intentions and feelings by paying attention to things like body language, inflection, and your own intuition. \n\n A successful Insight check allows you to resist the effects of some interaction skills, becoming aware of the other person’s true intent. You can also use the skill to tell when someone is behaving oddly or for assessing trustworthiness.'
		})

	skills.append({
		'name': 'Intimidation',
		'ability_id': 8,
		'untrained': True,
		'action_id': 1,
		'type': 1,
		'tools': False,
		'description': 'You know how to use threats (both real and implied) toget others to do what you want.'
		})

	skills.append({
		'name': 'Investigation',
		'ability_id': 6,
		'untrained': False,
		'action_id': 5,
		'type': None,
		'tools': False,
		'description': 'You know how to search for and study clues, gather information through interviews and surveillance, and analyze evidence to help solve crimes. The GM may make Investigation checks for you in secret, so you do not know exactly what you have found, or if you may have missed something'
		})

	skills.append({
		'name': 'Perception',
		'ability_id': 7,
		'untrained': True,
		'action_id': 3,
		'type': None,
		'tools': False,
		'description': 'Use this skill to notice and pick up on things. Discerning details—such as clearly hearing conversation or reading fine text—requires at least three degrees of success on the Perception check. \n\n In general, you have a –1 circumstance penalty to Perception checks for every 10 feet between you and what you are trying to perceive. So hearing a noise from 50 feet away is a –5 modifier to your Perception check, for example. \n\n The GM usually makes Perception checks secretly, so you don’t know whether you failed to notice anything, or there was nothing to notice in the first place. The common sorts of Perception checks are:'
		})

	skills.append({
		'name': 'Persuasion',
		'ability_id': 8,
		'untrained': True,
		'action_id': 5,
		'type': 1,
		'tools': False,
		'description': 'You’re skilled in dealing with people, from etiquette and social graces to a way with words and public speaking, all of which helps to get your point across, make a good impression, negotiate, and generally win people over to your way of seeing things. \n\n In negotiations, all participants roll Persuasion checks to see who gains the advantage. Opposed checks also resolve cases where two advocates plead opposing cases before a third party. \n\n Non-player characters each have an initial attitude towards you or your cause. The GM chooses the character’s initial attitude based on circumstances. Most of the time, people are favorable or indifferent toward heroes, but a specific circumstance or complication may call for a different attitude. \n\n You can improve others’ attitudes with a DC 15 Persuasion check. Success improves the subject’s attitude by one step, while every two additional degrees of success improve it by another step (so two steps at three degrees, three steps at five degrees, and so forth). Failure means no change, and more than a degree of failure worsens the subject’s attitude by one step! In the case of a hostile subject, they may outright attack or otherwise interfere with you if their attitude worsens.'
		})

	skills.append({
		'name': 'Ranged Combat',
		'ability_id': 4,
		'untrained': True,
		'action_id': 1,
		'type': None,
		'tools': False,
		'description': 'You’re trained with a particular type of ranged attack, giving you a bonus to your attack checks with it equal to your skill rank (see Attack Check in The Basics and in the Action & Adventure chapter). Each ranged attack is a separate Ranged Combat skill with its own rank, and encompasses a single weapon or power, although an array may be considered one power, at the Gamemaster’s discretion (see Arrays in the Powers chapter for more information). \n\n So a hero might have Ranged Combat (Guns) or Ranged Combat (Fire Control), but Ranged Combat (Powers) is too broad. Ranged Combat (Throwing) is an option and includes both thrown weapons and objects a character simply picks up and throws. \n\n The bonus from a Ranged Combat skill applies only to attack checks with the particular attack, not to defenses. For a broader bonus to attack checks that is less than simply raising Dexterity rank, see the Ranged Attack advantage in the Advantages chapter.'
		})

	skills.append({
		'name': 'Slight of Hand',
		'ability_id': 4,
		'untrained': False,
		'action_id': 1,
		'type': 2,
		'tools': False,
		'description': 'You can perform dexterous feats of legerdemain such aspalming small objects, picking pockets, slipping out of restraints, and so forth. Stage magicians use Sleight of Handlegitimately as a performance skill, but it is most commonlyknown for its criminal applications.'
		})

	skills.append({
		'name': 'Stealth',
		'ability_id': 3,
		'untrained': True,
		'action_id': 2,
		'type': None,
		'tools': False,
		'description': 'You’re skilled in going unnoticed. While using Stealth, youcan move at your speed rank minus 1 with no penalty.Faster than that, up to your full speed, you t'
		})

	skills.append({
		'name': 'Technology',
		'ability_id': 6,
		'untrained': False,
		'action_id': 1,
		'type': None,
		'tools': True,
		'description': 'Technology covers operating, building, repairing, and generally working with technological devices and equipment. Without the proper tools or equipment, you take a –5 penalty to Technology checks for highly unfavorablecircumstances.'
		})

	skills.append({
		'name': 'Treatment',
		'ability_id': 6,
		'untrained': False,
		'action_id': 1,
		'type': 2,
		'tools': True,
		'description': 'You’re trained in treating injuries and ailments. The check DC and effect of Treatment depend on the task:'
		})

	skills.append({
		'name': 'Vehicles',
		'ability_id': 4,
		'untrained': False,
		'action_id': 2,
		'type': 2,
		'tools': False,
		'description': 'Use this skill to operate vehicles, from ground vehicles like cars to boats, planes, or even spaceships! See Vehicles in the Gadgets & Gear chapter for details. \n\n Routine tasks, such as ordinary operation of known vehicles, don’t require a check and may even be done untrained for some vehicles, particularly common ones like cars. Make a check only when operating the vehicle in a stressful or dramatic situation like being chased or attacked, or trying to reach a destination in a limited amount of time. \n\n You can also make Vehicle checks to perform various maneuvers with a vehicle:'
		'table': [
					{'dc': 5, 
					'description': 'Easy (low-speed turn)'},
					{'dc': 10,
					'description': 'Average (sudden reverse, dodging obstacles)'},
					{'dc': 15,
					'description': 'Difficult (tight turns)'},
					{'dc': 20,
					'description': 'Challenging (bootlegger reverse, loop, barrel roll)'},
					{'dc': 25,
					'description': 'Formidable (high-speed maneuvers, jumping or flying around obstacles)'}
					]
		})

	for skill in skills:
		name = skill['name']
		abiliry_id = skill['ability_id']
		untrained = skill['untrained']
		action_id = skill['action_id']
		skill_type = skill['type']
		tools = skill['tools']
		description = skill['dxescription']
		table = skill['table', None]

		entry = Skill(name=name, abiliry_id=abiliry_id, untrained=untrained, action_id=action_id, skill_type=skill_type, tools=tools, description=description, table=table)
		db.session.add(entry)
		db.session.commit()

	results = Skill.query.all()

	for result in results:
		print (result.id)
		print (result.name)
		print (result.table)

	return ('skills added')


 



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)