function levels_check() {
	const levels_check = document.getElementById("levels_check");
	const levels_base_form = document.getElementById("levels-base-form");
	const title = document.getElementById("levels-title");

	if (levels_check.checked == true) {
		levels_base_form.style.opacity = "100%";
		title.style.color = "#af0101";
		title.style.fontSize = "207%";
		setTimeout(function(){title.style.fontSize = "200%"}, 75);
	} else {
		levels_base_form.style.opacity = "0%";
		title.style.color = "#245681";
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
				deleteBtn.innerHTML = '&cross;';
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
		
				errors_delete = document.getElementsByClassName('levels-err-line');

				if (typeof errors_delete[0] === "undefined") {
					console.log('no errors defined')
				} else {
					for (i = 0; i < errors_delete.length; i++) {
						errors_delete[i].style.maxHeight = "0px";
						errors_delete[i].style.padding = "0px";
						errors_delete[i].style.marginBottom = "0px";
					}

					errors = document.getElementById('levels-err')

					errors.style.display = "none";
					errors.style.padding = "0px";
					errors.style.maxHeight = "0px";
				}
			} else {
				const errors = document.getElementById('levels-err');

				errors.style.display = "grid";
				errors.style.padding = "1%";

				const error = document.createElement('div');
				error.className = 'levels-err-line';
				error.innerHTML = jsonResponse.error;

				errors.appendChild(error);

				error.style.maxHeight = error.scrollHeight + "px";

				errors.style.maxHeight = error.scrollHeight + errors.scrollHeight + 15 + "px";
				errors.style.padding = "1%";
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
	const deletes = document.querySelectorAll('.levels-xbox');
	const dcs = document.getElementsByClassName('levels-table-dc');
	const lvls = document.getElementsByClassName('levels-table-level');
	const efcts = document.getElementsByClassName('levels-table-effect');
	const deletesDiv = document.getElementsByClassName('levels-table-delete');
	for (let i = 0; i < deletes.length; i++) {
		const btn = deletes[i];
		btn.onclick = function(e) {
			console.log('click')

			const delId = e.target.dataset['id'];
			fetch('/skill/level/delete/' + delId, {
				method: 'DELETE'
			})
			.then(function() {

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
			})
		}
	}
};

levels_delete();