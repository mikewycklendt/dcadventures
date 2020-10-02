function resist_check() {
	const resist_check = document.getElementById("resist_check");
	const resist_target = document.getElementById("resist-target");
	
	if (resist_check.checked == true) {
		resist_target.style.opacity = "100%";
	} else {
		resist_target.style.opacity = "0%";
	}
}

function resist_base() {
	const resist_target = document.getElementById("resist_target");
	resisttarget =  deg_mod_target.options[resist_target.selectedIndex].value;
	console.log(resisttarget);
	const resist_entry = document.getElementById("resist-entry");

	if (resisttarget != '') {
		resist_entry.style.display = "grid";
		resist_entry.style.padding = "1%";
		resist_entry.style.maxHeight = resist_entry.scrollHeight + "px";
		resist_entry.style.padding = "1%";
	} else {
		resist_entry.style.maxHeight = "0px";
		resist_entry.style.padding = "0px";
	}
}

resistance_enter = 0;

function resistance_submit() {
	
	const resist_target = document.getElementById("resist_target");
	resisttarget =  deg_mod_target.options[resist_target.selectedIndex].value;

	let des_value = document.getElementById('resist_desc').value;
	let mod_field = document.getElementById('resist_modifier');
	let mod_value = mod_field.options[mod_field.selectedIndex].value; 

	console.log
	
	if (resisttarget != '' && mod_value != '' && des_value != '') {

		const mod = document.createElement('div');
		mod.className = 'resist-table-mod'
		mod.innerHTML = mod_value;

		const des = document.createElement('div');
		des.className = 'resist-table-desc'
		des.innerHTML = des_value;
	
		const resistDelete = document.createElement('div');
		resistDelete.className = 'resist-table-delete'
		const deleteBtn = document.createElement('button');
		deleteBtn.className = 'resist-xbox';
		deleteBtn.innerHTML = '&cross;';
		deleteBtn.setAttribute('data-id', resistance_enter);
		resistDelete.appendChild(deleteBtn);

		resistance_enter = resistance_enter + 1;

		const table = document.getElementById('resist-table');
	
		table.style.display = "grid";
		table.style.padding = "1%";
		table.style.maxHeight = table.scrollHeight + "px";
		table.style.padding = "1%";
	
		table.appendChild(mod);
		table.appendChild(des);
		table.appendChild(resistDelete);

		rows = [mod.scrollHeight, des.scrollHeight];
		let row_height = 0;

		for (i = 0; i < rows.length; i++) {
			if (rows[i] > row_height) {
				row_height = rows[i]
			}
		}

		
		mod.style.maxHeight = mod.scrollHeight + "px";
		des.style.maxHeight = des.scrollHeight + "px";
		resistDelete.style.maxHeight = resistDelete.scrollHeight + "px";
		table.style.maxHeight = table.scrollHeight + row_height + 15 + "px";

		resistance_delete()
	
		errors_delete = document.getElementsByClassName('resist-err-line');

		if (typeof errors_delete === "undefined") {
			console.log('no errors defined')
		} else {
			for (i = 0; i < errors_delete.length; i++) {
				errors_delete[i].style.maxHeight = "0px";
				errors_delete[i].style.padding = "0px";
				errors_delete[i].style.marginBottom = "0px";
			}

			errors = document.getElementById('rounds-err')

			errors.style.display = "none";
			errors.style.padding = "0px";
			errors.style.maxHeight = "0px";
		}

	} else {

		errors_delete = document.getElementsByClassName('resist-err-line');

		for (i = 0; i < errors_delete.length; i++) {
			errors_delete[i].style.display = "none";
		}
		errors = document.getElementById('resist-err')

		errors.style.display = "grid";
		errors.style.padding = "1%";
		errors.style.maxHeight = errors.scrollHeight + "px";
		errors.style.padding = "1%";

		if (resisttarget == '') {
			const error = document.createElement('div');
			error.className = 'resist-err-line'
			error.innerHTML = ' You must choose a target';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
		}

		if (mod_value == '') {
			const error = document.createElement('div');
			error.className = 'resist-err-line'
			error.innerHTML = ' You must specify a modifier';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
		}

		if (des_value == '') {
			const error = document.createElement('div');
			error.className = 'resist-err-line'
			error.innerHTML = ' You must enter a description';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
		}
	}
};

resistance_delete = function() {
	const deletes = document.querySelectorAll('.resist-xbox');
	const mods = document.getElementsByClassName('resist-table-mod');
	const dess = document.getElementsByClassName('resist-table-desc');
	const deletesDiv = document.getElementsByClassName('resist-table-delete');
	for (let i = 0; i < deletes.length; i++) {
		const btn = deletes[i];
		btn.onclick = function(e) {
			console.log('click')
			mods[i].style.maxHeight = "0px";
			mods[i].style.padding = "0px";
			mods[i].style.marginBottom = "0px";
			dess[i].style.maxHeight = "0px";
			dess[i].style.padding = "0px";
			dess[i].style.marginBottom = "0px";
			deletesDiv[i].style.maxHeight = "0px";
			deletesDiv[i].style.padding = "0px";
			deletesDiv[i].style.marginBottom = "0px";
		}
	}
};

resistance_delete();