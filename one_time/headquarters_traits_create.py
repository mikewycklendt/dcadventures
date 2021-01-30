
@app.route('/headquarters_traits/create')
def headquarters_traits_create():

	name = 'Awesome'
	size = 6

	entry = HeadSize(name=name, size=size)
	db.session.add(entry)
	db.session.commit()
	name = 'Colossal'
	size = 5

	entry = HeadSize(name=name, size=size)
	db.session.add(entry)
	db.session.commit()

	name = 'Gargantuan'
	size = 4

	entry = HeadSize(name=name, size=size)
	db.session.add(entry)
	db.session.commit()

	name = 'Huge'
	size = 3

	entry = HeadSize(name=name, size=size)
	db.session.add(entry)
	db.session.commit()

	name = 'Large'
	size = 2

	entry = HeadSize(name=name, size=size)
	db.session.add(entry)
	db.session.commit()

	name = 'Medium'
	size = 1

	entry = HeadSize(name=name, size=size)
	db.session.add(entry)
	db.session.commit()

	name = 'Small'
	size = 0

	entry = HeadSize(name=name, size=size)
	db.session.add(entry)
	db.session.commit()

	name = 'Tiny'
	size = -1

	entry = HeadSize(name=name, size=size)
	db.session.add(entry)
	db.session.commit())

	name = 'Diminutive'
	size = -2

	entry = HeadSize(name=name, size=size)
	db.session.add(entry)
	db.session.commit()

	name = 'Fine'
	size = -3

	entry = HeadSize(name=name, size=size)
	db.session.add(entry)
	db.session.commit()

	name = 'Miniscule'
	size = -4

	entry = HeadSize(name=name, size=size)
	db.session.add(entry)
	db.session.commit()


	results = HeadSize.query.all()

	for result in results:
		print (result.id)
		print (result.name)
		print (result.size)

	return ('headquarters sizes added')


'''
	Combat Simulator: A combat simulator is a special room
equipped with various devices intended to test characters’ powers and skills and allow them to train in realistic combat situations. Generally, a combat simulator has a suite
of equipment that can simulate any appropriate attack effect at a rank up to the HQ power level.
As an additional feature, the combat simulator can project
realistic illusions, allowing it to recreate or simulate almost
any environment. Combat simulators are useful for training
and short “war games” (pitting the characters against
each other or simulated opponents). Clever heroes also
can try to lure intruders into the combat simulator or an
intruder might override the simulator’s control systems
and trap the heroes in it, turning it into a deathtrap.

Communications: The communications feature allows
the headquarters to receive and transmit on a wide range
of radio and TV bands, monitor police and emergency
channels, coordinate communications between members
of a team, and so forth. It includes communications equipment, consoles, and monitors. The system’s access to restricted communication bands depends on the clearance
and skills of the user. Heroes often have access to special
government channels, while a successful Technology skill
check (DC 25) can grant a user illegal access to restricted
systems.

Computer: A state-of-the-art computer system serves the
entire headquarters. This allows characters to make full use of
the Technology skill and the computer can be programmed
to handle routine base functions (including monitoring communications channels and controlling defensive systems).
An artificially intelligent computer system should be created
as a Minion or Sidekick, perhaps with the cost shared among
members of a team. See the Constructs section for more.

Concealed: The headquarters is hidden from the outside
world in some way. It may be camouflaged behind a false
façade, buried underground, or something similar. Note
this is in addition to the Isolated feature, if any. An isolated
headquarters is difficult to reach, while a concealed headquarters is difficult to find in the first place. Skill checks to
locate the headquarters have their DC increased by +10.
Each additional feature applied to this increases the DC
+5, to a maximum of +30.

Defense System: A defense system consists of various
weapon emplacements defending the exterior and interior
of the headquarters. A defense system can have any attack
effect with a cost no greater than twice the HQ power
level. Their attack bonus is equal to the power level.

Deathtraps: A villainous version of the Defense System
feature is deathtraps: the villain’s lair has one or more
fiendish traps suitable for disposing of those pesky heroes.
Some deathtraps are designed as security systems to keep
heroes out: concealed auto-guns, walls of flames, sealing
rooms that fill with water or sand, and so forth. Others are
intended for the slow elimination of captured heroes.
Note that not having this feature does not mean a villain
cannot jury-rig a deathtrap within the lair—say, by chaining
heroes beneath a rocket counting down to launch,
or slowly lowering them into a volcano’s caldera. It just
means there’s no part of the base specifically designed as
a deathtrap.
Also note that, in spite of the name, not all “deathtraps” are necessarily lethal. Some may be intended to merely
incapacitate and capture intruders (more along the lines
of a Defense System), allowing the villain to interrogate
them and then put them into a real deathtrap!

Dimensional Portal: The headquarters has a portal or
gateway to another dimension or dimensions. This can
range from an otherwise innocuous-looking door to a
humming high-tech portal surrounded by support equipment and monitors. The portal provides two-way travel to
and from the other dimension, and it may even reach a
number of related dimensions. At the GM’s discretion, an
appropriate skill check—typically Expertise or Technology—may be required to operate the portal.

Dock: A dock houses water vehicles and includes access
to a nearby waterway, an airlock, or lock system for moving
vehicles in and out of the dock, and dry-dock facilities
for repairing and maintaining water vehicles. The headquarters should be located within reasonable distance of
a body of water to have this feature.

Dual Size: The headquarters has two separate Size categories: its inside category (purchased normally), which
determines the structure’s interior space, and an outside
category, one or more size categories smaller. In essence,
the headquarters is larger on the inside than on the outside!
So a small house, for example, might contain the
space of a huge castle on the inside. The GM may even
allow size categories beyond Awesome, with each additional
category doubling size; expensive HQs could be
pocket universes! Pay the cost of the larger size, plus this
feature, which lets you set the exterior size at any smaller
category.
In general, the exterior dimensions of the HQ cannot be
smaller than a miniscule structure, about the size of a closet
or phone booth (or, say, a wardrobe or police box), large
enough for an adult human to pass through whatever
serves as the base’s entrance. Headquarters that have no
“exterior” structure, such as an extra-dimensional fortress
accessed by a magical talisman, do not have this feature,
but instead have things like Dimensional Portal, Isolated,
Sealed, and the like.

Effect: A headquarters can be given any appropriate
power effect as a feature with the Gamemaster’s approval.
The effect cannot have a total cost greater than twice the
HQ power level and cannot exceed the power level limits.
Effects are assumed to affect either the headquarters or its
occupants, if they do both, apply the Affects Others modifier, or take them as separate features.

Fire Prevention System: The headquarters is equipped
with an automatic system for detecting and extinguishing
fires. Any large open flame sets the system off (beware,
fire-using heroes!). It functions as a Nullify Fire 5 effect. A
computer-controlled fire prevention system can be programmed to ignore certain sources of fire or the system
can be placed on manual control (requiring someone to
throw a switch in order to activate it).

Garage: A garage houses ground vehicles and includes
a ramp, elevator, or other access to move vehicles in and
out, facilities for repairing and maintaining vehicles, and a
sliding access door.

Grounds: In addition to the actual building(s) of the
headquarters, it has a considerable area of land surrounding
it. An HQ can have surrounding land of one size category larger than the structure at no cost, without having
this feature. Having it allows for grounds up to three size
categories larger than the structure, so a large mansion
headquarters could have a colossal area of land.
If the headquarters has features like Defense System and
Security System, they also extend over the grounds (with
fences, sensors, weapon emplacements, and so forth).

Gym: A gym consists of weight-training and other exercise
machines, space for working out, stretching, and similar
exercises, and all the necessary amenities (lockers, showers, etc.). Some HQs may incorporate the gym feature into
the combat simulator, for a multi-purpose training room.
A gym may also include a pool (heated or unheated, good
for aquatic characters), possibly even connected to an
outside body of water, to the base’s dock, or both at no
additional cost.

Hangar: A hangar houses air and space vehicles. It includes
a hatch and/or runway for the vehicles to launch
and facilities for repairing and maintaining flying vehicles.
For some HQs the launch facilities of the hangar may require a long tunnel or other access to the outside.

Holding Cells: These are cells for holding prisoners, usually
temporarily, although some headquarters might have
more permanent holding facilities. The cells are equipped
with Nullify devices (ranked at the HQ power level) or their
basic Toughness is increased by 50%, which option should
be agreed upon by both player and GM (both options for
two features). Heroes use holding cells to contain captured villains until they can be turned over to the proper
authorities while villains use them to keep heroes prisoner
until they can dispose of them in their latest deathtrap.

Infirmary: An infirmary consists of hospital beds and
equipment for the full use of the Treatment skill. An infirmary can provide treatment for a number of characters
equal to the base’s power level at one time and it can be
assumed to have the necessary facilities to handle any unusual
physiology of the base’s owner(s).

Isolated: Headquarters with this feature are situated somewhere out of the way like the Antarctic, the bottom of the
ocean, on top of a lonely mountain peak, even in orbit or
on the Moon. The base’s owner doesn’t have to worry about
things like door-to-door salesmen or other unwanted visitors but the headquarters is also far from civilization (which
can be limiting for heroes unable to travel fast). The headquarters is assumed to provide all the necessary life support for its location, but doesn’t provide characters with the
means to get to the base or travel back. They need the appropriate powers, a vehicle, or a separate base feature.

Laboratory: A laboratory is a facility for performing scientific tests or experiments. It contains all the necessary
162 CHAPTER 7: GADGETS & GEAR scientific equipment, including dedicated computers, if
the headquarters doesn’t have its own computer system.
Characters can use the laboratory to perform research,
study unusual phenomena (including many super-powers),
and so forth. A laboratory may be required for certain
Expertise, Investigation, or Technology skill checks, or provide
a circumstance bonus to those checks.

Library: A library allows for use of various Knowledge
skills when doing research. A library may consist of printed
matter (books and periodicals), microfilm, digital files,
or a combination of all three. A library may facilitate certain
Expertise skill checks and provide a circumstance bonus
for them.

Living Space: The headquarters includes all the necessary
amenities for people to live there full-time. This is usually
a number of residents equal to the HQ’s power level comfortably (possibly more, at the GM’s discretion). It includes
bedrooms or private suites, kitchen facilities, dining area,
and common living areas. Characters can live in a headquarters lacking this feature short-term, but they’re not
likely to be very comfortable.

Personnel: The HQ has a staff of personnel commensurate
with its size and facilities. The staff is made up of characters
created and controlled by the GM and tasked with servicing
the headquarters. As such, they shouldn’t be considered
all-purpose Minions of the occupant(s). A base’s personnel
may help defend it in case of attack, but they’re not going
to go out on missions or otherwise assist outside of their
duties. This feature simply ensures there’s someone taking
care of the place while the owner isn’t at home.
Note that an HQ’s personnel do not have to be ordinary
humans. They could be service robots, magical golems,
animated skeletons, enslaved aliens, trained apes, or just
about anything else the GM chooses to fit with the theme
of the base and its owner(s).

Power System: A power system makes the headquarters
completely independent of outside power. It has its own
generators (which may be solar, geothermal, nuclear,
cosmic, or anything else the designer wants). They provide the base’s entire power needs. The headquarters
also has emergency back-up power should the generators fail. This generally lasts for a number of hours equal
to the HQ’s power level.

Sealed: This is similar to the Isolated feature, except the
lair is sealed off from the outside world rather than isolated
by geographic location. It may be a structure with no
doors, windows, or other outside access, or behind some
sort of barrier. Only the lair’s owner and designated guests
may enter, although the GM should determine means by
which trespassers might do so, including effects like Dimensional
Travel, Insubstantial, Permeate, and Teleport.

Secret: This is similar to the Concealed feature except the
headquarters is not so much concealed as it is “hiding in
plain sight,” its existence as a headquarters unknown. So,
for example, people assume the abandoned house on
the hill or the old, closed-down factory are just that. This
feature increases the DCs of checks to discover the lair—
typically starting at DC 10—by +10, with each additional
application increasing them by +5 to a maximum of +30
(for truly “top-secret” locations).

Security System: Various locks and alarms protect the
headquarters from unauthorized access. A Technology
check (DC 20) overcomes these systems. Each additional
feature increases the DC by +5, to a maximum of DC 40.
The security system may be tied into a defense system (if
the headquarters is equipped with that feature), so triggering an alarm activates the defense system to disable or
restrain the intruder(s).

Self-Repairing: The structure of the headquarters “heals” any damage done to it over time. Essentially, it recovers
like a character does. If this feature is taken twice, the
structure will even rebuild itself in a week if it is destroyed!
If it cannot rebuild in its original location, it reappears in
the nearest suitable place.

Temporal Limbo: Time within the headquarters actually
moves at a different rate than that of the world outside!
Time within the structure is either slowed or sped up compared to the normal passage of time, passing at half or
twice the normal rate. Each additional application of this
feature doubles the ratio of time passage: one-quarter or
four times, one-eighth or eight times, and so forth.
This time differential allows a character within an accelerated Temporal Limbo to spend additional time planning, building, or recovering while little or no time passes
outside, for example. Conversely, it allows characters in
a slowed Temporal Limbo to pass great amounts of time
outside without aging, perhaps allowing for long periods
of self-imposed exile or contemplation.

Workshop: A workshop has all the facilities for making various things. It includes tools, workbenches, supplies, and so
forth. The Gamemaster may rule certain projects require a
dedicated workshop of their own (which is an additional feature). For example, a workshop can easily handle woodworking, metalworking, and machining, but might not be suitable
for creating magical inventions (see Inventing in this chapter), which require a separate dedicated workshop.
'''