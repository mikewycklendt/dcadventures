function circ_check() {
	const circ_check = document.getElementById("circ_check");
	const circ_base_form = document.getElementById("circ-base-form");
	
	if (circ_check.checked == true) {
		circ_base_form.style.opacity = "100%";
	} else {
		circ_base_form.style.opacity = "0%";
	}
}

function circ_base() {
	const circ_skill = document.getElementById("circ_skill");
	const circ_target = document.getElementById("circ_target");
	circskill = circ_skill.options[circ_skill.selectedIndex].value;
	circtarget =  circ_target.options[circ_target.selectedIndex].value;
	console.log(circskill);
	console.log(circtarget);
	const circ_entry = document.getElementById("circ-entry");

	if (circskill != '' && circtarget != '') {
		circ_entry.style.display = "grid";
		circ_entry.style.padding = "1%";
		circ_entry.style.maxHeight = circ_entry.scrollHeight + "px";
		circ_entry.style.padding = "1%";
	} else {
		circ_entry.style.maxHeight = "0px";
		circ_entry.style.padding = "0px";
	}
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
	
	if ( (circskill != '') && (circtarget != '') && ((mod_type_value == 'value' && modifier_value != '' && rnd_value != '' && circ_value != '') || 
		(mod_type_value == 'math' && rnd_value != '' && circ_value != '' && val_value != '' && unit_value != '' &&  mod_value != '') || 
		(mod_type_value == 'adjust' && rnd_value != '' && circ_value != '' && chk_value != '' && adj_value != '' && rank_value != '') || 
		(mod_type_value == 'noequip' && rnd_value != '' && circ_value != '' && modifier_value != ''))) {

		const mod = document.createElement('div');
		mod.className = 'circ-table-modifier'

		if (mod_type_value == 'value') {
			circ_mod_value = modifier_value;
		}
		if (mod_type_value == 'noequip') {
			circ_mod_value = modifier_value;
		}
		if (mod_type_value == 'math') {
			circ_mod_value = mod_value + ' for every ' + val_value + ' ' + unit_value; 
		}
		if (mod_type_value == 'adjust') {
			circ_mod_value = 'check adjust: ' + chk_value + ' rank adjust: ' + adj_value + ' ' + rank_value
		}
		mod.innerHTML = circ_mod_value;

		const rnd = document.createElement('div');
		rnd.className = 'circ-table-rounds';
		rnd.innerHTML = rnd_value;

		const circ = document.createElement('div');
		circ.className = 'circ-table-circ';
		circ.innerHTML = circ_value;

		const circDelete = document.createElement('div');
		circDelete.className = 'circ-table-delete'
		const deleteBtn = document.createElement('button');
		deleteBtn.className = 'circ-xbox';
		deleteBtn.innerHTML = '&cross;';
		deleteBtn.setAttribute('data-id', circ_enter);
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
		
		errors_delete = document.getElementsByClassName('circ-err-line');

		if (typeof errors_delete[0] === "undefined") {
			console.log('no errors defined')
		} else {
			for (i = 0; i < errors_delete.length; i++) {
				errors_delete[i].style.maxHeight = "0px";
				errors_delete[i].style.padding = "0px";
				errors_delete[i].style.marginBottom = "0px";
			}

			errors = document.getElementById('circ-err')

			errors.style.display = "none";
			errors.style.padding = "0px";
			errors.style.maxHeight = "0px";
		}
		
	} else {

		errors_delete = document.getElementsByClassName('circ-err-line');

		for (i = 0; i < errors_delete.length; i++) {
			errors_delete[i].style.display = "none";
		}

		const errors = document.getElementById('circ-err')

		console.log(rnd_value);

		errors.style.display = "grid";
		errors.style.padding = "1%";
		errors.style.maxHeight = errors.scrollHeight + "px";
		errors.style.padding = "1%";

		if (((mod_type_value == 'value') && (modifier_value == '')) || 
			((mod_type_value == 'math') && ((rnd_value == '') || (circ_value == '') || (val_value == '') || (unit_value == '') ||  (mod_value != ''))) || 
			((mod_type_value == 'adjust') && ((chk_value == '') || (adj_value == '') || (rank_value == ''))) || 
			((mod_type_value == 'noequip') && ((circ_value == '') || (modifier_value == '')))) {

			const error = document.createElement('div');
			error.className = 'circ-err-line'
			error.innerHTML = ' You must fill out all modifier fields';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors.style.maxHeight = errors.maxHeight + error.offsetHeight + 10 + 'px';
		
			console.log(error.scrollHeight);
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
			errors.style.maxHeight = errors.maxHeight + error.offsetHeight + 10 + 'px';
			
			console.log(error.scrollHeight);
		}

		if (rnd_value == '') {

			const error = document.createElement('div');
			error.className = 'circ-err-line'
			error.innerHTML = ' You must specify how many rounds this effect lasts.';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors.style.maxHeight = errors.maxHeight + error.offsetHeight + 10 + 'px';
			
			console.log(error.scrollHeight);
		}
	}
};

circ_delete = function() {
	const deletes = document.querySelectorAll('.circ-xbox');
	const mods = document.querySelectorAll('.circ-table-modifier');
	const rnds = document.querySelectorAll('.circ-table-rounds');
	const circs = document.querySelectorAll('.circ-table-circ');
	const deletesDiv = document.querySelectorAll('.circ-table-delete');
	for (let i = 0; i < deletes.length; i++) {
		const btn = deletes[i];
		btn.onclick = function(e) {
			console.log('click')
			mods[i].style.maxHeight = "0px";
			mods[i].style.padding = "0px";
			mods[i].style.marginBottom = "0px";
			rnds[i].style.maxHeight = "0px";
			rnds[i].style.padding = "0px";
			rnds[i].style.marginBottom = "0px";
			circs[i].style.maxHeight = "0px";
			circs[i].style.padding = "0px";
			circs[i].style.marginBottom = "0px";
			deletesDiv[i].style.maxHeight = "0px";
			deletesDiv[i].style.padding = "0px";
			deletesDiv[i].style.marginBottom = "0px";
		}
	}
};

circ_delete();