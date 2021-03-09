function range_type() {
	const check = 'ranged_check';
	const base = 'ranged-base';
	const entry = 'ranged-entry';
	const field = 'range';
	const value = 'rank';
	
	select_entry(check, base, entry, field, value);
}

function power_type() {
	const sense = "sense-entry";
	const sense_check = "sense_check";
	const sense_base = 'sense-base';
	const move_base = 'move-base';
	const move = "move-entry";
	const move_check = 'move_check';
	const field = 'type';

	
	select_entry(sense_check, sense_base, sense, field, 'sense');
	select_entry(move_check, move_base, move, field, 'move');
}



function advantage_dc_type() {
	const select = 'advantage_dc_type';
	const options = [{'val': 'value', 'div': "advantage-dc-value"}, {'val': 'mod', 'div': "advantage-dc-mod"}]

	select_opacity(select, options)
}

function advantage_dc_table() {
	const check = "dc_check";
	const base = 'dc-base';
	const entry = 'dc-entry';
	const field = 'advantage_dc_type';
	const value = 'table';

	select_entry(check, base, entry, field, value);
}

function circ() {
	const check = 'circ_check';
	const base = 'circ-base';
	const entry = 'circ-entry';
	const field = 'circ';
	const value = 'table';

	select_entry(check, base, entry, field, value);
}

function skill_type() {
	const check = 'skill_check';
	const base = 'skill-base';
	const entry = 'skill-entry';
	const field = 'type';
	const value = '4';

	select_entry(check, base, entry, field, value);	
}

function skill() {
	const type_field = document.getElementById("skill");
	const type = type_field.options[type_field.selectedIndex].value;
	const mod = document.getElementById("skill-grid");

	if (type == 'mod') {
		mod.style.opacity = "100%";
	} else {
		mod.style.opacity  = "0%"
	}
}

function movement() {
	const check = 'move_check';
	const base = 'move-base';
	const entry = "move-entry"
	const field = "action";
	const value = 2;

	select_entry(check, base, entry, field, value);
}

function check_type() {
	const check = 'opposed_check';
	const base = 'opposed-base';
	const entry = 'opposed-entry';
	const field = 'check';
	const value = 2;

	const select = document.getElementById(field)
	const field_value = select.options[select.selectedIndex].value;

	console.log(field_value)


	select_entry(check, base, entry, field, value);
}

function partner_trait_type() {
	const select = 'partner_trait_type';
	const fill = 'partner_trait';

	id_select(select, fill, trait_select, variable_sub);
}

function partner() {
	const field = document.getElementById('partner');
	const val = field.options[field.selectedIndex].value;
	const div = document.getElementById('power-partner');

	if (val == 'skill') {
		div.style.display = 'grid';
		div.style.maxHeight = div.scrollHeight + 'px';
	} else {
		div.style.maxHeight = '0px';
		setTimeout(function(){div.style.display = 'none'}, 400);
	}
}

function routine_trait_type()   {
	const select = 'routine_trait_type';
	const fill = 'routine_trait';

	id_select(select, fill, trait_select, variable_sub);
}

function routine_checkbox() {
	const check = document.getElementById('routine_checkbox');
	const div = document.getElementById('power-routine');
	const val = check.checked;

	if (val == true) {
		div.style.display = 'grid';
		div.style.maxHeight = div.scrollHeight + 'px';
	} else {
		div.style.maxHeight = '0px';
		setTimeout(function(){div.style.display = 'none'}, 400);
	}
}

function invent_trait_type() {
	const select = 'invent_trait_type';
	const fill = 'invent_trait';

	id_select(select, fill, trait_select, variable_sub);
}

function invent_trait() {
	const filter = select('invent_trait_type');
	const fill = 'invent_trait';

	id_select(fill, fill, trait_filter, filter);
}

function invent() {
	const check = 'invent';
	const div1 = 'base-invent-permanence';
	const div2 = 'base-field-invent';

	check_opacity(check, div1);
	check_display(check, div2);
}

function simultaneous() {
	const check = 'simultaneous';
	const div = 'base-simultaneous';

	check_opacity(check, div);
}

function language() {
	const check = 'language';
	const div = 'language-field';

	check_opacity(check, div)
}

function extra_action() {
	const check = 'extra_action';
	const div = 'extra-action';

	check_opacity(check, div);
}

function gm_secret_check() {
	const check = 'gm_secret_check';
	const div = 'gm-check';

	check_maxheight(check, div);
}

function gm_trait_type() {
	const select = 'gm_trait_type';
	const fill = 'gm_trait';

	id_select(select, fill, trait_select, variable_sub)
}

function gm_trait() {
	const filter = select('gm_trait_type');
	const fill = 'gm_trait';

	id_select(fill, fill, trait_filter, filter);
}

function trait_type() {
	const select = 'trait_type';
	const fill = 'trait'
	const check = "variable_check";
	const base = 'variable-base';
	const entry = 'variable-entry';
	const value = 'x';

	select_entry(check, base, entry, select, value);

	id_select(select, fill, trait_select, variable_sub);
}

function base_trait() {
	console.log('word')
	const filter = select('trait_type');
	const fill = 'trait'

	id_select(fill, fill, trait_filter, filter);
}

function replaced_trait_type() {
	const select = 'replaced_trait_type';
	const fill = 'replaced_trait';

	id_select(select, fill, trait_select, variable_sub);
}

function replaced_trait() {
	const filter = select('replaced_trait_type');
	const fill = 'replaced_trait';

	id_select(fill, fill, trait_filter, filter);
}

function skill_type() {
	const select = 'skill_type';
	const fill = 'skill';
	const options = [{'val': 'bonus', 'div': 'base-skill-description'}, {'val': 'skill', 'div': 'base-skill-description'}]
	const div = 'base-pre-check';

	select_opacity_any(select, div);
	select_maxheight(select, options)
	id_select(select, fill, trait_select, any_var_sub);
}

function base_skill_trait() {
	const filter = select('skill_type');
	const fill = 'skill';

	id_select(fill, fill, trait_filter, filter);
}

function ranked() {
	const check = 'ranked';
	const div = 'base-ranked';

	check_opacity(check, div);
}