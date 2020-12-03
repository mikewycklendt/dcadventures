function resist_check() {
	const resist_check = "resist_check";
	const resist_target = "resist-target";
	const title = "resist-title";
	const entry = 'resist-entry';

	check_title(resist_check, title, resist_target, entry);
}

function resist_base() {
	const resist_target = "resist_target";
	const resist_entry = "resist-entry";

	base(resist_target, resist_entry);
}

resistance_enter = 0;

function resistance_submit() {
	
	const resist_target = document.getElementById("resist_target");
	resisttarget =  deg_mod_target.options[resist_target.selectedIndex].value;

	let des_value = document.getElementById('resist_desc').value;
	let mod_field = document.getElementById('resist_modifier');
	let mod_value = mod_field.options[mod_field.selectedIndex].value; 

	console.log

	const bonus_id = document.getElementById('bonus_id').value;
	const error_line = 'resist-err-line';
	const error_table = 'resist-err';

	if (resisttarget != '' && mod_value != '' && des_value != '') {

		response = fetch('/skill/resistance/create', {
			method: 'POST',
			body: JSON.stringify({
				'bonus_id': bonus_id,
				'target': resisttarget,
				'mod': mod_value,
				'description': des_value
			}),
			headers: {
			  'Content-Type': 'application/json',
			}
		})
		.then(response => response.json())
		.then(jsonResponse => {
			console.log(jsonResponse)
			if (jsonResponse.success) {

				const mod = document.createElement('div');
				mod.className = 'resist-table-mod'
				mod.innerHTML = jsonResponse.mod;

				const des = document.createElement('div');
				des.className = 'resist-table-desc'
				des.innerHTML = jsonResponse.description;
	
				const resistDelete = document.createElement('div');
				resistDelete.className = 'resist-table-delete'
				const deleteBtn = document.createElement('button');
				deleteBtn.className = 'resist-xbox';
				deleteBtn.setAttribute('data-id', jsonResponse.id);
				resistDelete.appendChild(deleteBtn);

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
	
				clear_errors(error_line, error_table);
			
			} else {
				back_error(error_line, error_table);
			}
		})

	} else {

		errors_delete = document.getElementsByClassName('resist-err-line');

		for (i = 0; i < errors_delete.length; i++) {
			errors_delete[i].style.display = "none";
		}
		errors = document.getElementById('resist-err')

		errors.style.display = "grid";
		errors.style.padding = "1%";
		
		let errors_height = errors.scrollHeight + 20;

		if (resisttarget == '') {
			const error = document.createElement('div');
			error.className = 'resist-err-line'
			error.innerHTML = ' You must choose a target';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (mod_value == '') {
			const error = document.createElement('div');
			error.className = 'resist-err-line'
			error.innerHTML = ' You must specify a modifier';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (des_value == '') {
			const error = document.createElement('div');
			error.className = 'resist-err-line'
			error.innerHTML = ' You must enter a description';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		errors.style.maxHeight = errors_height + "px";
		errors.style.padding = "1%";
	}
};

resistance_delete = function() {
	const deletes = '.resist-xbox';
	const divs = ['resist-table-mod', 'resist-table-desc', 'resist-table-delete'];
	const route = '/skill/resistance/delete/';
	
	delete_function(deletes, divs, route);
};

resistance_delete();