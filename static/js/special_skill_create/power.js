function power_check() {
	const power_check = document.getElementById("power_check");
	const power_entry = document.getElementById("power-entry");
	const title = document.getElementById("power-title");
	
	if (power_check.checked == true) {
		power_entry.style.display = "grid";
		power_entry.style.padding = "1%";
		power_entry.style.maxHeight = power_entry.scrollHeight + "px";
		power_entry.style.padding = "1%";
		title.style.color = "#af0101";
		title.style.fontSize = "207%";
		setTimeout(function(){title.style.fontSize = "200%"}, 75);
	} else {
		power_entry.style.maxHeight = "0px";
		power_entry.style.padding = "0px";
		title.style.color = "#245681";
	}
}

power_enter = 0;

function power_submit() {
	
	let sit_value = document.getElementById('power_sit').value;
	let power_field = document.getElementById('power_power');
	let power_value = power_field.options[power_field.selectedIndex].value; 

	const bonus_id = document.getElementById('bonus_id').value;
	
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
				deleteBtn.innerHTML = '&cross;';
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

				errors_delete = document.getElementsByClassName('power-err-line');

				if (typeof errors_delete[0] === "undefined") {
					console.log('no errors defined')
				} else {
					for (i = 0; i < errors_delete.length; i++) {
						errors_delete[i].style.maxHeight = "0px";
						errors_delete[i].style.padding = "0px";
						errors_delete[i].style.marginBottom = "0px";
					}

					errors = document.getElementById('power-err')

					errors.style.display = "none";
					errors.style.padding = "0px";
					errors.style.maxHeight = "0px";
				}
			} else {
				const errors = document.getElementById('power-err');

				errors.style.display = "grid";
				errors.style.padding = "1%";

				const error = document.createElement('div');
				error.className = 'power-err-line';
				error.innerHTML = jsonResponse.error;

				errors.appendChild(error);

				error.style.maxHeight = error.scrollHeight + "px";

				errors.style.maxHeight = error.scrollHeight + errors.scrollHeight + 15 + "px";
				errors.style.padding = "1%";
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