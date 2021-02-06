function skill_create() {
	const create_name = 'skill_name'
	const create_add = 'add-skill'
	const create_route = '/skill/create'
	const create_name_div = 'skill-name'
	const hidden_id = 'skill_id'

	create_id(create_name, create_add, create_route, create_name_div, hidden_id);
}

function edit_form() {
	const item_name_edit = 'skill_name_edit'
	const name_div =  'skill-name'
	const item_edit_grid = 'skill-edit-grid'

	item_edit_form(item_name_edit, name_div, item_edit_grid);
}

function head_edit() {
	const item_id = 'skill_id'
	const item_name_edit = 'skill_name_edit'
	const edit_route = '/skill/edit_name'
	const item_name_div = 'skill-name'
	const item_edit_grid = 'skill-edit-grid'
	
	item_edit(item_id, item_name_edit, edit_route, item_name_div, item_edit_grid)
}


skill_save = function() {

	const skill_id = document.getElementById('skill_id').value;
	const description = text("description");
	const ability = select("ability");
	const skill = select("skill");
	const check_type = select("check");
	const action = select("action");
	const type = select("skill_type");
	const dc_type = select("skill_dc_type");
	const dc_value = select("skill_dc_value");
	const dc_mod = select("skill_dc_mod");
	const target = select("target");
	const targets = select("targets");
	const speed_type = select("speed_type");
	const speed_turns = select("speed_turns");
	const speed_direction = select("speed_direction");
	const speed_mod = select("speed_mod");
	const speed_value = select("speed_value");
	const condition = select("condition");
	const advantage = select("advantage");
	const concealment = select("concealment");
	const for_weapon = check("for_weapon");
	const weapon_cat = select("base_weapon_cat");
	const weapon_type = select("base_weapon_type");
	const weapon = select("base_weapon");
	const untrained = check("untrained");
	const tools = check("tools");
	const required_tools = select("required_tools");
	const subskill = check("subskill");
	const check_dc = check("check_dc");
	const secret = check("secret");
	const secret_frequency = select("secret_frequency");
	const ability_check = check("ability_check");
	const check_check = check("check_check");
	const circumstance = check("circ_check");
	const dc = check("dc_check");
	const degree = check("deg_mod_check");
	const levels = check("levels_check");
	const modifiers = check("modifiers_check");
	const opposed = check("opposed_check");
	const time = check("time_check_check");
	const opposed_multiple = select("opposed_multiple");
	const modifiers_multiple = select("modifiers_multiple");
	const modifiers_multiple_count = select("modifiers_multiple_count");

	const errors = 'skill-err';
	const err_line = 'skill-err-line';

	response = fetch('/skill/save', {
		method: 'POST',
		body: JSON.stringify({
			'skill_id': skill_id,
			'description': description,
			'ability': ability,
			'skill': skill,
			'check_type': check_type,
			'action': action,
			'type': type,
			'dc_type': dc_type,
			'dc_value': dc_value,
			'dc_mod': dc_mod,
			'target': target,
			'targets': targets,
			'speed_type': speed_type,
			'speed_turns': speed_turns,
			'speed_direction': speed_direction,
			'speed_mod': speed_mod,
			'speed_value': speed_value,
			'condition': condition,
			'advantage': advantage,
			'concealment': concealment,
			'for_weapon': for_weapon,
			'weapon_cat': weapon_cat,
			'weapon_type': weapon_type,
			'weapon': weapon,
			'untrained': untrained,
			'tools': tools,
			'required_tools': required_tools, 
			'subskill': subskill,
			'check_dc': check_dc,
			'secret': secret,
			'secret_frequency': secret_frequency,
			'ability_check': ability_check,
			'check_check': check_check,
			'circumstance': circumstance,
			'dc': dc,
			'degree': degree,
			'levels': levels,
			'modifiers': modifiers,
			'opposed': opposed,
			'time': time,
			'opposed_multiple': opposed_multiple,
			'modifiers_multiple': modifiers_multiple,
			'modifiers_multiple_count': modifiers_multiple_count
		}),
		headers: {
		'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			window.location.replace('/skill/save/success/' + skill_id);

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})

}

