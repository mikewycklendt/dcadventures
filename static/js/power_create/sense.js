function sense_check() {
	const check = "sense_check";
	const title = "sense-title";
	const base = 'sense-base';
	const entry = "sense-entry";

	check_title(check, title, base, entry);
}

function sense_base() {
	const field = 'sense_extra';
	const field2 = 'sense_target';
	const entry = "sense-entry";

	base_two(field, field2, entry);
}

function sense_extra() {
	const power_id = select("all_power_select");
	const field = 'sense_extra';
	const fill = 'sense_cost';
	const ranks = 'sense_ranks';
	///const power_id = document.getElementById('power_id');

	id_select(field, fill, power_cost_select, power_id, false, false, false, ranks);
}

function sense_cost() {
	const power_id = select("all_power_select");
	const field = 'sense_cost';
	const fill = 'sense_ranks';
	const extra = 'sense_extra';
	///const power_id = document.getElementById('power_id');

	id_select(field, fill, power_ranks_select, extra, false, false, false, power_id);
}


function sense_sense() {
	const select = 'sense_sense';
	const fill = 'sense_subsense';
	const sub = 'sense';

	id_select(select, fill, subsense_select, sub)
}

function sense_skill() {
	const field_field = document.getElementById("sense_skill");
	const field = field_field.options[field_field.selectedIndex].value;
	const div = document.getElementById("sense-skill-req")

	if (field != '') {
		div.style.opacity = "100%"	
	} else {
		div.style.opacity = "0%";
	}
}

function sense_type() {
	const select = "sense_type";
	const options = [{'val': 'height', 'div': "sense-height"},
					{'val': 'resist', 'div': "sense-resist"},
					{'val': 'conceal', 'div': "sense-conceal"},
					{'val': 'counter_conceal', 'div': 'sense-counter-conceal'},
					{'val': 'light', 'div': 'sense-light-penalty'}];

	select_opacity(select, options);
}

function sense_counter_conceal()   {
	const select = 'sense_counter_conceal';
	const options = [{'val': 'descriptor', 'div': 'sense-counter-conceal-descriptor'}]

	select_opacity(select, options);
}

function sense_light_penalty_trait_type() {
	const select = 'sense_light_penalty_trait_type';
	const fill = 'sense_light_penalty_trait';

	id_select(select, fill, trait_select);
}

function sense_height_trait_type() {
	const select = 'sense_height_trait_type';
	const fill = 'sense_height_trait';

	id_select(select, fill, trait_select);
}

function sense_height_trait() {
	const filter = select('sense_height_trait_type');
	const fill = 'sense_height_trait';

	id_select(fill, fill, trait_filter, filter);
}

function sense_resist_trait_type() {
	const select = 'sense_resist_trait_type';
	const fill = 'sense_resist_trait';

	id_select(select, fill, trait_select);
}

function sense_resist_trait() {
	const filter = select('sense_resist_trait_type');
	const fill = 'sense_resist_trait';

	id_select(fill, fill, trait_filter, filter);
}

function sense_power_req() {
	const check = "sense_height_power_req";
	const div = "sense-height-ensense";

	check_opacity(check, div);
}

function sense_resist_immune() {
	const check = "sense_resist_immune";
	const div = "sense-resist-immune-perm";

	check_opacity(check, div);
}

function sense_dark() {
	const check = "sense_dark";
	const lig = "sense-lighting";

	check_display(check, lig);
}

function sense_time_set() {
	const select = "sense_time_set";
	const options = [{'val': 'value', 'div': "sense-time-value"},
					{'val': 'skill', 'div': "sense-time-skill"},
					{'val': 'bonus', 'div': "sense-time-bonus"}];

	select_maxheight(select, options);
}

function sense_time() {
	const check = "sense_time";
	const div = "sense-time";
	const sen = "sense-entry";

	check_drop(check, div, sen)
}

function sense_ranged() {
	const check = "sense_ranged";
	const div = "sense-distance";
	const sen = "sense-entry";

	check_drop(check, div, sen)
}

function sense_distance() {
	const field_field = document.getElementById("sense_distance")
	const field = field_field.options[field_field.selectedIndex].value;
	const val = document.getElementById("sense-distance-values")
	const fac = document.getElementById("sense-distance-factor")

	if (field == 'flat') {
		val.style.opacity = "100%";
		fac.style.opacity = "0%";
	} else if (field == 'rank') {
		val.style.opacity = "100%";
		fac.style.opacity = "100%";
	} else {
		val.style.opacity = "0%";
		fac.style.opacity = "0%";
	}
}



function sense_dimensional() {
	const check = 'sense_dimensional';
	const div = 'sense-dimensional';
	const entry = 'sense-entry';

	check_drop(check, div, entry);
}

function sense_comprehend(){
	const check = 'sense_comprehend';
	const div = 'sense-comprehend';
	const entry = 'sense-entry';

	check_drop(check, div, entry);
}

function sense_concealment() {
	const select = 'sense_concealment'
	const options = [{'val': 'any', 'div': 'sense-conceal-precise'}]

	select_opacity(select, options);
}

function sense_conceal_power() {
	const check = 'sense_conceal_power';
	const div = 'sense-conceal-power';

	check_display(check, div);
}

function sense_dimensional_type() {
	const select = 'sense_dimensional_type';
	const options = [{'val': 'descriptor', 'div': 'sense-dimensional-type'}]

	select_opacity(select, options);
}

function sense_awareness() {
	const check = 'sense_awareness';
	const div = 'sense-awareness';
	const entry = 'sense-entry';

	check_drop(check, div, entry);
}

function sense_ranged() {
	const check = 'sense_ranged';
	const div = 'sense-ranged';
	const entry ='sense-entry';

	check_drop(check, div, entry);
}

let sense_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function sense_submit() {
	
	const columns = sense_grid.columns;
	const created = sense_grid.titles;
	const font = sense_grid.font;

	const target = select("sense_target");
	const extra_id = select("sense_extra");
	const sense = select("sense_sense");
	const subsense = select("sense_subsense");
	const visual = check("sense_visual");
	const mental = check("sense_mental");
	const tactile = check("sense_tactile");
	const skill = select("sense_skill");
	const sense_type = select("sense_type");
	const height_trait_type = select("sense_height_trait_type");
	const height_trait = select("sense_height_trait");
	const height_power_required = check("sense_height_power_req");
	const height_ensense = select("sense_height_ensense");
	const resist_trait_type = select("sense_resist_trait_type");
	const resist_trait = select("sense_resist_trait");
	const resist_immune = check("sense_resist_immune");
	const resist_permanent = select("sense_resist_perm");
	const resist_circ = select("sense_resist_circ");
	const objects = check("sense_objects");
	const exclusive = check("sense_exclusive");
	const gm = check("sense_gm");
	const dark = check("sense_dark");
	const lighting = select("sense_lighting");
	const time = check("sense_time");
	const dimensional = check("sense_dimensional");
	const radius = check("sense_radius");
	const accurate = check("sense_accurate");
	const acute = check("sense_acute");
	const distance = select("sense_distance");
	const distance_dc = select("sense_dis_dc");
	const distance_mod = select("sense_dis_mod");
	const distance_value= text("sense_dis_value");
	const distance_unit = select("sense_dis_unit");
	const distance_factor = select("sense_dis_factor");
	const dimensional_type = select("sense_dimensional_type");
	const dimensional_descriptor = select("sense_dimensional_descriptor")
	const ranks = select("sense_ranks");
	const cost = select("sense_cost");
	const power_cost = select("cost");
	const circ = select("sense_circ");
	const comprehend = check("sense_comprehend");
	const comprehend_type = select("aense_comprehend_type");
	const concealment = select("sense_concealment");
	const conceal_precise = check("sense_conceal_precise");
	const conceal_power = check("sense_conceal_power");
	const conceal_power_sense = select("sense_conceal_power_sense");
	const multiple = select("sense_multiple");
	const analytical = check("sense_analytical");
	const acute_req = check("sense_acute_req");
	const awareness = check("sense_awareness");
	const awareness_descriptor = select("sense_awareness_descriptor")
	const counter_conceal = select("sense_counter_conceal");
	const counter_conceal_descriptor = select("sense_counter_conceal_descriptor")
	const ranged = check("sense_ranged");
	const range = select("sense_range");
	const ranged_type = select("sense_ranged_type");
	const light_penalty = select("sense_light_penalty");
	const light_penalty_trait_type = select("sense_light_penalty_trait_type");
	const light_penalty_trait = select("sense_light_penalty_trait");
	const ranged_sense = check('sense_ranged_sense')

	///const power_id = document.getElementById('power_id').value;
	const power_id = select("create_power_select");
	
	const errors = 'sense-err';
	const err_line = 'sense-err-line';

	response = fetch('/power/sense/create', {
		method: 'POST',
		body: JSON.stringify({
			'power_id': power_id,
			'extra_id': extra_id,
			'target': target,
			'sense': sense,
			'subsense': subsense,
			'visual': visual,
			'mental': mental,
			'tactile': tactile,
			'skill': skill,
			'sense_type': sense_type,
			'height_trait_type': height_trait_type,
			'height_trait': height_trait,
			'height_power_required': height_power_required,
			'height_ensense': height_ensense,
			'resist_trait_type': resist_trait_type,
			'resist_trait': resist_trait,
			'resist_immune': resist_immune,
			'resist_permanent': resist_permanent,
			'resist_circ': resist_circ,
			'objects': objects,
			'exclusive': exclusive,
			'gm': gm,
			'dark': dark,
			'lighting': lighting,
			'time': time,
			'dimensional': dimensional,
			'radius': radius,
			'accurate': accurate,
			'acute': acute,
			'distance': distance,
			'distance_dc': distance_dc,
			'distance_mod': distance_mod,
			'distance_value': distance_value,
			'distance_unit': distance_unit,
			'distance_factor': distance_factor,
			'dimensional_type': dimensional_type,
			'dimensional_descriptor': dimensional_descriptor,
			'ranks': ranks,
			'cost': cost,
			'columns': columns,
			'created': created,
			'font': font,
			'power_cost': power_cost,
			'circ': circ,
			'comprehend': comprehend,
			'comprehend_type': comprehend_type,
			'concealment': concealment,
			'conceal_precise': conceal_precise,
			'conceal_power': conceal_power,
			'conceal_power_sense': conceal_power_sense,
			'multiple': multiple,
			'analytical': analytical,
			'acute_req': acute_req,
			'awareness': awareness,
			'awareness_descriptor': awareness_descriptor,
			'counter_conceal': counter_conceal,
			'counter_conceal_descriptor': counter_conceal_descriptor,
			'ranged': ranged,
			'range': range,
			'ranged_type': ranged_type,
			'light_penalty': light_penalty,
			'light_penalty_trait_type': light_penalty_trait_type,
			'light_penalty_trait': light_penalty_trait,
			'ranged_sense': ranged_sense
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {
			
			extra_effect_check(jsonResponse)
			
			sense_grid.columns.length = 0;
			sense_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/power/' + table_id + '/delete/'
			create_table('power', jsonResponse, sense_grid, route);
			clear_errors(err_line, errors)

			sense_grid.titles = true;
		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}