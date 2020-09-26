function opposed_by_check() {
	const opposed_by_check = document.getElementById("opposed_by_check");
	const opposed_by_base_form = document.getElementById("opposed-by-base-form");
	
	if (opposed_by_check.checked == true) {
		opposed_by_base_form.style.opacity = "100%";
	} else {
		opposed_by_base_form.style.opacity = "0%";
	}
}

function opposed_by_by() {
	const opposed_by_by = document.getElementById("opposed_by_by")
	let opposed_by_by_value = opposed_by_by.options[opposed_by_by.selectedIndex].value;
	console.log(opposed_by_by_value)
	const opposed_by_entry = document.getElementById("opposed-by-entry")

	if (opposed_by_by_value != '') {
		opposed_by_entry.style.display = "grid";
		opposed_by_entry.style.padding = "1%";
		opposed_by_entry.style.maxHeight = opposed_by_entry.scrollHeight + "px";
		opposed_by_entry.style.padding = "1%";
	} else {
		opposed_by_entry.style.maxHeight = "0px";
		opposed_by_entry.style.padding = "0px";
	}
}

opposed_enter = 0;

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