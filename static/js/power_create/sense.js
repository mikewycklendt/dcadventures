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

function sense_sense() {

	const select = 'sense_sense';
	const fill = 'sense_subsense';

	subsense_select(select, fill)
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
					{'val': 'resist', 'div': "sense-resist"}];

	select_opacity(select, options);
}

function sense_height_trait() {
	const select = 'sense_height_trait_type';
	const fill = 'sense_height_trait';

	trait_select(select, fill)
}

function sense_resist_trait() {
	const select = 'sense_resist_trait_type';
	const fill = 'sense_resist_trait';

	trait_select(select, fill)
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

	check_opacity(check, lig);
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
	const sense_cost = select("sense_sense_cost");
	const subsense_cost = select("sense_subsense_cost");
	const skill = select("sense_skill");
	const skill_required = check("sense_skill_req");
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
	const time_set = select("sense_time_set");
	const time_value = text("sense_time_value");
	const time_unit = select("sense_time_unit");
	const time_skill = select("sense_time_skill");
	const time_bonus = select("sense_time_bonus");
	const time_factor = select("sense_time_factor");
	const distance = select("sense_distance");
	const distance_dc = select("sense_dis_dc");
	const distance_mod = select("sense_dis_mod");
	const distance_value= text("sense_dis_value");
	const distance_unit = select("sense_dis_unit");
	const distance_factor = select("sense_dis_factor");
	const dimensional_type = select("sense_dimensional_type");
	const ranks = select("sense_ranks");
	const cost = select("sense_cost");

	const power_id = document.getElementById('power_id').value;

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
			'sense_cost': sense_cost,
			'subsense_cost': subsense_cost,
			'skill': skill,
			'skill_required': skill_required,
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
			'time_set': time_set,
			'time_value': time_value,
			'time_unit': time_unit,
			'time_skill': time_skill,
			'time_bonus': time_bonus,
			'time_factor': time_factor,
			'distance': distance,
			'distance_dc': distance_dc,
			'distance_mod': distance_mod,
			'distance_value': distance_value,
			'distance_unit': distance_unit,
			'distance_factor': distance_factor,
			'dimensional_type': dimensional_type,
			'ranks': ranks,
			'cost': cost,
			'columns': columns,
			'created': created,
			'font': font
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {
			
			sense_grid.columns.length = 0;
			sense_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/power/' + table_id + '/delete/'
			create_table(jsonResponse, sense_grid, route);
			clear_errors(err_line, errors)

			sense_grid.titles = true;
		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}