function power_check() {
	const power_check = "power_check";
	const power_entry = "power-entry";
	const title = "power-title";
	
	entry_check(power_check, power_entry, title);
}

power_enter = 0;

function power_submit() {
	
	let sit_value = document.getElementById('power_sit').value;
	let power_field = document.getElementById('power_power');
	let power_value = power_field.options[power_field.selectedIndex].value; 

	const bonus_id = document.getElementById('bonus_id').value;
	const error_line = 'power-err-line';
	const error_table = 'power-err';

	if (sit_value != '' && power_value != '') {

		response = fetch('/skill/power/create', {
			method: 'POST',
			body: JSON.stringify({
				'bonus_id': bonus_id,
				'power': power_value,
				'description': sit_value
			}),
			headers: {
			  'Content-Type': 'application/json',
			}
		})
		.then(response => response.json())
		.then(jsonResponse => {
			console.log(jsonResponse)
			if (jsonResponse.success) {

				const pwr = document.createElement('div');
				pwr.className = 'power-table-power'
				pwr.innerHTML = jsonResponse.power;

				const sit = document.createElement('div');
				sit.className = 'power-table-sit'
				sit.innerHTML = jsonResponse.description;
	
				const pwrDelete = document.createElement('div');
				pwrDelete.className = 'power-table-delete'
				const deleteBtn = document.createElement('button');
				deleteBtn.className = 'power-xbox';
				deleteBtn.setAttribute('data-id', jsonResponse.id);
				pwrDelete.appendChild(deleteBtn);

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

				clear_errors(error_line, error_table);
			} else {
				back_error(error_line, error_table);
			}
		})

	} else {

		errors_delete = document.getElementsByClassName('power-err-line');

		for (i = 0; i < errors_delete.length; i++) {
			errors_delete[i].style.display = "none";
		}
		errors = document.getElementById('power-err')

		errors.style.display = "grid";
		errors.style.padding = "1%";

		let errors_height = errors.scrollHeight + 20;

		if (sit_value == '') {
			const error = document.createElement('div');
			error.className = 'power-err-line'
			error.innerHTML = ' You must enter a situation';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (power_value== '') {
			const error = document.createElement('div');
			error.className = 'power-err-line'
			error.innerHTML = ' You must enter a power';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		errors.style.maxHeight = errors_height + "px";
		errors.style.padding = "1%";
	}
};

power_delete = function() {
	const deletes = '.power-xbox';
	const divs = ['power-table-power', 'power-table-sit', 'power-table-delete'];
	const route = '/skill/power/delete/';

	delete_function(deletes, divs, route);
};

power_delete();