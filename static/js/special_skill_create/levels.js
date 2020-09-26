function levels_check() {
	const levels_check = document.getElementById("levels_check");
	const levels_base_form = document.getElementById("levels-base-form");
	
	if (levels_check.checked == true) {
		levels_base_form.style.opacity = "100%";
	} else {
		levels_base_form.style.opacity = "0%";
	}
}

function levels_base() {
	const level_type = document.getElementById("level_type");
	const level_dc_set = document.getElementById("levels_dc_set");
	const level_target = document.getElementById("levels_target");
	levels_dc =  level_dc_set.options[level_dc_set.selectedIndex].value;
	levels_target =  level_target.options[level_target.selectedIndex].value;
	levels_type = level_type.value;
	console.log(levels_dc);
	console.log(levels_target);
	console.log(levels_type);
	const levels_entry = document.getElementById("levels-entry");

	if (levels_type != '' && levels_target != '' && levels_dc != '') {
		levels_entry.style.display = "grid";
		levels_entry.style.padding = "1%";
		levels_entry.style.maxHeight = levels_entry.scrollHeight + "px";
		levels_entry.style.padding = "1%";
	} else {
		levels_entry.style.maxHeight = "0px";
		levels_entry.style.padding = "0px";
	}
}


levels_enter = 0;

function levels_submit() {
	const table = document.getElementById('levels-table');
	let trgt_field = document.getElementById('levels_target');
	let trgt_value = trgt_field.options[trgt_field.selectedIndex].value;
	let type_value = document.getElementById('level_type').value;
	let type_field = document.getElementById('level_type');

	const level_type = document.getElementById('levels-table-type');

	level_type.innerHTML = type_value;
	type_field.style.opacity = "0%;"

	table.style.display = "grid";
	table.style.padding = "1%";
	table.style.maxHeight = table.scrollHeight + "px";
	table.style.padding = "1%";
	
	let lvl_value = document.getElementById('level').value;
	let efct_value = document.getElementById('level_effect').value;
	let dc_field = document.getElementById('levels_dc_set');
	let dc_value =  dc_field.options[dc_field.selectedIndex].value; 

	console.log
	
	if (type_value != '' && lvl_value != '' && efct_value != '' && dc_value != '' && trgt_value != '') {

		const dc = document.createElement('div');
		dc.className = 'levels-table-dc'
		dc.innerHTML = dc_value;

		const lvl = document.createElement('div');
		lvl.className = 'levels-table-level'
		lvl.innerHTML = lvl_value;

		const efct = document.createElement('div');
		efct.className = 'levels-table-effect'
		efct.innerHTML = efct_value;

		const lvlDelete = document.createElement('div');
		lvlDelete.className = 'levels-table-delete'
		const deleteBtn = document.createElement('button');
		deleteBtn.className = 'levels-xbox';
		deleteBtn.innerHTML = '&cross;';
		deleteBtn.setAttribute('data-id', levels_enter);
		lvlDelete.appendChild(deleteBtn);

		levels_enter = levels_enter + 1;
	
		table.appendChild(dc);
		table.appendChild(lvl);
		table.appendChild(efct);
		table.appendChild(lvlDelete);

		
		dc.style.maxHeight = dc.scrollHeight + "px";
		lvl.style.maxHeight = lvl.scrollHeight + "px";
		efct.style.maxHeight = efct.scrollHeight + "px";
		lvlDelete.style.maxHeight = lvlDelete.scrollHeight + "px";
		table.style.maxHeight = table.scrollHeight + 20 + "px";

		levels_delete()
	}
};

levels_delete = function() {
	const deletes = document.querySelectorAll('.levels-xbox');
	const dcs = document.getElementsByClassName('levels-table-dc');
	const lvls = document.getElementsByClassName('levels-table-level');
	const efcts = document.getElementsByClassName('levels-table-effect');
	const deletesDiv = document.getElementsByClassName('levels-table-delete');
	for (let i = 0; i < deletes.length; i++) {
		const btn = deletes[i];
		btn.onclick = function(e) {
			console.log('click')
			dcs[i].style.maxHeight = "0px";
			dcs[i].style.padding = "0px";
			dcs[i].style.marginBottom = "0px";
			lvls[i].style.maxHeight = "0px";
			lvls[i].style.padding = "0px";
			lvls[i].style.marginBottom = "0px";
			efcts[i].style.maxHeight = "0px";
			efcts[i].style.padding = "0px";
			efcts[i].style.marginBottom = "0px";
			deletesDiv[i].style.maxHeight = "0px";
			deletesDiv[i].style.padding = "0px";
			deletesDiv[i].style.marginBottom = "0px";
		}
	}
};

levels_delete();