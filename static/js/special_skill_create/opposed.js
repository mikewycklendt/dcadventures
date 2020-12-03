function opposed_by_check() {
	const opposed_by_check = "opposed_by_check";
	const opposed_by_base_form = "opposed-by-base-form";
	const title = "opposed-by-title";
	const entry = 'opposed-by-entry';
	
	check_title(opposed_by_check, title, opposed_by_base_form, entry);
}

function opposed_by_by() {
	const opposed_by_by = "opposed_by_by";
	const opposed_by_entry = "opposed-by-entry";

	base(opposed_by_by, opposed_by_entry);
}

opposed_enter = 0;

function opposed_by_submit() {
	
	let sit_value = document.getElementById('opposed_by_sit').value;
	let opposed_field = document.getElementById('opposed_by');
	let mod_field = document.getElementById('opposed_by_mod');
	let opposed_by_field = document.getElementById('opposed-by-base-form');
	let opposed_value =  opposed_field.options[opposed_field.selectedIndex].value;
	let mod_value =  mod_field.options[mod_field.selectedIndex].value; 

	const opposed_by_by = document.getElementById("opposed_by_by")
	let opposed_by_by_value = opposed_by_by.options[opposed_by_by.selectedIndex].value;

	console.log(sit_value)

	const bonus_id = document.getElementById('bonus_id').value;
	const error_line = 'opposed-by-err-line';
	const error_table = 'opposed-by-err';

	if (opposed_value != '' && mod_value != '' && sit_value != '' && opposed_by_by_value != '') {

		response = fetch('/skill/opposed/create', {
			method: 'POST',
			body: JSON.stringify({
				'bonus_id': bonus_id,
				'priority': opposed_by_by_value,
				'opposed': opposed_value,
				'mod': mod_value,
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

				const opp = document.createElement('div');
				opp.className = 'opposed-by-table-oppose'
				opp.innerHTML = jsonResponse.opposed;

				const mod = document.createElement('div');
				mod.className = 'opposed-by-table-mod'
				mod.innerHTML = jsonResponse.mod;

				const sit = document.createElement('div');
				sit.className = 'opposed-by-table-sit';
				sit.innerHTML = jsonResponse.description;

				const oppDelete = document.createElement('div');
				oppDelete.className = 'opposed-by-table-delete'
				const deleteBtn = document.createElement('button');
				deleteBtn.className = 'opposed-by-xbox';
				deleteBtn.setAttribute('data-id', jsonResponse.id);
				oppDelete.appendChild(deleteBtn);

				const table = document.getElementById('opposed-by-table');

				table.style.display = "grid";
				table.style.padding = "1%";
				table.style.maxHeight = table.scrollHeight + "px";
				table.style.padding = "1%";

				table.appendChild(opp);
				table.appendChild(mod);
				table.appendChild(sit);
				table.appendChild(oppDelete);

				rows = [opp.scrollHeight, mod.scrollHeight, sit.scrollHeight];
				let row_height = 0;

				for (i = 0; i < rows.length; i++) {
					if (rows[i] > row_height) {
						row_height = rows[i]
					}
				}

		
				opp.style.maxHeight = opp.scrollHeight + "px";
				mod.style.maxHeight = mod.scrollHeight + "px";
				sit.style.maxHeight = sit.scrollHeight + "px";
				oppDelete.style.maxHeight = oppDelete.scrollHeight + "px";
				table.style.maxHeight = table.scrollHeight + row_height + 15 + "px";

				opposed_by_field.style.opacity = '0%';

				opposed_delete()
	
				clear_errors(error_line, error_table);
			} else {
				back_error(error_line, error_table);
			}
		})

	} else {

		errors_delete = document.getElementsByClassName('opposed-by-err-line');

		for (i = 0; i < errors_delete.length; i++) {
			errors_delete[i].style.display = "none";
		}
		errors = document.getElementById('opposed-by-err')

		errors.style.display = "grid";
		errors.style.padding = "1%";

		let errors_height = errors.scrollHeight + 20;

		if (opposed_value == '') {
			const error = document.createElement('div');
			error.className = 'opposed-by-err-line'
			error.innerHTML = ' You must specify what this skill is opposed by';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (mod_value == '') {
			const error = document.createElement('div');
			error.className = 'opposed-by-err-line'
			error.innerHTML = ' You must enter a modifier';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (sit_value == '') {
			const error = document.createElement('div');
			error.className = 'opposed-by-err-line'
			error.innerHTML = ' You must specify the situation in which thios skill is opposed';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (opposed_by_by_value == '') {
			const error = document.createElement('div');
			error.className = 'opposed-by-err-line'
			error.innerHTML = ' You must choose the priority by which the opposed skill is determined';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		errors.style.maxHeight = errors_height + "px";
		errors.style.padding = "1%";
	}
};

opposed_delete = function() {
	const deletes = '.opposed-by-xbox';
	const divs = ['opposed-by-table-oppose', 'opposed-by-table-mod', 'opposed-by-table-sit', 'opposed-by-table-delete'];
	const route = '/skill/opposed/delete/';

	delete_function(deletes, divs, route);
};

opposed_delete();