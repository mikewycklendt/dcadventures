function other_check() {
	const other_check = "other_check";
	const other_entry = "other-entry";
	const title = "other-title";

	entry_check(other_check, other_entry, title);
}

function other_submit() {
	let examples_value = document.getElementById('other_examples').value;
	let skill_field = document.getElementById('other_skill');
	let skill_value =  skill_field.options[skill_field.selectedIndex].value; 

	const bonus_id = document.getElementById('bonus_id').value;
	const error_line = 'other-err-line';
	const error_table = 'other-err';

	console.log(bonus_id)
	
	if (skill_value != '' && examples_value != '') {

		response = fetch('/skill/other_checks/create', {
			method: 'POST',
			body: JSON.stringify({
				'bonus_id': bonus_id,
				'skill_id': skill_value,
				'description': examples_value,
			}),
			headers: {
			  'Content-Type': 'application/json',
			}
		})
		.then(response => response.json())
		.then(jsonResponse => {
			console.log(jsonResponse)
			if (jsonResponse.success) {

				const skill = document.createElement('div');
				skill.className = 'other-table-skill'
				skill.innerHTML = jsonResponse.skill;

				const examples = document.createElement('div');
				examples.className = 'other-table-examples'
				examples.innerHTML = jsonResponse.description;
	
				const otherDelete = document.createElement('div');
				otherDelete.className = 'other-table-delete'
				const deleteBtn = document.createElement('button');
				deleteBtn.className = 'other-xbox';
				deleteBtn.setAttribute('data-id', jsonResponse.id);
				otherDelete.appendChild(deleteBtn);

				const table = document.getElementById('other-table');

				table.style.display = "grid";
				table.style.padding = "1%";
				table.style.maxHeight = table.scrollHeight + "px";
				table.style.padding = "1%";
	
				table.appendChild(skill);
				table.appendChild(examples);
				table.appendChild(otherDelete);

				rows = [skill.scrollHeight, examples.scrollHeight];
				let row_height = 0;

				for (i = 0; i < rows.length; i++) {
					if (rows[i] > row_height) {
						row_height = rows[i]
					}
				}
		
				skill.style.maxHeight = skill.scrollHeight + "px";
				examples.style.maxHeight = examples.scrollHeight + "px";
				otherDelete.style.maxHeight = otherDelete.scrollHeight + "px";
				table.style.maxHeight = table.scrollHeight + row_height + 15 + "px";

				other_delete()
	
				clear_errors(error_line, error_table);
			} else {
				back_error(error_line, error_table);
			}
		})
	} else {

		errors_delete = document.getElementsByClassName('other-err-line');

		for (i = 0; i < errors_delete.length; i++) {
			errors_delete[i].style.display = "none";
		}
		errors = document.getElementById('other-err')

		errors.style.display = "grid";
		errors.style.padding = "1%";
		
		console.log(examples_value)

		let errors_height = errors.scrollHeight + 20;

		if (skill_value == '') {
			const error = document.createElement('div');
			error.className = 'other-err-line'
			error.innerHTML = ' You must choose a skill';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (examples_value == '') {
			const error = document.createElement('div');
			error.className = 'other-err-line'
			error.innerHTML = ' You must provide example  situations';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		errors.style.maxHeight = errors_height + "px";
		errors.style.padding = "1%";
	}
};

other_delete = function() {
	const deletes = '.other-xbox';
	const divs = ['other-table-skill', 'other-table-examples', 'other-table-delete'];
	const route = '/skill/other_checks/delete/';
	
	delete_function(deletes, divs, route);
};

other_delete();