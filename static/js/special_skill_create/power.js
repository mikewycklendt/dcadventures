function power_check() {
	const power_check = document.getElementById("power_check");
	const power_entry = document.getElementById("power-entry");
	
	if (power_check.checked == true) {
		power_entry.style.display = "grid";
		power_entry.style.padding = "1%";
		power_entry.style.maxHeight = power_entry.scrollHeight + "px";
		power_entry.style.padding = "1%";
	} else {
		power_entry.style.maxHeight = "0px";
		power_entry.style.padding = "0px";
	}
}

power_enter = 0;

function power_submit() {
	
	let sit_value = document.getElementById('power_sit').value;
	let power_field = document.getElementById('power_power');
	let power_value = power_field.options[power_field.selectedIndex].value; 
	
	if (sit_value != '' && power_value != '') {

		const pwr = document.createElement('div');
		pwr.className = 'power-table-power'
		pwr.innerHTML = power_value;

		const sit = document.createElement('div');
		sit.className = 'power-table-sit'
		sit.innerHTML = sit_value;
	
		const pwrDelete = document.createElement('div');
		pwrDelete.className = 'power-table-delete'
		const deleteBtn = document.createElement('button');
		deleteBtn.className = 'power-xbox';
		deleteBtn.innerHTML = '&cross;';
		deleteBtn.setAttribute('data-id', power_enter);
		pwrDelete.appendChild(deleteBtn);

		power_enter = power_enter + 1;
	
		const table = document.getElementById('power-table');

		table.style.display = "grid";
		table.style.padding = "1%";
		table.style.maxHeight = table.scrollHeight + "px";
		table.style.padding = "1%";

		table.appendChild(pwr);
		table.appendChild(sit);
		table.appendChild(pwrDelete);

		rows = [pwr.scrollHeight, sit.scrollHeight];
		let row_height = 0;

		for (i = 0; i < rows.length; i++) {
			if (rows[i] > row_height) {
				row_height = rows[i]
			}
		}

		pwr.style.maxHeight = pwr.scrollHeight + "px";
		sit.style.maxHeight = sit.scrollHeight + "px";
		pwrDelete.style.maxHeight = pwrDelete.scrollHeight + "px";
		table.style.maxHeight = table.scrollHeight + row_height + 15 + "px";

		power_delete()
	}
};

power_delete = function() {
	const deletes = document.querySelectorAll('.power-xbox');
	const pwrs = document.getElementsByClassName('power-table-power');
	const sits = document.getElementsByClassName('power-table-sit');
	const deletesDiv = document.getElementsByClassName('power-table-delete');
	for (let i = 0; i < deletes.length; i++) {
		const btn = deletes[i];
		btn.onclick = function(e) {
			console.log('click')
			pwrs[i].style.maxHeight = "0px";
			pwrs[i].style.padding = "0px";
			pwrs[i].style.marginBottom = "0px";
			sits[i].style.maxHeight = "0px";
			sits[i].style.padding = "0px";
			sits[i].style.marginBottom = "0px";
			deletesDiv[i].style.maxHeight = "0px";
			deletesDiv[i].style.padding = "0px";
			deletesDiv[i].style.marginBottom = "0px";
		}
	}
};

power_delete();