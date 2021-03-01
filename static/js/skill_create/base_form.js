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
	const field = 'check';
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
	const sub = 'skill_create';

	select_maxheight_any(select, div);
	id_select(select, fill, weapon_type_select, sub);
}

function base_weapon_type() {
	const select = 'base_weapon_type';
	const fill = 'base_weapon';
	const sub = 'skill_create';

	id_select(select, fill, weapon_select, sub);
}

function secret() {
	const check = 'secret';
	const div = 'secret-frequency';
	const shrink = 'secret-trait'

	check_opacity(check, div);
	check_maxheight(check, shrink);
}

function secret_trait_type() {
	const select = 'secret_trait_type';
	const fill = 'secret_trait';

	id_select(select, fill, trait_select);
}

function gm_circ() {
	const check = 'gm_circ';
	const div = 'gm-circ';

	check_opacity(check, div);
}

function partner() {
	const check = 'partner';
	const div = 'base-partner';

	check_opacity(check, div);
}

function partner_type() {
	const select = 'partner_type';
	const options = [{'val': 'trait', 'div': 'partner-trait'},
					{'val': 'equip', 'div': 'partner-equip'},
					{'val': 'feature', 'div': 'partner-feature'},
					{'val': 'tools', 'div': 'partner-tools'},
					{'val': 'materials', 'div': 'partner-materials'}]

	select_maxheight(select, options);
}

function partner_equip_type() {
	const select = 'partner_equip_type';
	const fill = 'partner_equip';

	id_select(select, fill, equipment_select);
}

function partner_trait_type() {
	const select = 'partner_trait_type';
	const fill = 'partner_trait';

	id_select(select, fill, trait_select);
}

function required_tools() {
	const check = 'tools';
	const div =  'required-tools';

	check_opacity(check, div);
}

function opponent_turn() {
	const check = 'opponent_turn';
	const div = 'opponent-turn';

	check_opacity(check, div);
}