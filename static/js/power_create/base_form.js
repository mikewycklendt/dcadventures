function range_type() {
	const check = 'ranged_check';
	const base = 'ranged-base';
	const entry = 'ranged-entry';
	const field = 'range';
	const value = 'rank';
	
	select_entry(check, base, entry, field, value);
}

function power_type() {
	const sense = document.getElementById("sense-entry");
	const sense_check = document.getElementById("sense_check");
	const sense_base = document.getElementById('sense-base');
	const move_base = document.getElementById('move-base');
	const move = document.getElementById("move-entry");
	const move_check = document.getElementById('move_check')
	const field_field = document.getElementById('type');
	const field = field_field.options[field_field.selectedIndex].value;

	sense_base.style.opacity = '0%';
	move_base.style.opacity = '0%';

	if (field == 'sense') {
		sense_base.style.opacity = '100%';
		move_base.style.opacity = '0%';
		sense.style.display = "grid";
		sense.style.maxHeight = sense.scrollHeight + "px";
		sense_check.checked = true;
		move_check.checked = false;
		move.style.maxHeight = "0px";
		setTimeout(function(){move.style.display = 'none'}, 400);
	} else if (field == 'move') {
		sense_base.style.opacity = '0%';
		move_base.style.opacity = '100%';
		move.style.display = "grid";
		move.style.maxHeight = move.scrollHeight + "px";
		move_check.checked = true;
		sense_check.checked = false;
		sense.style.maxHeight = "0px";
		setTimeout(function(){sense.style.display = 'none'}, 400);
	} else {
		sense_base.style.opacity = '0%';
		move_base.style.opacity = '0%';
		move_check.checked = false;
		sense_check.checked = false;
		sense.style.maxHeight = "0px";
		setTimeout(function(){sense.style.display = 'none'}, 400);
		move.style.maxHeight = "0px";
		setTimeout(function(){move.style.display = 'none'}, 400);
	}
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

	trait_select(select, fill);
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

	trait_select(select, fill);
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