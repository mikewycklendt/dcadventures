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
``
function check_type() {
	const check = 'opposed_check'
	const base = 'opposed-base';
	const entry = 'opposed-entry';
	const field = 'check_type';
	const value = '2';

	select_entry(check, base, entry, field, value);
}

function ability() {
	const check = "ability_check";
	const base = 'ability-base';
	const entry = 'ability-entry';
	const field = 'ability';
	const value = 'x';
	const div = 'ability-icon';

	select_entry(check, base, entry, field, value);
	icon_select(field, ability_icon_select, div, false, true, true);

}
 
function speed_type() {
	const select = 'speed_type';
	const options = [{'val': 'value', 'div': 'base-speed-value'}, 
					{'val': 'mod', 'div': 'base-speed-mod'}]

	select_maxheight(select, options);
}

function for_weapon() {
	const check = 'for_weapon';
	const div = 'base-weapon-cat';

	check_opacity(check, div);
}

function base_weapon_cat() {
	const select = 'base_weapon_cat';
	const div = 'base-weapon';
	const fill = 'base_weapon_type';

	select_maxheight_any(select, div);
	id_select(select, fill, weapon_type_select);
}

function base_weapon_type() {
	const select = 'base_weapon_type';
	const fill = 'base_weapon';

	id_select(select, fill, weapon_select);
}

function secret() {
	const check = 'secret';
	const div = 'secret-frequency';

	check_opacity(check, div);
}

function required_tools() {
	const check = 'required_tools';
	const div =  'required-tools';

	check_opacity(check, div);
}