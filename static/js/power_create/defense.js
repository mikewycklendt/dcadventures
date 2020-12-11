function defense_check() {
	const check = "defense_check";
	const title = "defense-title";
	const base = 'defense-base';
	const entry = "defense-entry";

	check_title(check, title, base, entry);
}

function defense_base() {
	const field = 'defense_extra';
	const entry = "defense-entry";

	base(field, entry);
}

function defense_reflect() {
	const check = 'defense_reflect';
	const div = 'defense-reflect';
	const entry = 'defense-entry';

	check_drop(check, div, entry);
}

function defense_immunity() {
	const check = 'defense_immunity';
	const div = 'defense-immunity';
	const entry = 'defense-entry'

	check_drop(check, div, entry);
}

function defense_reflect_opposed_trait_type() {
	const select = 'defense_reflect_opposed_trait_type';
	const fill = 'defense_reflect_opposed_trait';
	
	trait_select(select, fill);
}

function defense_reflect_resist_trait_type() {
	const select = 'defense_reflect_resist_trait_type';
	const fill = 'defense_reflect_resist_trait';
	
	trait_select(select, fill);
}

function defense_reflect_check() {
	const select = 'defense_reflect_check';
	const options = [{'val': 1, 'div': 'defense-reflect-dc'},
					{'val': 2, 'div': 'defense-reflect-opposed'},
					{'val': 6, 'div': 'defense-reflect-resist'}];

	select_opacity(select, options);
}

function defense_immunity_trait_type() {
	const select = 'defense_immunity_trait_type';
	const fill = 'defense_immunity_trait';

	trait_select(select, fill);
}

function defense_immunity_type() {
	const select = 'defense_immunity_type';
	const options = [{'val': 'trait', 'div': 'defense-immunity-trait'},
					{'val': 'damage', 'div': 'defense-immunity-damage'},
					{'val': 'descriptor', 'div': 'defense-immunity-descriptor'},
					{'val': 'rule', 'div': 'defense-immunity-rule'}]

	select_opacity(select, options);
}

function defense_cover() {
	const check = 'defense_cover';
	const div = 'defense-cover';

	check_opacity(check, div);
}

function defense_submit() {

	const extra = select("defense_extra");
	const defense = select("defense_defense");
	const use = select("defense_use");
	const mod = select("defense_mod");
	const roll = select("defense_roll");
	const outcome = select("defense_outcome");
	const dodge = check("defense_dodge");
	const fortitude = check("defense_fortitude");
	const parry = check("defense_parry");
	const toughness = check("defense_toughness");
	const will = check("defense_will");
	const resist_area = check("defense_resist_area");
	const resist_perception = check("defense_resist_perc");
	const reflect = check("defense_reflect");
	const immunity = check("defense_immunity");
	const reflect_action = select("defense_reflect_action");
	const reflect_check = select("defense_reflect_check");
	const reflect_dc = select("defense_reflect_dc");
	const reflect_opposed_trait_type = select("defense_reflect_opposed_trait_type");
	const reflect_opposed_trait = select("defense_reflect_opposed_trait");
	const reflect_resist_trait_type = select("defense_reflect_resist_trait_type");
	const reflect_resist_trait = select("defense_reflect_resist_trait");
	const immunity_type = select("defense_immunity_type");
	const immunity_trait_type = select("defense_immunity_trait_type");
	const immunity_trait = select("defense_immunity_trait");
	const immunity_descriptor = select("defense_immunity_descriptor");
	const immunity_damage = select("defense_immunity_damage");
	const immunity_rule = select("defense_immunity_rule");
	const cover_check = check("defense_cover_check");
	const cover_type = select("defense_cover_type");

	const power_id = document.getElementById('power_id').value;

	const errors = 'defense-err';
	const err_line = 'defense-err-line';

	response = fetch('/power/defense/create', {
		method: 'POST',
		body: JSON.stringify({
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'defense': self.defense,
			'use': self.use,
			'mod': self.mod,
			'roll': self.roll,
			'outcome': self.outcome,
			'dodge': self.dodge,
			'fortitude': self.fortitude,
			'parry': self.parry,
			'toughness': self.toughness,
			'will': self.will,
			'resist_area': self.resist_area,
			'resist_perception': self.resist_perception,
			'reflect': self.reflect,
			'immunity': self.immunity,
			'reflect_action': self.reflect_action,
			'reflect_check': self.reflect_check,
			'reflect_dc': self.reflect_dc,
			'reflect_opposed_trait_type': self.reflect_opposed_trait_type,
			'reflect_opposed_trait': self.reflect_opposed_trait,
			'reflect_resist_trait_type': self.reflect_resist_trait_type,
			'reflect_resist_trait': self.reflect_resist_trait,
			'immunity_type': self.immunity_type,
			'immunity_trait_type': self.immunity_trait_type,
			'immunity_trait': self.immunity_trait,
			'immunity_descriptor': self.immunity_descriptor,
			'immunity_damage': self.immunity_damage,
			'immunity_rule': self.immunity_rule,
			'cover_check': self.cover_check,
			'cover_type': self.cover_type
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

		} else {

		}
	})
}