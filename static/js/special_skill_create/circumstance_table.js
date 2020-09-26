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

opposed_enter = 0;

function circ_mod() {
	
	let mod_field = document.getElementById('opposed_by_mod');
	let circ_mod_type_field = document.getElementById('circ_mod_type');
	let circ_mod_type_value =  circ_mod_type_field.options[circ_mod_type_field.selectedIndex].value;
	let mod_field = document.getElementById('circ-mod-field');
	let value_field = document.getElementById('circ-mod-value');
	let math_field = document.getElementById('circ-mod-math');
	let adjust_field = document.getElementById('circ-mod-adjust');


	if (circ_mod_type_value = 'value') {
		value_field.style.display = "grid";
		value_field.style.maxHeight = value_field.scrollHeight + "px";
		mod_field.style.display = "grid";
		mod_field.style.maxHeight = mod_field.scrollHeight + 20 + "px";
		math_field.style.display = "none";
		adjust_field.style.display = "none"
	} else if (circ_mod_type_value = 'math') {
		math_field.style.display = "grid";
		math_field.style.maxHeight = value_field.scrollHeight + "px";
		mod_field.style.display = "grid";
		mod_field.style.maxHeight = mod_field.scrollHeight + 20 + "px";
		value_field.style.display = "none";
		adjust_field.style.display = "none"
	} else if (circ_mod_type_value = 'Adjust') {
		adjust_field.style.display = "grid";
		adjust_field.style.maxHeight = value_field.scrollHeight + "px";
		mod_field.style.display = "grid";
		mod_field.style.maxHeight = mod_field.scrollHeight + 20 + "px";
		math_field.style.display = "none";
		math_field.style.display = "none"
	} else if (circ_mod_type_value = 'No equipment') {
		value_field.style.display = "grid";
		value_field.style.maxHeight = value_field.scrollHeight + "px";
		mod_field.style.display = "grid";
		mod_field.style.maxHeight = mod_field.scrollHeight + 20 + "px";
		math_field.style.display = "none";
		adjust_field.style.display = "none"
	} else {
		mod_field.style.maxHeight = "0px";
		mod_field.style.padding = "0px";
		math_field.style.display = "none";
		value_field.style.display = "none";
		adjust_field.style.display = "none"
	}

	console.log(sit_value)
	
	if (opposed_value != '' && mod_value != '' && sit_value != '') {

		const opp = document.createElement('div');
		opp.className = 'opposed-by-table-oppose'
		opp.innerHTML = opposed_value;

		const mod = document.createElement('div');
		mod.className = 'opposed-by-table-mod'
		mod.innerHTML = mod_value;

		const sit = document.createElement('div');
		sit.className = 'opposed-by-table-sit';
		sit.innerHTML = sit_value;

		const oppDelete = document.createElement('div');
		oppDelete.className = 'opposed-by-table-delete'
		const deleteBtn = document.createElement('button');
		deleteBtn.className = 'opposed-by-xbox';
		deleteBtn.innerHTML = '&cross;';
		deleteBtn.setAttribute('data-id', opposed_enter);
		oppDelete.appendChild(deleteBtn);

		opposed_enter = opposed_enter + 1;
	
		table.appendChild(opp);
		table.appendChild(mod);
		table.appendChild(sit);
		table.appendChild(oppDelete);

		
		opp.style.maxHeight = opp.scrollHeight + "px";
		mod.style.maxHeight = mod.scrollHeight + "px";
		sit.style.maxHeight = sit.scrollHeight + "px";
		oppDelete.style.maxHeight = oppDelete.scrollHeight + "px";
		table.style.maxHeight = table.scrollHeight + 20 + "px";

		opposed_by_field.style.opacity = '0%';

		opposed_delete()
	}
};

function opposed_by_submit() {
	const table = document.getElementById('opposed-by-table');

	table.style.display = "grid";
	table.style.padding = "1%";
	table.style.maxHeight = table.scrollHeight + "px";
	table.style.padding = "1%";
	
	let sit_value = document.getElementById('opposed_by_sit').value;
	let opposed_field = document.getElementById('opposed_by');
	let mod_field = document.getElementById('opposed_by_mod');
	let opposed_by_field = document.getElementById('opposed-by-base-form');
	let opposed_value =  opposed_field.options[opposed_field.selectedIndex].value;
	let mod_value =  mod_field.options[mod_field.selectedIndex].value; 

	console.log(sit_value)
	
	if (opposed_value != '' && mod_value != '' && sit_value != '') {

		const opp = document.createElement('div');
		opp.className = 'opposed-by-table-oppose'
		opp.innerHTML = opposed_value;

		const mod = document.createElement('div');
		mod.className = 'opposed-by-table-mod'
		mod.innerHTML = mod_value;

		const sit = document.createElement('div');
		sit.className = 'opposed-by-table-sit';
		sit.innerHTML = sit_value;

		const oppDelete = document.createElement('div');
		oppDelete.className = 'opposed-by-table-delete'
		const deleteBtn = document.createElement('button');
		deleteBtn.className = 'opposed-by-xbox';
		deleteBtn.innerHTML = '&cross;';
		deleteBtn.setAttribute('data-id', opposed_enter);
		oppDelete.appendChild(deleteBtn);

		opposed_enter = opposed_enter + 1;
	
		table.appendChild(opp);
		table.appendChild(mod);
		table.appendChild(sit);
		table.appendChild(oppDelete);

		
		opp.style.maxHeight = opp.scrollHeight + "px";
		mod.style.maxHeight = mod.scrollHeight + "px";
		sit.style.maxHeight = sit.scrollHeight + "px";
		oppDelete.style.maxHeight = oppDelete.scrollHeight + "px";
		table.style.maxHeight = table.scrollHeight + 20 + "px";

		opposed_by_field.style.opacity = '0%';

		opposed_delete()
	}
};

opposed_delete = function() {
	const deletes = document.querySelectorAll('.opposed-by-xbox');
	const opposeds = document.querySelectorAll('.opposed-by-table-oppose');
	const modss = document.querySelectorAll('.opposed-by-table-mod');
	const sits = document.querySelectorAll('.opposed-by-table-sit');
	const deletesDiv = document.querySelectorAll('.opposed-by-table-delete');
	for (let i = 0; i < deletes.length; i++) {
		const btn = deletes[i];
		btn.onclick = function(e) {
			console.log('click')
			opposeds[i].style.maxHeight = "0px";
			opposeds[i].style.padding = "0px";
			opposeds[i].style.marginBottom = "0px";
			modss[i].style.maxHeight = "0px";
			modss[i].style.padding = "0px";
			modss[i].style.marginBottom = "0px";
			sits[i].style.maxHeight = "0px";
			sits[i].style.padding = "0px";
			sits[i].style.marginBottom = "0px";
			deletesDiv[i].style.maxHeight = "0px";
			deletesDiv[i].style.padding = "0px";
			deletesDiv[i].style.marginBottom = "0px";
		}
	}
};

opposed_delete();