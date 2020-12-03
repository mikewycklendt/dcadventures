function circ_check() {
	const circ_check = "circ_check";
	const circ_base_form = "circ-base-form";
	const title = "circ-title";
	const entry = 'circ-entry';

	check_title(circ_check, title, circ_base_form, entry);
}

function circ_base() {
	const circ_skill = "circ_skill";
	const circ_target = "circ_target";
	const circ_entry = "circ-entry";

	base_two(circ_skill, circ_target, circ_entry);
}


function circ_mod() {
	let circ_mod_type_field = document.getElementById('circ_mod_type');
	let circ_mod_type_value =  circ_mod_type_field.options[circ_mod_type_field.selectedIndex].value;
	let mod_field = document.getElementById('circ-mod-field');
	const value_field = document.getElementById('circ-mod-value');
	const math_field = document.getElementById('circ-mod-math');
	const adjust_field = document.getElementById('circ-mod-adjust');
	const circ_entry = document.getElementById("circ-entry");

	if (circ_mod_type_value == 'value') {
		value_field.style.display = "grid";
		circ_entry.style.maxHeight = circ_entry.scrollHeight + value_field.scrollHeight + "px";
		value_field.style.padding = "1%";
		value_field.style.maxHeight = value_field.scrollHeight + "px";
		math_field.style.display = "none";
		math_field.style.maxHeight = "0px";
		adjust_field.style.display = "none";
		adjust_field.style.maxHeight = "0px";
	} else if (circ_mod_type_value == 'math') {
		math_field.style.display = "grid";
		circ_entry.style.maxHeight = circ_entry.scrollHeight + math_field.scrollHeight + "px";
		math_field.style.padding = "1%";
		math_field.style.maxHeight = math_field.scrollHeight + "px";
		value_field.style.display = "none";
		value_field.style.maxHeight = "0px";
		adjust_field.style.display = "none";
		adjust_field.style.maxHeight = "0px";
	} else if (circ_mod_type_value == 'adjust') {
		adjust_field.style.display = "grid";
		circ_entry.style.maxHeight = circ_entry.scrollHeight + adjust_field.scrollHeight+ "px";
		adjust_field.style.padding = "1%";
		adjust_field.style.maxHeight = adjust_field.scrollHeight + "px";
		value_field.style.display = "none";
		value_field.style.maxHeight = "0px";
		math_field.style.display = "none";
		math_field.style.maxHeight = "0px";
	} else if (circ_mod_type_value == 'noequip') {
		value_field.style.display = "grid";
		circ_entry.style.maxHeight = circ_entry.scrollHeight + value_field.scrollHeight + "px";
		value_field.style.padding = "1%";
		value_field.style.maxHeight = value_field.scrollHeight + "px";
		adjust_field.style.display = "none"
		adjust_field.style.maxHeight = "0px";
		math_field.style.display = "none";
		math_field.style.maxHeight = "0px";
	} else {
		math_field.style.display = "none";
		math_field.style.maxHeight = "0px";
		value_field.style.display = "none";
		value_field.style.maxHeight = "0px";
		adjust_field.style.display = "none";
		adjust_field.style.maxHeight = "0px";
		circ_entry.style.maxHeight = circ_entry.scrollHeight + "px";
	}

};

circ_enter = 0;

function circ_submit() {

	const circ_skill = document.getElementById("circ_skill");
	const circ_target = document.getElementById("circ_target");
	circskill = circ_skill.options[circ_skill.selectedIndex].value;
	circtarget =  circ_target.options[circ_target.selectedIndex].value;
	
	let circ_value = document.getElementById('circumstance_entry').value;
	
	let mod_type_field = document.getElementById('circ_mod_type');
	
	let rnd_field = document.getElementById('circ_mod_rounds');
	let modifier_field = document.getElementById('circ_modifier');
	let mod_field = document.getElementById('circ_mod');
	let unit_field = document.getElementById('circ_mod_unit');
	let chk_field = document.getElementById('circ_adjust_check');
	let adj_field = document.getElementById('circ_adjust_mod');
	let rank_field = document.getElementById('circ_adjust_rank');

	let val_value = document.getElementById('circ_mod_value').value;

	let modifier_value = modifier_field.options[modifier_field.selectedIndex].value;
	let mod_value = mod_field.options[mod_field.selectedIndex].value;
	let unit_value = unit_field.options[unit_field.selectedIndex].value;
	let chk_value = chk_field.options[chk_field.selectedIndex].value;
	let adj_value = adj_field.options[adj_field.selectedIndex].value;
	let rank_value = rank_field.options[rank_field.selectedIndex].value;
	let rnd_value =  rnd_field.options[rnd_field.selectedIndex].value;
	let mod_type_value =  mod_type_field.options[mod_type_field.selectedIndex].value; 

	const bonus_id = document.getElementById('bonus_id').value;
	const error_line = 'circ-err-line';
	const error_table = 'circ-err';
	
	if ( (circskill != '') && (circtarget != '') && ((mod_type_value == 'value' && modifier_value != '' && rnd_value != '' && circ_value != '') || 
		(mod_type_value == 'math' && rnd_value != '' && circ_value != '' && val_value != '' && unit_value != '' &&  mod_value != '') || 
		(mod_type_value == 'adjust' && rnd_value != '' && circ_value != '' && chk_value != '' && adj_value != '' && rank_value != '') || 
		(mod_type_value == 'noequip' && rnd_value != '' && circ_value != '' && modifier_value != ''))) {

		response = fetch('/skill/circ/create', {
			method: 'POST',
			body: JSON.stringify({
				'bonus_id': bonus_id,
				'skill': circskill,
				'target': circtarget,
				'type': mod_type_value,
				'mod': modifier_value,
				'unit_mod': mod_value,
				'unit_value': val_value,
				'unit_type': unit_value,
				'adjust_check_mod': chk_value,
				'adjust_mod': adj_value,
				'adjust_rank': rank_value,
				'equip_mod': modifier_value,
				'rounds': rnd_value,
				'description': circ_value
			}),
			headers: {
			  'Content-Type': 'application/json',
			}
		})
		.then(response => response.json())
		.then(jsonResponse => {
			console.log(jsonResponse)
			if (jsonResponse.success) {

				const mod = document.createElement('div');
				mod.className = 'circ-table-modifier'

				if (mod_type_value == 'value') {
					circ_mod_value = jsonResponse.mod;
				}
				if (mod_type_value == 'noequip') {
					circ_mod_value = jsonResponse.mod;
				}
				if (mod_type_value == 'math') {
					circ_mod_value = jsonResponse.unit_mod + ' for every ' + jsonResponse.unit_value + ' ' + jsonResponse.unit_type; 
				}
				if (mod_type_value == 'adjust') {
					circ_mod_value = 'check adjust: ' + jsonResponse.adjust_check_mod + ' rank adjust: ' + jsonResponse.adjust_mod + ' ' + jsonResponse.adjust_rank;
				}
				mod.innerHTML = circ_mod_value;

				const rnd = document.createElement('div');
				rnd.className = 'circ-table-rounds';
				rnd.innerHTML = jsonResponse.rounds;

				const circ = document.createElement('div');
				circ.className = 'circ-table-circ';
				circ.innerHTML = jsonResponse.description;

				const circDelete = document.createElement('div');
				circDelete.className = 'circ-table-delete'
				const deleteBtn = document.createElement('button');
				deleteBtn.className = 'circ-xbox';
				deleteBtn.setAttribute('data-id', jsonResponse.id);
				circDelete.appendChild(deleteBtn);

				circ_enter = circ_enter + 1;
	
				const table = document.getElementById('circ-table');

				table.style.display = "grid";
				table.style.padding = "1%";
				table.style.maxHeight = table.scrollHeight + "px";
				table.style.padding = "1%";

				table.appendChild(mod);
				table.appendChild(rnd);
				table.appendChild(circ);
				table.appendChild(circDelete);

		
				rows = [mod.scrollHeight, rnd.scrollHeight, circ.scrollHeight];
				let row_height = 0;

				for (i = 0; i < rows.length; i++) {
					if (rows[i] > row_height) {
						row_height = rows[i]
					}
				}
		
				mod.style.maxHeight = mod.scrollHeight + "px";
				rnd.style.maxHeight = rnd.scrollHeight + "px";
				circ.style.maxHeight = circ.scrollHeight + "px";
				circDelete.style.maxHeight = circDelete.scrollHeight + "px";
				table.style.maxHeight = table.scrollHeight + row_height + 15 + "px";

				circ_delete()
		
				clear_errors(error_line, error_table);
			} else {

				back_errors(error_line, error_table);
			}
		})
	} else {

		errors_delete = document.getElementsByClassName('circ-err-line');

		for (i = 0; i < errors_delete.length; i++) {
			errors_delete[i].style.display = "none";
		}

		const errors = document.getElementById('circ-err')

		console.log(rnd_value);

		errors.style.display = "grid";
		errors.style.padding = "1%";

		let errors_height = errors.scrollHeight + 20;

		if (((mod_type_value == 'value') && (modifier_value == '')) || 
			((mod_type_value == 'math') && ((rnd_value == '') || (circ_value == '') || (val_value == '') || (unit_value == '') ||  (mod_value != ''))) || 
			((mod_type_value == 'adjust') && ((chk_value == '') || (adj_value == '') || (rank_value == ''))) || 
			((mod_type_value == 'noequip') && ((circ_value == '') || (modifier_value == '')))) {

			const error = document.createElement('div');
			error.className = 'circ-err-line'
			error.innerHTML = ' You must fill out all modifier fields';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors.style.maxHeight = errors.offsetHeight + error.scrollHeight + 10 + 'px';
		
			console.log(error.offsetHeight);
			console.log(errors.offsetHeight);

			errors_height = errors_height + error.scrollHeight; 
			console.log(errors_height);
		}

		if (circskill == '') {

			const error = document.createElement('div');
			error.className = 'circ-err-line'
			error.innerHTML = ' You must choose a skill check type.';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors.style.maxHeight = errors.maxHeight + error.offsetHeight + 10 + 'px';
		}

		if (circtarget == '') {

			const error = document.createElement('div');
			error.className = 'circ-err-line'
			error.innerHTML = ' You must choose a target';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors.style.maxHeight = errors.maxHeight + error.offsetHeight + 10 + 'px';
		}

		if (circ_value == '') {

			const error = document.createElement('div');
			error.className = 'circ-err-line'
			error.innerHTML = ' You must explain the circumstance.';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors.style.maxHeight = errors.offsetHeight + error.offsetHeight + 10 + 'px';
			
			console.log(error.offsetHeight);
			console.log(errors.offsetHeight);

			errors_height = errors_height + error.scrollHeight;
			console.log(errors_height);
		}

		if (rnd_value == '') {

			const error = document.createElement('div');
			error.className = 'circ-err-line'
			error.innerHTML = ' You must specify how many rounds this effect lasts.';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors.style.maxHeight = errors.offsetHeight + error.offsetHeight + 10 + 'px';
			
			console.log(error.offsetHeight);
			console.log(errors.offsetHeight);

			errors_height = errors_height + error.scrollHeight;
			console.log(errors_height);
		}

		
		errors.style.maxHeight = errors_height + "px";
		errors.style.padding = "1%";
	}
};

circ_delete = function() {
	const deletes = '.circ-xbox';
	const divs = ['circ-table-modifier', 'circ-table-rounds', 'circ-table-circ', 'circ-table-delete'];
	const route = '/skill/circ/delete/';

	delete_function(deletes, divs, route)
};

circ_delete();