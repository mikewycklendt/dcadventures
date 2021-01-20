function modifiers_check() {
	const check = "modifiers_check";
	const title = "modifiers-title";
	const base = 'modifiers-base';
	const entry = "modifiers-entry";

	entry_check(check, title, base, entry);
}

function modifiers_trigger() {
	const select = 'modifiers_trigger';
	const options = [{'val': 'environment', 'div': 'modifiers-environment'}, 
					{'val': 'sense', 'div': 'modifiers-sense'}, 
					{'val': 'tools', 'div': 'modifiers-tools'}, 
					{'val': 'skill', 'div': 'modifiers-skill'}, 
					{'val': 'light', 'div': 'modifiers-light'}, 
					{'val': 'cover', 'div': 'modifiers-cover'}, 
					{'val': 'ranged', 'div': 'modifiers-ranged'},
					{'val': 'melee', 'div': 'modifiers-melee'},  
					{'val': 'conceal', 'div': 'modifiers-conceal'},
					{'val': 'conflict', 'div': 'modifiers-conflict'},
					{'val': 'maneuver', 'div': 'modifiers-maneuvers'},
					{'val': 'subsense', 'div': 'modifiers-subsense'},
					{'val': 'condition', 'div': 'modifiers-condition'},
					{'val': 'profession', 'div': 'modifiers-profession'},
					{'val': 'creature', 'div': 'modifiers-creature'},
					{'val': 'emotion', 'div': 'modifiers-emotion'},
					{'val': 'power', 'div': 'modifiers-power'},
					{'val': 'consequence', 'div': 'modifiers-consequence'},
					{'val': 'range', 'div': 'modifiers-range'},
					{'val': 'db', 'div': 'modifiers-profession-other'},
					{'val': 'db', 'div': 'modifiers-creature-other'},
					{'val': 'db', 'div': 'modifiers-emotion-other'},
					{'val': 'db', 'div': 'modifiers-environment-other'}]
	const selects = ['modifiers_profession', 'modifiers_creature', 'modifiers_emotion', 'modifiers_environment'];

	select_opacity(select, options);
	select_reset(select, selects);
}

function modifiers_profession() {
	const select = 'modifiers_profession';
	const options = [{'val': 'other', 'div': 'modifiers-profession-other'}]
	const div = 'modifiers-profession';

	select_other(select, options, div)
} 

function modifiers_creature() {
	const select = 'modifiers_creature';
	const options = [{'val': 'other', 'div': 'modifiers-creature-other'}]
	const div = 'modifiers-creature';

	select_other(select, options, div)
}

function modifiers_emotion() {
	const select = 'modifiers_emotion';
	const options = [{'val': 'other', 'div': 'modifiers-emotion-other'}]
	const div = 'modifiers-emotion';

	select_other(select, options, div)
}

function modifiers_environment() {
	const select = 'modifiers_environment';
	const options = [{'val': 'other', 'div': 'modifiers-environment-other'}]
	const div = 'modifiers-environment';

	select_other(select, options, div)
}

let modifiers_effect = {'status': false}

function modifiers_bonus_effect() {
	const select1 = 'modifiers_bonus_effect';
	const select2 = 'modifiers_penalty_effect';
	const options = [{'val': 'trait', 'div': 'modifiers-bonus-trait'}, 
					{'val': 'check', 'div': 'modifiers-bonus-check'}, 
					{'val': 'conflict', 'div': 'modifiers-bonus-conflict'}];
	const entry = 'modifiers-entry';
	const row = 'modifiers-row3'
	const second = [{'val': 'trait', 'divs': ['modifiers-bonus-defense'], 'select1': 'modifiers_penalty_trait_type', 'select2': 'modifiers_bonus_trait_type'},
					{'val': 'conflict', 'divs': ['modifier-bonus-conflict-defend'], 'select1': 'modifiers_penalty_conflict', 'select2': 'modifiers_bonus_conflict'}];
	const row4 = 'modifiers-row4';

	double_select(select1, select2, options, row, entry)
	hide_secondary_double(select1, select2, second, row4, entry);
	
}

function modifiers_penalty_effect() {
	const select1 = 'modifiers_penalty_effect';
	const select2 = 'modifiers_bonus_effect';
	const options = [{'val': 'trait', 'div': 'modifiers-penalty-trait'}, 
					{'val': 'check', 'div': 'modifiers-penalty-check'}, 
					{'val': 'conflict', 'div': 'modifiers-penalty-conflict'}];
	const entry = 'modifiers-entry';
	const row = 'modifiers-row3';
	const second = [{'val': 'trait', 'divs': ['modifiers-penalty-defense'], 'select1': 'modifiers_penalty_trait_type', 'select2': 'modifiers_bonus_trait_type'},
					{'val': 'conflict', 'divs': ['modifier-penalty-conflict-defend'], 'select1': 'modifiers_penalty_conflict', 'select2': 'modifiers_bonus_conflict'}];
	const row4 = 'modifiers-row4';

	double_select(select1, select2, options, row, entry);
	hide_secondary_double(select1, select2, second, row4, entry);
}

let modifiers_trait_type = {'status': false}

function modifiers_penalty_trait_type() {
	const fill = 'modifiers_penalty_trait';
	const select1 = 'modifiers_penalty_trait_type';
	const select2 = 'modifiers_bonus_trait_type';
	const options = [{'val': 'defense', 'div': 'modifiers-penalty-defense'}];
	const entry = 'modifiers-entry';
	const row = 'modifiers-row4';
	const others = [{'select': 'modifiers_bonus_conflict', 'values': ['5']}];
	
	double_select_second(select1, select2, options, others, row, entry);
	trait_select(select1, fill);
}

function modifiers_bonus_trait_type() {
	const select1 = 'modifiers_bonus_trait_type';
	const select2 = 'modifiers_penalty_trait_type';
	const fill = 'modifiers_bonus_trait';
	const options = [{'val': 'defense', 'div': 'modifiers-bonus-defense'}];
	const entry = 'modifiers-entry';
	const row = 'modifiers-row4';
	const others = [{'select': 'modifiers_penalty_conflict', 'values': ['5']}];

	double_select_second(select1, select2, options, others, row, entry)
	trait_select(select1, fill);
}

function modifiers_penalty_conflict() {
	const select1 = 'modifiers_penalty_conflict';
	const select2 = 'modifiers_bonus_conflict';
	const options = [{'val': '5', 'div': 'modifier-penalty-conflict-defend'}];
	const entry = 'modifiers-entry';
	const row = 'modifiers-row4';
	const others = [{'select': 'modifiers_bonus_trait_type', 'values': ['defense']}];

	double_select_second(select1, select2, options, others, row, entry)
}

function modifiers_bonus_conflict() {
	const select1 = 'modifiers_bonus_conflict';
	const select2 = 'modifiers_penalty_conflict';
	const options = [{'val': '5', 'div': 'modifier-bonus-conflict-defend'}];
	const entry = 'modifiers-entry';
	const row = 'modifiers-row4';
	const others = [{'select': 'modifiers_penalty_trait_type', 'values': ['defense']}];

	double_select_second(select1, select2, options, others, row, entry)
}

let modifiers_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function modifiers_submit() {

	const columns = modifiers_grid.columns;
	const created = modifiers_grid.titles;
	const font = modifiers_grid.font;

	const benefit = select("modifiers_benefit");
	const bonus = select("modifiers_bonus");
	const bonus_type = select("modifiers_bonus_type");
	const penalty = select("modifiers_penalty");
	const penalty_type = select("modifiers_penalty_type");
	const trigger = select("modifiers_trigger");
	const bonus_effect = select("modifiers_bonus_effect");
	const penalty_effect = select("modifiers_penalty_effect");
	const environment = select("modifiers_environment");
	const environment_other = text("modifiers_environment_other");
	const sense = select("modifiers_sense");
	const mod_range = select("modifiers_range");
	const subsense = select("modifiers_subsense");
	const cover = select("modifiers_cover");
	const conceal = select("modifiers_conceal");
	const maneuver = select("modifiers_maneuver");
	const weapon_melee = select("modifiers_weapon_melee");
	const weapon_ranged = select("modifiers_weapon_ranged");
	const tools = select("modifiers_tools");
	const condition = select("modifiers_condition");
	const power = select("modifiers_power");
	const consequence = select("modifiers_consequence");
	const creature = select("modifiers_creature");
	const creature_other = text("modifiers_creature_other");
	const emotion = select("modifiers_emotion");
	const emotion_other = text("modifiers_emotion_other");
	const conflict = select("modifiers_conflict");
	const profession = select("modifiers_profession");
	const profession_other = text("modifiers_profession_other");
	const bonus_trait_type = select("modifiers_bonus_trait_type");
	const bonus_trait = select("modifiers_bonus_trait");
	const bonus_check = select("modifiers_bonus_check");
	const bonus_check_range = select("modifiers_bonus_check_range");
	const bonus_conflict = select("modifiers_bonus_conflict");
	const penalty_trait_type = select("modifiers_penalty_trait_type");
	const penalty_trait = select("modifiers_penalty_trait");
	const penalty_check = select("modifiers_penalty_check");
	const penalty_check_range = select("modifiers_penalty_check_range");
	const penalty_conflict = select("modifiers_penalty_conflict");
	const bonus_active_defense = check("modifiers_bonus_active_defense");
	const bonus_conflict_defend = check("modifiers_bonus_conflict_defend");
	const penalty_active_defense = check("modifiers_penalty_active_defense");
	const penalty_conflict_defend = check("modifiers_penalty_conflict_defend");
	const multiple = select("modifiers_multiple");
	const multiple_count = select("modifiers_multiple_count");
	const lasts = select("modifier_lasts");

	const equip_id = document.getElementById('equip_id').value;

	const errors = 'modifiers-err';
	const err_line = 'modifiers-err-line';

	response = fetch('/equipment/modifiers/create', {
		method: 'POST',
		body: JSON.stringify({
			'equip_id': equip_id,
			'columns': columns,
			'created': created,
			'font': font,
			'benefit': benefit,
			'bonus': bonus,
			'bonus_type': bonus_type,
			'penalty': penalty,
			'penalty_type': penalty_type,
			'trigger': trigger,
			'bonus_effect': bonus_effect,
			'penalty_effect': penalty_effect,
			'environment': environment,
			'environment_other': environment_other,
			'sense': sense,
			'mod_range': mod_range,
			'subsense': subsense,
			'cover': cover,
			'conceal': conceal,
			'maneuver': maneuver,
			'weapon_melee': weapon_melee,
			'weapon_ranged': weapon_ranged,
			'tools': tools,
			'condition': condition,
			'power': power,
			'consequence': consequence,
			'creature': creature,
			'creature_other': creature_other,
			'emotion': emotion,
			'emotion_other': emotion_other,
			'conflict': conflict,
			'profession': profession,
			'profession_other': profession_other,
			'bonus_trait_type': bonus_trait_type,
			'bonus_trait': bonus_trait,
			'bonus_check': bonus_check,
			'bonus_check_range': bonus_check_range,
			'bonus_conflict': bonus_conflict,
			'penalty_trait_type': penalty_trait_type,
			'penalty_trait': penalty_trait,
			'penalty_check': penalty_check,
			'penalty_check_range': penalty_check_range,
			'penalty_conflict': penalty_conflict,
			'bonus_active_defense': bonus_active_defense,
			'bonus_conflict_defend': bonus_conflict_defend,
			'penalty_active_defense': penalty_active_defense,
			'penalty_conflict_defend': penalty_conflict_defend,
			'multiple': multiple,
			'multiple_count': multiple_count,
			'lasts': lasts
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			multiple_field('modifiers-multiple');

			const insert = jsonResponse.new;
			const items = jsonResponse.new_items;

			new_items(insert, items);

			modifiers_grid.columns.length = 0;
			modifiers_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/equipment/' + table_id + '/delete/'
			create_table(jsonResponse, modifiers_grid, route);
			clear_errors(err_line, errors)

			modifiers_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}