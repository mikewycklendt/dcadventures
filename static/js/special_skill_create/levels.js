function levels_check() {
	const levels_check = "levels_check";
	const levels_base_form = "levels-base-form";
	const title = "levels-title";
	const entry = 'levels-entry';

	check_title(levels_check, title, levels_base_form, entry);
}

function levels_base() {
	const level_type = "level_type";
	const level_dc_set = "levels_dc_set";
	const level_target = "levels_target";
	const levels_entry = "levels-entry";

	base_three(level_dc_set, level_target, level_type, levels_entry);
}


let bonus_level = true;

function levels_submit() {
	let trgt_field = document.getElementById('levels_target');
	let trgt_value = trgt_field.options[trgt_field.selectedIndex].value;
	let type_value = document.getElementById('level_type').value;
	let level_type_field = document.getElementById('level-type');

	const level_type = document.getElementById('levels-table-type');

	level_type.innerHTML = type_value;
	level_type_field.style.opacity = "0%";

	let lvl_value = document.getElementById('level').value;
	let efct_value = document.getElementById('level_effect').value;
	let dc_field = document.getElementById('levels_dc_set');
	let dc_value =  dc_field.options[dc_field.selectedIndex].value;
	
	const bonus_id = document.getElementById('bonus_id').value;
	const error_line = 'levels-err-line';
	const error_table = 'levels-err';

	console.log(bonus_level)
	
	if (type_value != '' && lvl_value != '' && efct_value != '' && dc_value != '' && trgt_value != '') {

		response = fetch('/skill/level/create', {
			method: 'POST',
			body: JSON.stringify({
				'bonus_id': bonus_id,
				'bonus_level': bonus_level,
				'type': type_value,
				'target': trgt_value,
				'degree': dc_value,
				'keyword': lvl_value,
				'description': efct_value
			}),
			headers: {
			  'Content-Type': 'application/json',
			}
		})
		.then(response => response.json())
		.then(jsonResponse => {
			console.log(jsonResponse)
			if (jsonResponse.success) {

				bonus_level = false;

				const dc = document.createElement('div');
				dc.className = 'levels-table-dc'
				dc.innerHTML = jsonResponse.degree;

				const lvl = document.createElement('div');
				lvl.className = 'levels-table-level'
				lvl.innerHTML = jsonResponse.keyword;

				const efct = document.createElement('div');
				efct.className = 'levels-table-effect'
				efct.innerHTML = jsonResponse.description;

				const lvlDelete = document.createElement('div');
				lvlDelete.className = 'levels-table-delete'
				const deleteBtn = document.createElement('button');
				deleteBtn.className = 'levels-xbox';
				deleteBtn.setAttribute('data-id', jsonResponse.id);
				lvlDelete.appendChild(deleteBtn);
	
				const table = document.getElementById('levels-table');

				table.style.display = "grid";
				table.style.padding = "1%";
				table.style.maxHeight = table.scrollHeight + "px";
				table.style.padding = "1%";
			
				table.appendChild(dc);
				table.appendChild(lvl);
				table.appendChild(efct);
				table.appendChild(lvlDelete);

				rows = [dc.scrollHeight, lvl.scrollHeight, efct.scrollHeight];
				let row_height = 0;

				for (i = 0; i < rows.length; i++) {
					if (rows[i] > row_height) {
						row_height = rows[i]
					}
				}
		
				dc.style.maxHeight = dc.scrollHeight + "px";
				lvl.style.maxHeight = lvl.scrollHeight + "px";
				efct.style.maxHeight = efct.scrollHeight + "px";
				lvlDelete.style.maxHeight = lvlDelete.scrollHeight + "px";
				table.style.maxHeight = table.scrollHeight + row_height + 15 + "px";

				levels_delete()
		
				clear_errors(error_line, error_table);
			} else {
				back_error(error_line, error_table);
			}
		})


	} else {

		errors_delete = document.getElementsByClassName('levels-err-line');

		for (i = 0; i < errors_delete.length; i++) {
			errors_delete[i].style.display = "none";
		}
		errors = document.getElementById('levels-err')

		errors.style.display = "grid";
		errors.style.padding = "1%";

		let errors_height = errors.scrollHeight + 20;

		if (type_value == '') {
			const error = document.createElement('div');
			error.className = 'levels-err-line'
			error.innerHTML = ' You must enter a level type';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (lvl_value == '') {
			const error = document.createElement('div');
			error.className = 'levels-err-line'
			error.innerHTML = ' You must enter a level value';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (efct_value == '') {
			const error = document.createElement('div');
			error.className = 'levels-err-line'
			error.innerHTML = ' You must enter an effect';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (dc_value == '') {
			const error = document.createElement('div');
			error.className = 'levels-err-line'
			error.innerHTML = ' You must enter a difficulty class';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (trgt_value == '') {
			const error = document.createElement('div');
			error.className = 'levels-err-line'
			error.innerHTML = ' You must enter a target';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		errors.style.maxHeight = errors_height + "px";
		errors.style.padding = "1%";
	}
};

levels_delete = function() {
	const deletes = '.levels-xbox';
	const divs = ['levels-table-dc', 'levels-table-level', 'levels-table-effect', 'levels-table-delete'];
	const route = '/skill/level/delete/';

	delete_function(deletes, divs, route);
};

levels_delete();