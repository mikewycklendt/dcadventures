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

@app.route('/check/create')
def check_create():

	checks = []

	checks.append({
		'name': 'Skill Check',
		'critical': True,
		'dc': True,
		'opposed': False,
		'automatic': False,
		'routine': False,
		'graded': True,
		'roll': True,
		'compare': False,
		'fail': None
	})

	checks.append({
		'name': 'Opposed Check',
		'critical': True,
		'dc': False,
		'opposed': True,
		'automatic': False,
		'routine': True,
		'graded': False,
		'roll': True,
		'compare': False,
		'fail': 1
	})

	checks.append({
		'name': 'Routine Check',
		'critical': False,
		'dc': True,
		'opposed': False,
		'automatic': False,
		'routine': False,
		'graded': True,
		'roll': False,
		'compare': False,
		'fail': None
	})

	checks.append({
		'name': 'Team Check',
		'critical': False,
		'dc': True,
		'opposed': True,
		'automatic': False,
		'routine': False,
		'graded': True,
		'roll': True,
		'compare': False,
		'fail': None
	})

	checks.append({
		'name': 'Attack Check',
		'critical': True,
		'dc': False,
		'opposed': True,
		'automatic': False,
		'routine': False,
		'graded': False,
		'roll': True,
		'compare': False,
		'fail': 1
	})

	checks.append({
		'name': 'Resistance Check',
		'critical': False,
		'dc': True,
		'opposed': False,
		'automatic': False,
		'routine': False,
		'graded': True,
		'compare': False,
		'roll': True,
		'fail': None
	})

	checks.append({
		'name': 'Comparison Check',
		'critical': False,
		'dc':False,
		'opposed': True,
		'automatic': True,
		'routine': False,
		'graded': False,
		'compare':True,
		'roll': False,
		'fail': None
	})

	for check in checks:
		name = check['name']
		critical = check['critical']
		dc = check['dc']
		opposed = check['opposed']
		automatic = check['automatic']
		routine = check['routine']
		graded = check['graded']
		fail = check['fail']

		entry = Check(name=name, critical=critical, dc=dc, opposed=opposed, automatic=automatic, routine=routine, graded=graded, fail=fail)
		db.session.add(entry)
		db.session.commit()

	results = Check.query.all()

	for result in results:
		print (result.id)
		print (result.name)

	return ('Checks Added')

@app.route('/abilities/create')
def abilities_create():
	abilities = []
		
	abilities.append({'name': "Strength",
		'description': ['Damage dealt by your unarmed and strength-based attacks.',
						'How far you can jump.',
						'The amount of weight you can lift, carry, and throw.',
						'Athletics skill checks.'],
		'summary': 'Strength measures sheer muscle power and the ability to apply it. Your Strength rank applies to:'})

	abilities.append({'name': "Stamina",
		'description': ['Toughness defense, for resisting damage.',
						'Fortitude defense, for resisting effects targeting your character’s health.',
						'Stamina checks to resist or recover from things af-fecting your character’s health when a specific de-fense doesn’t apply.'],
		'summary': 'Stamina is health, endurance, and overall physical resil-ience. Stamina is important because it affects a charac-ter’s ability to resist most forms of damage. Your Stamina modifier applies to:'})

	abilities.append({'name': "Agility",
		'description': ['Dodge defense, for avoiding ranged attacks and oth-er hazards.',
						'Initiative bonus, for acting first in combat.',
						'Acrobatics and Stealth skill checks.',
						'Agility checks for feats of coordination, gross move-ment, and quickness when a specific skill doesn’t apply.'],
		'summary': 'Agility is balance, grace, speed, and overall physical coor-dination. Your Agility rank applies to:'})

	abilities.append({'name': "Dexterity",
		'description': ['Attack checks for ranged attacks.',
						'Sleight of Hand and Vehicles skill checks.',
						'Dexterity checks for feats of fine control and preci-sion when a specific skill doesn’t apply.'],
		'summary': 'Dexterity is a measure of hand-eye coordination, precision, and manual dexterity. Your Dexterity rank applies to:'})
					
	abilities.append({'name': "Fighting",
		'description': ['Attack checks for close attacks.',
						'Parry defense, for avoiding close attacks'],
		'summary': 'Fighting measures your character’s ability in close com-bat, from hitting a target to ducking and weaving around any counter-attacks. Your Fighting rank applies to:'})

	abilities.append({'name': "Intellect",
		'description': ['Expertise, Investigation, Technology, and Treatment skill checks.',
						'Intellect checks to solve problems using sheer brain-power when a specific skill doesn’t apply.'],
		'summary': 'Intellect covers reasoning ability and learning. A character with a high Intellect rank tends to be knowledgeable and well educated. Your Intellect modifier applies to:'})

	abilities.append({'name': "Awareness",
		'description': ['Will defense, for resisting attacks on your mind.',
						'Insight and Perception skill checks.',
						'Awareness checks to resolve matters of intuition when a specific skill doesn’t apply.'],
		'summary': 'While Intellect covers reasoning, Awareness describes common sense and intuition, what some might call “wis-dom.” A character with a high Intellect and a low Aware-ness may be an “absent-minded professor” type, smart but not always aware of what’s going on. On the other hand, a not so bright (low Intellect) character may have a great deal of common sense (high Awareness). Your Awareness modifier applies to:'})

	abilities.append({'name': "Presence",
		'description': ['Deception, Intimidation, and Persuasion skill checks.',
						'Presence checks to influence others through force of personality when a specific skill doesn’t apply.'],
		'summary': 'Presence is force of personality, persuasiveness, leader-ship ability and (to a lesser degree) attractiveness. Pres-ence is useful for heroes who intend to be leaders as well as those who strike fear into the hearts of criminals with their presence. Your Presence modifier applies to:'})
	
	for ability in abilities:
		print (ability['name'])
		name = ability['name']
		print (ability['summary'])
		summary = ability['summary']
		description = ability['description']
		newEntry = Ability(name=name, description=description, summary=summary)
		db.session.add(newEntry)
		db.session.commit()
		for describe in description:
			print (describe)

	return ('abilities')

@app.route('/action/create')
def action_create():

	actions = []

	actions.append({
		'name': 'Standard Action',
		'cost': True,
		'turn': True,
		'description': 'A standard action generally involves acting upon something, whether it’s an attack or using a power to affect something. You’re limited to one standard action each round.'	
		})

	actions.append({
		'name': 'Move Action',
		'cost': True,
		'turn': True,
		'description': 'A move action, like the name implies, usually involves moving. You can take your move action before or afteryour standard action, so you can attack then move, or move then attack. You cannot, however, normally split-up your move action before and after your standard action. Move actions also include things like drawing weapons, standing up, and picking up or manipulating objects.'	
		})

	actions.append({
		'name': 'Free Action',
		'cost': False,
		'turn': True,
		'description': 'A free action is something so comparatively minor it doesn’t take significant time, so you can perform as many free actions in a round as the GM considers reasonable. Free actions include things like talking (heroes and villains always find time to say a lot in the middle of a fight), dropping something, ending the use of a power, activating or maintaining some other powers, and so forth.'	
		})

	actions.append({
		'name': 'Reaction',
		'cost': False,
		'turn': False,
		'description': 'A reaction is something you do in response to something else. A reaction doesn’t take any significant time, like a free action. The difference is you react in response to something else happening during the round, perhaps not even on your turn. Reactions don’t count against your normal allotment of actions and you can react as often as the circumstances dictate, but only when they dictate.'	
		})

	actions.append({
		'name': 'Multiple Actions',
		'cost': True,
		'turn': True,
		'description': 'This kind of action takes more than one standard action and may take up multiple turns.'	
		})

	actions.append({
		'name': 'Conversation',
		'cost': False,
		'turn': False,
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

@app.route('/modifier')
def modifiers_create():
	modifiers = []

	modifiers.append({'name': 'Abilities',
						'cost': 2,
						'description': 'Every ability has a rank associated with it, based on how above or below average it is. Abilities start at rank 0, the baseline average for an adult human being. They can go as low as –5 (truly terrible) and as high as 20, with higher values reserved for truly cosmic beings and forces. The ability rank is added to, or subtracted from, die rolls when your character does something related to that ability. For example, your Strength rank affects the amount of damage you do when punching someone, your Intellect rank comes into play when you roll skills based on Intellect, and so forth. Sometimes your rank is used to calculate another value, such as when you use your Dexterity to determine how good you are at avoiding harm with your reflexes (your Dodge defense). \n\n You choose your hero’s ability ranks by spending power points on them. Increasing an ability rank by 1 costs 2 power points, so putting two points into Strength, for example, raises it from 0 to 1. Remember a rank of 0 is average, 2 is a fair amount of talent or natural ability, 3 is exceptional, 4 extraordinary, and so forth. (See the Ability Benchmarks table for guidelines.) \n\n You can also lower one or more of your character’s ability ranks from the starting value of 0. Each rank you lower an ability gives you an additional two power points to spend elsewhere. You cannot lower an ability rank below –5, which is itself a serious deficiency. Although a rank of 7 is defined as “the peak of human achievement” in an ability on the Ability Benchmarks table, a character with an ability rank greater than 7 isn’t necessarily “non-human,” merely superhuman in comparison to ordinary people. Many “normal human” characters in the comics have truly superhuman abilities, particularly mental abilities. A character can have a superhuman ability rank without necessarily being anything other than an amazingly talented, well-trained human being. The limit of what “normal” people can accomplish is up to the Gamemaster and depends very much on the style of the game. \n\n Enhanced Abilities \n\n Some ability ranks—or portions of them—may be acquired as Enhanced Traits, as described in the Powers chapter. Enhanced Abilities are superhuman powers rather than natural. The key differences between Enhanced Abilities and normal ability ranks are Enhanced Abilities can be nullified (normal abilities cannot, see Nullify) and Enhanced Abilities can have power modifiers and be used for power stunts with extra effort (most normal abilities cannot, see Extra Effort.',
						'table': True
		})

	modifiers.append({'name': 'Debilitated Abiilities',
						'cost': None,
						'description': 'If one of your hero’s ability ranks drops below –5 for any reason, that ability is said to be debilitated and the character suffers more serious effects than just a penalty to certain traits and rolls. Debilitated ability ranks usually result from a power affecting your character. Ability ranks cannot be lowere any further once they are debilitated.',
						'table': False
		})

	modifiers.append({'name': 'Absent Abiliities',
						'cost': -10,
						'description': 'Rather than having a rank of –5 in a given ability, some things or creatures actually lack an ability altogether. These beings automatically fail any check requiring the absent ability. \n\n Lacking an ability is –10 power points; that is, it gives the character an additional 10 power points to spend elsewhere, similar to having a –5 rank in an ability, but with different effects. DC Adventures heroes cannot be absent an ability without Gamemaster permission, as it can have significant effects on the character and the game. \n\n Absent abilities cannot be weakened (see the Weaken effect in the Powers chapter) or debilitated, since they are not present at all in the first place! \n\n  Inanimate objects have no abilities other than their Toughness. Animate, but nonliving, constructs such as robots nor zombies have Strength, Agility, and Dexterity, and may have ranks of Awareness and Presence (if aware of their environment or capable of interaction), and Fighting (if able to make close attacks). They may have Intellect (if capable of independent thought), but have no Stamina (since they are not living things). See Constructs in the Gadgets & Gear chapter for more information.',
						'table': False
		})

	modifiers.append({'name': 'Defense',
						'cost': 1,
						'description': 'Heroes face many hazards in their line of work, from attacks by villainous foes to traps and fiendish mind control. A hero’s defenses are abilities used to avoid such things, determining the difficulty to affect a hero with an attack, or to make resistance checks against them. Each defense is based on a particular ability, modified by the hero’s advantages and powers. For more on defenses in general and how you use them, see the Action & Adventure chapter. \n\n Defensse Rank \n\n Your base defense ranks are equal to your ranks in their associated abilities. You can increase your defenses above the values granted by your ability ranks by spending power points: 1 power point grants you an additional rank in a defense, up to the limits imposed by power level (see Power Level) \n\n With the Enhanced Trait effect (see the Powers chapter) you can also improve your defenses with powers at the same cost, 1 point per rank. \n\n Toughness Rank \n\n The exception is Toughness, which can only be increased above your base Stamina rank using advantages and powers, not by direct spending of power points. This reflects that greater-than-normal Toughness is virtually always some sort of special ability. See the Advantages and Powers chapters for various options for improving Toughness, notably the Defensive Roll advantage and the Protection effect. \n\n Active Defenses \n\n Dodge and Parry defenses require a measure of action to be fully effective. Limits on your mobility, focus, and reaction time adversely affect them. If you are vulnerable, your Dodge and Parry defense ranks are halved (divide their normal values by 2 and round up), and if you are defenseless, they are both reduced to 0!',
						'table': False
		})

	modifiers.append({'name': 'Skills',
						'cost': 1,
						'description': 'Heroes sneak into the closely guarded lairs of criminal masterminds, infiltrate alien computer systems, and build devices beyond the understanding of modern science. They can piece together obscure clues to a villain’s latest plot, run along tightropes, and pilot vehicles through obstacle courses, all in a day’s work. In DC Adventures, they do so through the use of various skills, described in this chapter. \n\n Skills are learned abilities, a combination of training (the skill) and natural talent (an ability rank). Each skill has a rank, used as a bonus to the die roll when using the skill. To make a skill check, roll: \n\n d20 + skill rank + ability modifier + miscellaneous modifiers \n\n  Skill Rank: Your rank in a skill, based on the points you have invested in that skill. If you have ranks in a skill, you’re  considered trained in that skill. You can use some skills even if you don’t have any ranks in them, known as using a skill untrained. Some skills may not be used untrained. \n\n Ability Modifier: Each skill has an ability modifier applied to the skill’s checks. Each skill’s ability modifier is noted in its description and on the Skills table. If you use a skill untrained, the ability modifier still applies to the skill check. \n\n Miscellaneous Modifiers: Miscellaneous modifiers to skill checks include modifiers for circumstances, and bonuses from advantages or powers, among others. \n\n The higher the total, the better the result. You’re usually looking for a total that equals or exceeds a particular difficulty class (DC), which may be based on another character’s traits.\n\n ACQUIRING SKILLS \n\n Give your hero skill ranks by spending power points: \n\n 2 skill ranks per power point. \n\n Skill ranks do not all need to be assigned to the same skill. You can split them between different skills. Characters can perform some tasks without any training, using only raw talent (as defined by their ability ranks), but skilled characters are better at such things. Those with the right combinations of skills and advantages can even hold their own against super-powered opponents. \n\n Skill Cost = 1 power point per 2 skill ranks \n\n HOW SKILLS WORK \n\n When you use a skill, make a skill check to see how you do. Based on the circumstances, your result must match or beat a particular number to use the skill successfully. The harder the task, the higher the number you need to roll. (See Checks) \n\n UNTRAINED SKILL CHECKS \n\n Generally, if you attempt a task requiring a skill you don’t have, you make a skill check as normal. Skill rank doesn’t apply because you don’t have any ranks in the skill. You do get other modifiers, however, such as the skill’s ability modifier. \n\n Many skills can only be used if you are trained in them. Skills that cannot be used untrained are marked with a “No” in the “Untrained” column on the Skills table and listed as “Trained Only” in their descriptions. Attempts touse these skills untrained automatically fail. In some cases, a skill may have both trained and untrained aspects; if you do not have any ranks in that skill, you can only use the untrained ones. \n\n INTERACTION SKILLS \n\n Certain skills, called interaction skills, are aimed at dealing with others through social interaction. Interaction skills allow you to influence the attitudes of others and get them to cooperate with you in one way or another. Since interaction skills are intended for dealing with others socially, they have certain requirements. \n\n First, you must be able to interact with the subject(s) of the skill. They must be aware of you and able to understand you. If they can’t hear or understand you for some reason, you have a –5 circumstance penalty to your skill check (see Circumstance Modifiers in The Basics). \n\n Interaction skills work best on intelligent subjects, ones with an Intellect rank of –4 or better. You can use them on creatures with Int –5, but again with a –5 circumstance penalty; they’re just too dumb to get the subtleties of your point. You can’t use interaction skills at all on subjects lacking one or more mental abilities. (Try convincing a rock to be your friend—or afraid of you—sometime.) \n\n The Immunity effect (see the Powers chapter) can also render characters immune to interaction skills.\n\n You can use interaction skills on groups of subjects at once, but only to achieve the same result for everyone. So you can attempt to use Deception or Persuasion to convince a group of something, or Intimidation to cow a crowd, for example, but you can’t convince some individuals of one thing and the rest of another, or intimidate some and not others. The GM decides if a particular use of an interaction skill is effective against a group, and may apply modifiers depending on the situation. The general rules for interaction still apply: everyone in the group must be able to hear and understand you, for example, or you suffer a –5 on your skill check against them. Mindless subjects are unaffected, as usual. \n\n MANIPULATION SKILLS \n\n Some skills, called manipulation skills, require a degree of fine physical manipulation. You need prehensile limbs and a Strength rank or some suitable Precise power effect to use manipulation skills effectively. If your physical manipulation capabilities are impaired in some fashion (such as having your hands tied or full use of only one hand), the GM may impose a circumstance modifier based on the severity of the impairment. Characters lacking the ability to use manipulation skills can still have ranks in them and use them to oversee or assist the work of others (see Team Checks) ',
						'table': False
		})

	modifiers.append({'name': 'Advantages',
						'cost': 1,
						'description': 'Heroes are more than just skilled; they often have amazing advantages, beyond the abilities of ordinary people. In DC Adventures, advantages often allow heroes to “break the rules,” gaining access to and doing things most people cannot, or simply doing them better. \n\n ACQUIRING ADVANTAGES \n\n Advantages are rated in ranks and bought with power points, just like abilities and skills. Advantages cost 1 power point per rank. Some advantages have no ranks and are acquired only once, effectively at rank 1. \n\n Advantage Cost = 1 power point per advantage rank \n\n ADVANTAGE DESCRIPTIONS \n\n Each advantage’s description explains the benefit it provides. It also says if the advantage can be acquired in ranks and the effects of doing so. Such advantages are listed as “Ranked” alongside the advantage name. Ranks in an advantage are noted with a number after the advantage’s name, such as “Defensive Roll 2” (for a character who has taken two ranks in the Defensive Roll advantage), just like skill and power ranks. If there is a maximum number of ranks a character can take, it’s listed in parentheses after the word “Ranked” in the advantage’s heading. \n\n TYPES OF ADVANTAGES \n\n Advantages are categorized as one of four types: \n\n - Combat Advantages are useful in combat and often modify how various combat maneuvers are performed. \n\n - Fortune Advantages require and enhance the use of hero points. \n\n - General Advantages provide special abilities or bonuses not covered by the other categories. \n\n - Skill Advantages offer bonuses or modifications to skill use. ',
						'table': False
		})

	modifiers.append({'name': 'Powers',
						'cost': None,
						'description': '''Although some heroes and villains rely solely on their skills and advantages, most are set apart by their superhuman powers. DC Adventures characters can lift tanks, fly through the air, throw lightning from their hands, shoot heat-beams from their eyes, or any number of other amazing things. This chapter describes these and many other powers and how you can create your own. \n\n ACQUIRING POWERS \n\n Players spend power points on various powers for their heroes, like acquiring skills or other traits. A power is made up of one or more effects, possibly with different modifiers, which increase or decrease the cost of the effects. Effects can be used to create any number of different powers. A hero with the Concealment effect (see page 91) could use it to create a power called Blending, Blur, Cloak, Invisibility, Shadowmeld, or anything else appropriate to the character you wish to play. It’s all a matter of how powerful the effect is and what modifiers have been placed on it to increase or decrease its performance. Another way to think of it is that this book is filled with effects, but your character sheet is filled with powers. \n\n POWER COSTS \n\n Power effects are acquired in ranks, like ranks for other traits. The more ranks an effect has, the greater its effect. Each effect of a power has a standard cost per rank. \n\n MODIFIERS \n\n Modifiers change how an effect works, making it more effective (an extra) or less effective (a flaw). Modifiers have ranks, just like other traits. Extras increase a power’s cost while flaws decrease it. Some modifiers increase an effect’s cost per rank, while others apply an unchanging cost to the power’s total; these are called flat modifiers. For more information see Modifiers. \n\n The final cost of a power effect is the base effect cost, modified by extras and flaws, multiplied by rank, with flat modifiers applied to the total cost. \n\n Effect Cost = ((base effect cost + extras – flaws) × rank) + flat modifiers \n\n POWER DESCRIPTORS \n\n The rules in this chapter explain what the various powers do, that is, what their game effects are, but it is left up to the player and Gamemaster to apply descriptors to define exactly what a power is and what it looks (and sounds, and feels) like to observers beyond just a collection of game effects. \n\n A power’s descriptors are primarily for color. It’s more interesting and clear to say a hero has a “Flame Blast” or “Lightning Bolt” power than a generic “Damage effect.” “Flame” and “lightning” are descriptors for the Damage effect. Descriptors do have some impact on the game since some effects work only on or with effects of a particular descriptor. A hero may be immune to fire and heat, for example, so any effect with the “fire” or “heat” descriptor doesn’t affect that character. The different sense types (see page 113) are descriptors pertaining to sensory effects. \n\n Generally speaking, a descriptor is part of what a power is called beyond its game system name. For example, a weather-controlling heroine has the following effects: Damage, Concealment, and Environment. Her Damage effect is the power to throw lightning bolts, so it has the descriptor “lightning.” If a villain can absorb electricity, then his power works against the heroine’s Damage (since lightning is electrical in nature). Concealment creates thick banks of fog, giving it the “fog” or “mist” descriptor. So if an opponent transforms into mist, with the ability to regenerate in clouds or fog, he can regenerate inside the heroine’s Concealment area. Her Environment is the power to control the weather, giving it the descriptor “weather.” If the heroine’s power comes as a gift from the gods, it may also have the descriptor “divine” or “magical.” On the other hand, if it comes from her metahuman genetic structure, then it has the descriptor “metahuman.” A villain able to nullify metahuman powers could potentially nullify all of the heroine’s powers! \n\n The number of power descriptors is virtually limitless. The players and Gamemaster should cooperate to apply the appropriate descriptors to characters’ powers and use common sense when dealing with how the different descriptors interact. Just because one hero throws “lightning” and an opponent can absorb “electricity” doesn’t mean the villain’s absorption doesn’t work because it’s not the exact same descriptor. Lightning is a form of electricity. A certain amount of flexibility is built into descriptors, allowing them to cover the full range of possible powers. As in all things, the GM is the final arbitrator and should be consistent when ruling on whether or not a particular descriptor is appropriate and how all effects and descriptors interact in the series. \n\n The powers in this chapter provide numerous examples of descriptors. Feel free to create as many of your own as desired. \n\n NOTICING POWER EFFECTS \n\n Effects with a duration of instant, concentration, or sustained must be noticeable in some way. For example, a Ranged Damage effect might have a visible beam or make a loud noise (ZAP!) or both. Some effects are quite obvious, such as Flight, Insubstantiality, Growth, or Shrinking. Effects with a continuous or permanent duration are not noticeable by default. \n\n If an instant, concentration, or sustained effect’s base duration is changed using modifiers, the effect remains noticeable. A continuous or permanent effect made instant, concentration, or sustained also becomes noticeable. The Subtle modifier (see page 132) can make noticeable powers difficult or impossible to detect. Conversely, the Noticeable modifier makes a normally subtle effect noticeable. \n\n POWERS THAT AREN’T \n\n “Powers” in DC Adventures refer to all extraordinary traits other than abilities, skills, and advantages. Whether a character with powers is “superhuman” or not is largely a matter of opinion and the descriptors used. For example, there are lots of DC characters with superhuman traits still considered “normal” humans. Their amazing effects come from talent, training, luck, self-discipline, devices, or some similar source, with appropriate descriptors. They’re still “powers” in game terms, but they don’t necessarily mean the character is something other than human. \n\n Ultimately it’s up to the GM to decide if having certain effects makes a character something “other than human,” (and what, if anything, that means). \n\n REQUIRED DESCRIPTORS \n\n In some series, the Gamemaster may require certain descriptors for all powers. Usually, a required descriptor reflects some common element of the series. For example, if all characters with powers are metahumans, then all powers have the “metahuman” descriptor by definition, unless the player comes up with a good explanation why they should not. If all characters are psychic metahumans, then all powers have both the “psychic” and “metahuman” descriptors. Likewise, if all powers derive from quantum forces in some way, “quantum” might be a required descriptor. The GM sets the rules as far as what descriptors are required (or restricted) in the series. A character who breaks this guideline—say the one alien in a series where all powers are otherwise metahuman in origin—might have a Benefit (unusual origin) or face certain complications, possibly both. \n\n SAMPLE DESCRIPTORS \n\n Concepts: Anarchy, Balance, Chaos, Evil, Good, Justice, Law, Liberty, Tyranny \n\nElements: Air, Earth, Fire, Plant, Water, Weather \n\n Energy: Acid, Chemical, Cold, Cosmic, Darkness, Electricity, Gravity, Heat, Kinetic, Light, Magnetic, Radiation, Sonic, Vibration \n\n Phenomena: Colors, Dimensions, Dreams, Entropy, Ideas, Luck, Madness, Memes, Mind, Quantum Forces, Space, Thought, Time \n\n Sources: Alien, Biological, Chi, Divine, Magic, Mystic, Metahuman, Preternatural, Primal, Psionic, Psychic, Skill, Technology, Training \n\n EFFECT TYPES \n\n Power effects fall into certain categories or effect types. Effects of the same type follow similar rules and provide descriptors for certain other effects. This section discusses the different effect types and the rules governing them. \n\n ATTACK \n\n Attack effects are used offensively in combat. They require an attack check and damage, hinder, or otherwise harm their target in some way. Attack effects require a standard action to use. Their duration is usually instant although their results—whether damage or some other hindrance—may linger until the target recovers. Attack effects always allow for a resistance check. \n\n CONTROL \n\n Control effects grant the user influence over something, from the environment to the ability to move objects or even create them out of thin air. Control effects require a standard action to initiate, but can then usually be sustained. Control effects used against unwilling targets usually require an attack check and allow a resistance check, the same for the hazards they are capable of causing, such as creating intense cold or dropping a heavy object on someone. \n\n DEFENSE \n\n Defense effects protect in various ways, typically offering a bonus to resistance checks, or granting outright immunity to particular effects or conditions. Most defense effects work only on the user and are subtle and permanent, functioning at all times. Some are activated and sustained as a free action, meaning they can switch on or off, but can potentially leave the user unprotected. \n\n GENERAL \n\n General effects don’t fit into any other particular category. They’re not governed by any special rules other than those given in the effect’s description. \n\n MOVEMENT \n\n Movement effects allow characters to get around in various ways. Some provide a speed rank with a particular form of movement—such as ground, air, or water—while others offer different modes of movement, like walking on walls or slithering along the ground like a snake. \n\n Although activating a movement effect is typically a free action, 
						the character must still take a move action in order to actually move using the effect. So, for example, the action of the Flight effect is “free” and activating it grants the character a Flight speed rank equal to the effect rank. Moving that speed rank still requires a move action, however. \n\n SENSORY \n\n Sensory effects enhance or alter the senses. Some sensory effects improve the user’s senses while others grant entirely new senses or fool the senses in some way. Sensory effects are typically a free action to activate and sustain, or are permanent and always in effect. \n\n SENSE TYPES \n\n Senses in DC Adventures are grouped into sense types, descriptors for how different sensory effects work. The sense types, and some of the senses included in them, are: \n\n - Visual: normal sight, darkvision, infravision, low-light  vision, microscopic vision, ultravision, X-ray vision \n\n - Auditory: normal hearing, sonar (accurate ultrasonic), ultrasonic hearing \n\n - Olfactory: normal smell and taste, scent \n\n - Tactile: normal touch, tremorsense \n\n - Radio: radar (accurate radio), radio \n\n - Mental: mental awareness, Mind Reading, Precognition, Postcognition \n\n - Special: This is the catchall for other sensory descriptors not given above, including unusual senses or exotic descriptors like cosmic, gravitic, magical, and so forth. \n\n\n HOW POWERS WORK \n\nUsing powers is a fairly simple matter. Some power effects work automatically. Others—particularly those affecting other people—require some effort to use, like an attack check or effect check. Powers affecting others allow resistance checks against their effects. \n\n EFFECT CHECKS \n\n In some cases, you may be required to make an effect check to determine how well an effect works. A power check is just like any other check: d20, plus the effect’s rank, plus any applicable modifiers, against a difficulty class set by the Gamemaster. The results of various effect checks are described in this chapter. \n\n Effect Check = d20 + rank + modifiers vs. difficulty class \n\n ROUTINE EFFECT CHECKS \n\n Many power effects allow for routine checks involving their use, generally specified in the effect’s description (see Routine Checks in The Basics chapter). \n\n OPPOSED EFFECT CHECKS \n\n In some cases, usually when one effect is used directly against another, or against a particular trait like an ability or skill, an opposed check is called for (see Opposed Checks in The Basics chapter). If a contest is entirely a matter of whose power is greater, a comparison check (see page 14) is called for; the character with the higher power rank wins automatically. \n\n EFFECT PARAMETERS \n\n Each effect has certain parameters that describe the time needed to use the effect, the subject or target, the distance it works at, and so forth. The basic effect parameters are Action, Range, and Duration. \n\n ACTION \n\n Using or activating an effect requires a particular amount of time. See Actions, page 175, for details about the different types of actions. Modifiers may change the action needed to use an effect. \n\n - Standard: Using the effect requires a standard action. \b\b - Move: Using the effect requires a move action. \b\n - Free: It requires a free action to use or activate the effect. Once an effect is activated or deactivated, it remains so until your next turn. As with all free actions, the GM may limit the total number of effects a hero can turn on or off in a turn. \n\n - Reaction: It requires no action to use the effect. It operates automatically in response to something else, such as an attack. \n\n - None: It requires no action to use the effect. It is always active. \n\n HOW POWERS WORK \n\n Using powers is a fairly simple matter. Some power effects work automatically. Others—particularly those affecting other people—require some effort to use, like an attack check or effect check. Powers affecting others allow resistance checks against their effects. \n\n EFFECT CHECKS \n\n In some cases, you may be required to make an effect check to determine how well an effect works. A power check is just like any other check: d20, plus the effect’s rank, plus any applicable modifiers, against a difficulty class set by the Gamemaster. The results of various effect checks are described in this chapter. \n\n\n Effect Check = d20 + rank + modifiers vs. difficulty class \n\n\n ROUTINE EFFECT CHECKS \n\n Many power effects allow for routine checks involving their use, generally specified in the effect’s description (see Routine Checks in The Basics chapter). \n\n OPPOSED EFFECT CHECKS \n\n In some cases, usually when one effect is used directly against another, or against a particular trait like an ability or skill, an opposed check is called for (see Opposed Checks in The Basics chapter). If a contest is entirely a matter of whose power is greater, a comparison check (see page 14) is called for; the character with the higher power rank wins automatically. \n\n EFFECT PARAMETERS \n\n Each effect has certain parameters that describe the time needed to use the effect, the subject or target, the distance it works at, and so forth. The basic effect parameters are Action, Range, and Duration. \n\n ACTION \n\n Using or activating an effect requires a particular amount of time. See Actions, page 175, for details about the different types of actions. Modifiers may change the action needed to use an effect. \n\n - Standard: Using the effect requires a standard action. \n\n - Move: Using the effect requires a move action. \n\n - Free: It requires a free action to use or activate the effect. Once an effect is activated or deactivated, it remains so until your next turn. As with all free actions, the GM may limit the total number of effects a hero can turn on or off in a turn. \n\n - Reaction: It requires no action to use the effect. It operates automatically in response to something else, such as an attack. \n\n - None: It requires no action to use the effect. It is alwaysactive.\n\n\n RANGE \n\nEach effect has a default range, which may be changed by modifiers. \n\n - Personal: The effect works only on you, the user. \n\n - Close: The effect can target anyone or anything you touch. Touching an unwilling subject requires an unarmed attack check against the subject’s Parry. \n\n - Ranged: The effect works at a distance, limited by perception and path and requiring a ranged attack cheek against the subject’s Dodge defense. A ranged effect has a short range of (rank x 25 feet), a medium range of (rank x 50 feet) and a long range of (rank x 100 feet). Ranged attack checks at medium range suffer a –2 circumstance penalty, while ranged attacks at long range suffer a –5 circumstance penalty. See the Action & Adventure chapter for details. \n\n - Perception: The effect works on any target you can perceive with an accurate sense, without any need for an attack check. If you cannot accurately perceive the target, you cannot affect it. \n\n - Rank: The effect’s range or area of effect is determined by its rank, as given in its description. \n\n\n DURATION \n\n Each effect lasts for a particular amount of time, which may be changed by modifiers. \n\n - Instant: When used, the effect occurs and ends in the same turn, although its results may linger. \n\n - Concentration: You can keep a concentration effect going by taking a standard action each round to do so. If you are incapable of taking the necessary action, or simply choose not to, the effect ends. \n\n - Sustained: You can keep a sustained effect going by taking a free action each round to do so. If you are incapable of taking the necessary action, or simply choose not to, the effect ends. \n\n - Continuous: The effect lasts as long as you wish, without any action required on your part. Once active, it stays that way until you choose to deactivate it (a free action). \n\n - Permanent: The effect is always active and cannot be deactivated, even if you want to. A permanent effect cannot be improved using extra effort. \n\n\n RESISTANCE CHECK \n\n Effects targeting other characters allow a resistance check. The defense used and the difficulty class depend on the effect and its modifiers. \n\n Willing characters can forgo their resistance check against an effect, if they wish. This includes characters who think they’re receiving a beneficial effect, even if they’re not! You can’t forgo Toughness checks, but you may choose to discontinue the use of effects with a duration of Continuous or Sustained that grant a Toughness bonus in order to lower your resistance. \n\n The Immunity effect allows characters to ignore certain effects altogether, removing the need for a resistance check. \n\n COUNTERING EFFECTS \n\n In some circumstances the effects of one power may counter another, negating it. Generally for two effects to counter each other they must have opposed descriptors. For example, light and darkness can counter each other as can heat and cold, water and fire, and so forth. In some cases, such as magical or mental effects, powers of the same descriptor can also counter each other. The GM is the final arbiter as to whether or not an effect with a particular descriptor can counter another. The Nullify effect (see page 111) can counter any effect of a particular descriptor! \n\n HOW COUNTERING WORKS \n\n To counter an effect, you must take the ready action. In doing so, you wait to complete your action until your opponent tries to use a power. You may still move, since ready is a standard action. \n\n You must be able to use the readied effect as a standard action or less. Effects usable as a reaction do not require a ready action; you can use them to counter at any time. Effects requiring longer than a standard action cannot counter during action rounds (although they may be able to counter ongoing effects, see the following section). \n\n If an opponent attempts to use a power you are able to counter, use your countering effect 
						as your readied action. You and the opposing character make effect checks (d20 + rank). If you win, your two powers cancel each other out and there is no effect from either. If the opposing character wins, your attempt to counter is unsuccessful. The opposing effect works normally. \n\n Example: Firestorm is fighting the villainess Killer Frost, who shoots a blast of freezing cold. Having prepared an action, Firestorm’s player says he wants to counter Killer Frost’s ice-blast with a nuclear bolt. The GM agrees the two powers should be able to counter each other, so he asks the player to make a power check for Firestorm’s Nuclear Blast power, while he makes a Cold Control power check for Killer Frost. The player rolls a result of 26 while the GM rolls a result of 19. Firestorm successfully counters the ice-blast, transforming it into a gout of steam and no one takes any damage. \n\n COUNTERING ONGOING EFFECTS You can also use one power to counter the ongoing effect of another, or other lingering results of an instant effect (like flames ignited by a fiery Damage effect). This requires a normal use of the countering effect and an opposed check, as above. If you are successful, you negate the effect (although the opposing character can attempt to reestablish it normally). \n\n INSTANT COUNTERING \n\n You can spend a hero point to attempt to counter another power as a reaction, without the need to ready an action to do so. See Hero Points)''',		
						'table': False
		})

	modifiers.append({'name': 'Flaws',
						'cost': None,
						'description': 'You can add flaws to your effect to reduce the number of power points required for that effect.',
						'table': False
		})

	modifiers.append({'name': 'Extras',
						'cost': None,
						'description': 'You can add extras to powers to increase its modifier by spending power points.',
						'table': False
		})

	modifiers.append({'name': 'Descriptors',
						'cost': None,
						'description': 'DESCRIPTORS \n\n Descriptors help to bring a collection of effects and modifiers to life, differentiating them from similar (or even identical) configurations and making them into distinct powers. Although descriptors don’t always have significant game effects in DC Adventures, they’re perhaps the most important element in providing color and character to the powers of heroes and villains. \n\n Descriptors do have some affect on game play. In particular, descriptors often govern how certain effects interact with each other, serving as convenient shorthand to help define an effect’s parameters. For example, Immunity and Nullify work against effects with specific descriptors; if they were limited solely to things like effect type, it would leave out a tremendous range of options, like “Immunity to Fire” or “Nullify Metahuman Powers,” which are important to the source material. \n\n ', 
						'table': False
		})

	modifiers.append({'name': 'Devices',
						'cost': None,
						'description': 'DEVICES \n\n A device is an item that provides a particular power effect or set of effects. While devices are typically creations of advanced science, they don’t have to be. Many heroes and villains have magical devices such as enchanted weapons and armor, magical talismans, wands and staves of power, and so forth. Some devices are products of alien technology so advanced they might as well be magical, or focuses of psychic or cosmic power beyond the understanding of both magic and science. All devices work the same way in game terms, regardless of their origin or descriptors. \n\n Generally speaking, devices are powers with the Removable flaw applied to them (see Removable in the Powers chapter), meaning the power is external to the character. Take away the device, and the wielder loses the ability to use those powers. So if an armored hero loses access to his battlesuit, for example, he also loses access to the powers tied-up in it. The same is the case if a hero loses a cosmic ring, magic helmet, or alien artifact, which is why Removable is a flaw for those powers. \n\n Just like other powers, devices cost power points (albeit reduced some by the Removable flaw). Characters who want to have and use a device on a regular basis have to pay power points to have it, just like having any other power. The device becomes a part of the character’s abilities. If the device is lost, stolen, or destroyed, the character can replace it, given time, since the device is considered a permanent part of the character. Only a re-allocation of the character’s power points will change this, and Gamemasters should allow characters to re-allocate power points spent on a Removable power if it is somehow permanently lost. \n\n In other cases, characters may make temporary use of a device. Most devices are usable by anyone able to operate them, in which case characters may loan devices to each other, or may pick up and use someone else’s device (or even steal a device away from someone in order to use it against them). The key concept here is the use of the device is temporary, something that happens during a single scene or, at most, a single adventure. If the character wants to continue using the device beyond that, he must pay power points to make the device part of his regular abilities. Otherwise the GM can simply rule that the device is lost, reclaimed by its owner, runs out of power, breaks down, or whatever, and is therefore no longer accessible. Characters with the Inventor and Artificer advantages can create temporary devices for use in an adventure. \n\n Gamemasters may require characters to spend a hero point to make temporary use of a device that doesn’t belong to them, similar to performing a power stunt without suffering fatigue. This helps to limit the loaning and temporary use of devices.',
						'table': False
		})

	modifiers.append({'name': 'Equipment',
						'cost': None,
						'description': 'In addition to their amazing devices, characters often make use of various mundane equipment—ordinary things found in the real world—ranging from a simple set of tools to cell phones, laptop computers, and even common appliances. These items are known as equipment to differentiate them from devices. \n\nEQUIPMENT COST \n\n Equipment is acquired with points from the Equipment advantage. Each piece of equipment has a cost in points, just like other traits. The character pays the item’s cost out of the points from the Equipment advantage and can thereafter have and use that item. \n\n EQUIPMENT EFFECTS AND FEATURES \n\n An item’s cost is based on its effects and features, just like a power (see the Powers chapter), so a ranged weapon has a cost based on its Ranged Damage rank. Equipment often provides the Features effect, including some specific equipment Features described in this chapter. Indeed, some items of equipment provide only Features. \n\n ALTERNATE EQUIPMENT \n\n Just as with power effects, there is a diminishing value in having multiple items with a similar function, or a single piece of equipment with multiple functions, usable only one at a time. Equipment can have the Alternate Effect modifier (see the Extras section of the Powers chapter), such as a weapon capable of different modes of operation. \n\n Characters can also have Alternate Equipment, an array of items usable only one at a time. This is typically a multifunction item, or a kit or collection of various smaller items. The classic example is the utility belt (see its description later in this chapter). Alternate Equipment can also include things like an arsenal of weapons the character can swap out, providing different sets of weapons, with only a limited number usable at once. \n\n ON-HAND EQUIPMENT \n\n Characters may not necessarily carry all their equipment with them at all times. The GM may allow players to spend a hero point in order to have a particular item of equipment “on-hand” at a particular time. This is essentially an equipment “power stunt”—a one-time use of the item for one scene—and the Gamemaster rules whether or not having a particular item on-hand is even possible. For example, a hero out for an evening in his secret identity might have something like a concealed weapon or other small item onhand, but it’s unlikely the character is carrying a large weapon or item unless he has some means of concealing it. \n\n RESTRICTED EQUIPMENT \n\n The Gamemaster may rule some equipment is simply not available or that characters must pay for an additional Feature (or more) in order to have it. This may include certain kinds of weapons, vehicles, and anything else the GM feels should be restricted in the series. \n\n DAMAGING EQUIPMENT \n\n Most equipment can be damaged like other objects (see Damaging Objects), based on its Toughness. Equipment suffering damage loses some effectiveness. The item loses 1 Feature or suffers a –1 circumstance penalty on checks involving it each time it is damaged. These penalties are eliminated once the item is repaired. \n\n REPAIRING AND REPLACING \n\n Repairing an item requires a Technology check. You can also affect jury-rigged repairs to temporarily restore the item to normal (see Technology in the Skills chapter). \n\n  Replacing damaged or destroyed equipment requires only time and resources, although the GM has the final say as to how much time. It’s easy to replace a lost item when the store is right around the corner, harder when it’s the middle of the night or you’re out in the middle of nowhere, or the item is restricted in some fashion. Gamemasters can allow players to spend a hero point to have a replacement for a piece of equipment as an on-hand item (see On-Hand Equipment, previously). \n\n THE LIMITS OF EQUIPMENT \n\n While equipment is useful, it does have its limits, particularly when compared to powers or devices. Equipment is less expensive—it’s cheaper to have a handgun than a Damage power or even a high-tech blaster weapon—but equipment is also more limited. Keep the following limitations of equipment in mind. \n\n TECHNOLOGICAL LIMITS \n\n Equipment includes only items and technology commonly available in the setting. The GM decides what is “commonly available,” but as a rule of thumb assume equipment only includes things from the real world, not battlesuits, anti-gravity devices, shrink rays, and so forth. Those are all devices (see Devices at the start of this chapter). AVAILABILITY \n\n Ownership of some equipment is restricted and the GM decides what is available in the setting. For example, guns may require permits, licenses, waiting periods, and so forth. Also, equipment can be bulky and difficult to carry around. Gamemasters are encouraged to enforce the limitations of carrying a lot of equipment at once. Players who want to have an unusual item of equipment on-hand must either remember to bring it along or use the guidelines for on-hand equipment. Devices are not so limited and characters are assumed to have an easy means of carrying and transporting them. \n\n BONUS STACKING \n\n Equipment bonuses are limited compared to the bonuses granted by other effects. Generally, they do not stack with each other or other types of bonuses, only the highest bonus applies. Thus a hero with a high Protection bonus doesn’t get much, if any, advantage from wearing a bulletproof vest. The only exception to this is Strength-based weapons, and there are limits on them as well (see Melee Weapons, later in this chapter). \n\n NO EXTRA EFFORT \n\n Unlike devices, you do not have the choice of suffering the strain of extra effort when improving equipment, the equipment always takes the strain. You can push your equipment to the limit (eventually causing it to fail) but trying real hard on your part isn’t going to make your car go faster or your gun more effective. You also can’t use extra effort to perform power stunts with equipment. Instead, you must spend a hero point to do so. The GM can always disallow extra effort with equipment if the item is one that is not capable of exceeding its normal operating limits. \n\n DAMAGE AND LOSS \n\n Equipment is subject to damage, malfunctions, and loss, even more so than devices with the Removable flaw (see the flaw description in the Powers chapter). Equipment may be lost or taken away from the character with impunity, and the GM may have equipment fail, run out of ammo or fuel, or otherwise malfunction as a complication.',
						'table': False
		})

	modifiers.append({'name': 'General Equipment',
						'cost': 1,
						'description': 'Most items of general equipment provide Features or other comparatively minor effects. Each is a rank 1 Feature, costing 1 point, unless specified otherwise.',
						'table': False
		})

	modifiers.append({'name': 'Weapons',
						'cost': None,
						'description': 'Weapons of various sorts are common for both heroes and villains. They range from melee weapons to ranged weapons like guns and bows and devices like shrink-rays, mind-control helmets and more. Characters that don’t have any offensive powers often rely on weapons to get the job done.',
						'table': False
		})

	modifiers.append({'name': 'Armor',
						'cost': None,
						'description': 'With so many weapons and super-powered attacks around, characters may need armor to protect them. Some heroes are innately tough enough to stand up to a lot of punishment, while others rely on their high Dodge and Parry ranks. Others choose to wear armor, ranging from ancient metal armors to modern composites or ultra-modern battlesuits. \n\n Armor provides a Protection effect, a bonus to Toughness. Like other equipment, armor bonuses do not stack with other armor or effect bonuses, only the highest bonus applies, one of the reasons why tough heroes rarely, if ever, wear armor. Toughness, even that granted by armor, is limited by your series’ power level. Armor has the following traits: \n\n Category: Armors are categorized as archaic (ancient styles of armor like chain- and plate-mail), modern (typically bulletproof composites and synthetics), and shields (requiring some active use to protect against attacks). \n\n Effect: The effect of most armor is Protection, sometimes with the Impervious modifier. Shields provide a sort of mobile cover (see Cover in the Action & Adventure chapter), granting Enhanced Dodge and Parry defenses. \n\n Cost: This is the armor’s cost in points. Characters pay this cost from their equipment points to have the armor of this type as part of their regular equipment.',
						'table': False
		})

	modifiers.append({'name': 'Vehicles',
						'cost': None,
						'description': 'Not every hero can fly (or teleport, or run at super-speed). Sometimes heroes make use of other means to get around. Vehicles are used primarily for transportation, although they may come with additional capabilities—including weapons— making them useful in other situations as well.',
						'table': False
		})

	modifiers.append({'name': 'Headquarters',
						'cost': None,
						'description': 'Whether it’s an underground cave, the top floors of a skyscraper, a satellite in orbit, or a base on the Moon, many heroesand villains maintain their own secret (or not so secret) headquarters. Teams may even pool their equipment points to have a headquarters they share, with the Gamemaster’s approval. \n\n A character can even have multiple bases of operation (see Alternate Headquarters later in this section). This is more common for villains, who have back-up plans and secret bases they can retreat to when their plans are defeated. If a character’s headquarters is destroyed, the character can choose to rebuild it or build a new headquarters with different features using the same equipment points. Super-villains often go through a succession of different lairs.',
						'table': False
		})

	modifiers.append({'name': 'Conditions',
						'cost': None,
						'description': 'Heroes run into their share of difficulties in their work. One way DC Adventures measures this is with different conditions. They are shorthand for the different game modifiers imposed by things from power effects to injuries or fatigue. So, for example, “vulnerable” is a condition where a hero’s active defenses are reduced. An opponent grabbing them or an entangling mass of glue might make heroes vulnerable, or they might be made vulnerable by a foe’s cunning combat maneuver or being caught off-guard. The game effect is the same (the hero’s active defenses are reduced), so it is easier to just refer to the overall condition as “vulnerable” and describe the different situations that cause it. \n\n This section describes the different conditions that can affect characters in DC Adventures. If multiple conditions apply, use all of their effects. Some conditions supersede other, lesser, conditions, as given in their descriptions.',
						'table': False 
		})

	modifiers.append({'name': 'Extra Effort',
						'cost': None,
						'description': 'Heroes are sometimes called upon to perform feats beyond even their amazing abilities. This calls for extra effort. Players can use extra effort to improve a hero’s abilities in exchange for the hero suffering some fatigue. The benefits of extra effort are not limited by power level due to their extraordinary nature. \n\n Players can have their heroes use extra effort simply by declaring they are doing so. Extra effort is a free action and can be performed at any time during the hero’s turn (but is limited to once per turn). A hero using extra effort gains one of the following benefits:',
						'table': False
		})

	modifiers.append({'name': 'Maneuvers',
						'cost': None,
						'description': 'A maneuver is a different way of performing a particular action. For example, a defensive attack is an attack action that improves your defenses at the cost of accuracy. Maneuvers are optional; you choose which, if any, apply to your action(s) when you declare them. The GM decides if a particular maneuver is appropriate or prohibited by circumstances. \n\n Certain advantages and effects may enhance or work in conjunction with certain maneuvers. See their descriptions for details.',
						'table': False
		})

	modifiers.append({'name': 'Complications',
						'cost': None,
						'description': 'Comic books are full of storylines involving personal complications, and players are encouraged to come up with some for their heroes. Complications have a specific use in the game as well: they give the Gamemaster a “handle” on your hero, different challenges to introduce or include in adventures. When the GM does so, players earn hero points they can use to enhance their characters’ chances of success, amongst other things. (See Hero Points in The Basics and Action & Adventure chapters for more information.) \n\n CHOOSING COMPLICATIONS \n\n Choose at least two complications for your hero: a Motivation and at least one other. You can take as many complications as you wish, although the GM may set limits for the sake of being able to keep track of them all. Complications are also self-limiting, in that you only earn hero points for those complications that actually come into play. So even if you have more than a dozen, if the GM can only include a couple in a game session, then those are the ones that earn you hero points for that game. You can—and generally should—look for opportunities to include your hero’s complications and offer suggestions to the GM, who makes the final decision on which complications come into play at any given time. \n\n Example: Superman has no lack of complications. In addition to his devotion to Doing Good, the Man of Steel has a number of important relationships in his life (his wife Lois, friends and co-workers at the Daily Planet, etc.), long-time foes like Lex Luthor and Brainiac, and vulnerabilities like kryptonite, the loss of his powers under a red sun, and so forth. When the Gamemaster uses one of Superman’s complications in an adventure—say by putting Lois in danger or having a villain set a trap using kryptonite—Superman’s player gets a hero point. If the GM uses multiple complications, having one of Superman’s arch-foes kidnap Lois and set a trap using kryptonite, for example, then his player gets multiple hero points. One of the reasons why powerful heroes’ lives are so complex is they need the hero points those complications provide them! \n\n The GM also decides what complications are appropriate for the game and can overrule any particular complication, based on the style and needs of the story and the series. Keep in mind the adventure needs to have room for all of the heroes’ complications, so individual ones can only come up so often.',
						'table': False
		})

	modifiers.append({'name': 'Hero Points',
						'cost': None,
						'description': 'Whether it’s luck, talent, or sheer determination, heroes have something setting them apart from everyone else, allowing them to perform amazing feats under the most difficult circumstances. In DC Adventures that “something” is hero points. Spending a hero point can make the difference between success and failure in the game. When you’re entrusted with the safety of the world, that means a lot! \n\n Hero points allow players to “edit” the plot of the adventure and the rules of the game to a degree. They give heroes the ability to do the amazing things heroes do in the comics, but with certain limits, and they encourage players to make the sort of choices heroes do in the comics, in order to get more hero points. \n\n Players start each game session with 1 hero point. During the adventure they get opportunities to earn more hero points. Players can use various tokens (poker chips, glass beads, etc.) to keep track of their hero points, handing them over to the Gamemaster when they spend them. The Gamemaster can likewise give out tokens when awarding hero points to the players. \n\n Unspent hero points don’t carry over to the next adventure; the heroes start out with 1 point again. Use them or lose them! Since hero points are a finite resource, players need to manage them carefully, spending them at the most opportune times and taking chances to earn them through complications. Playing it “safe” tends to eliminate chances of getting more hero points while taking risks, facing complications, and, in general, acting like a hero offers rewards that help them out later on.',
						'table': False
		})

	modifiers.append({'name': 'Constructs',
						'cost': None,
						'description': 'Armored robots, humanlike androids, even magically-animated golems or zombies are all examples of constructs, nonliving things capable of acting on their own to one degree or another, carrying out pre-programmed instructions, or even possessing independent thought in some cases. \n\n Since they are capable of action on their own (rather than just improving their owner’s abilities), constructs are considered minions—full-fledged characters—rather than devices or equipment and are acquired using the Minions advantage or summoned or created by a Summon effect. \n\n CONSTRUCT CREATION \n\n Constructs are created exactly like other characters, usingthe guidelines in the Secret Origins chapter, with a fewexceptions. \n\n Constructs are subject to the same power level limits as other characters and the Gamemaster should require constructs controlled by the players to observe these limits. Non-player character constructs have their power level determined the same as other NPCs.',
						'table': False
		})

	for modifier in modifiers:
		name = modifier['name']
		cost = modifier['cost']
		description = modifier['description']
		table = modifier['table']

		entry = Modifier(name=name, cost=cost, description=description, table=table)
		db.session.add(entry)
		db.session.commit()

	added = Modifier.query.all()

	for add in added:
		modifier_id = add.id
		name = add.name

		print(modifier_id)
		print(name)


	return ('modifiers')


@app.route('/modifierid')
def modifierid():

	modifierid = 1

	abilities = Ability.query.all()

	for ability in abilities:
		ability.modifier_id = 1
		db.session.commit()
		db.session.close()

	table = Ability.query.all()

	for row in table:
		print(row.id)
		print(row.name)
		print(row.modifier_id)

	return ('updated modifieer')





	
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)