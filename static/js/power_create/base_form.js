function range_type() {
	const check = 'ranged_check';
	const base = 'ranged-base';
	const entry = 'ranged-entry';
	const field = 'range';
	const value = '5';
	
	select_entry(check, base, entry, field, value);
}

function power_type() {
	const sense = "sense-entry";
	const sense_check = "sense_check";
	const sense_base = 'sense-base';
	const move_base = 'move-base';
	const move = "move-entry";
	const move_check = 'move_check'
	const field = 'type';

	select_entry(sense_check, sense_base, sense, field, 'sense');
	select_entry(move_check, move_base, move, field, 'move');
}

function power_dc_type() {
	const select = 'power_dc_type';
	const options = [{'val': 'value', 'div': "power-dc-value"}, {'val': 'mod', 'div': "power-dc-mod"}]

	select_opacity(select, options)
}

function power_dc_table() {
	const check = "dc_check";
	const base = 'dc-base';
	const entry = 'dc-entry';
	const field = 'power_dc_type';
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

	select_entry(check, base, entry, field, value);
}

function partner_trait_type() {
	const select = 'partner_trait_type';
	const fill = 'partner_trait';

	id_select(select, fill, trait_select);
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

	id_select(select, fill, trait_select);
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