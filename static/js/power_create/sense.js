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

function sense_submit() {
	
	const target = select("sense_target");
	const extra = select("sense_extra");
	const sense = select("sense_sense");
	const subsense = select("sense_subsense");
	const sense_cost = select("sense_sense_cost");
	const subsense_cost = select("sense_subsense_cost");
	const skill = select("sense_skill");
	const skill_required = check("sense_skill_req");
	const type = select("sense_type");
	const height_trait_type = select("sense_height_trait_type");
	const height_trait = select("sense_height_trait");
	const  height_power_required = check("sense_height_power_req");
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
	const lighting = select("sense-lighting");
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

}