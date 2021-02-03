function skill() {	
	const select = 'skill';
	const div = 'skill-icon';

	icon_select(select, skill_icon_select, div, false, true, true);
}

function skill_dc_type() {
	const select = 'skill_dc_type';
	const options = [{'val': 'value', 'div': "skill-dc-value"}, 
					{'val': 'mod', 'div': "skill-dc-mod"}]

	select_opacity(select, options)
}

function skill_dc_table() {
	const check = "dc_check";
	const base = 'dc-base';
	const entry = 'dc-entry';
	const field = 'skill_dc_type';
	const value = 'table';

	select_entry(check, base, entry, field, value);
}

function speed_type() {
	const select = 'speed_type';
	const options = [{'val': 'value', 'div': 'base-speed-value'}, 
					{'val': 'mod', 'div': 'base-speed-mod'}]

	select_maxheight(select, options);
}
