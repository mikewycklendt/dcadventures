function pre_check_check() {
	const pre_check_check = "pre_check_check";
	const pre_check_header_type = "pre-check-header-type";
	const title = "pre-check-title";
	const entry1 = "pre-check-entry-standard";
	const entry2 = "pre-check-entry-opposed";
	
	check_title_two(pre_check_check, title, pre_check_header_type, entry1, entry2);
}

function pre_check_entry() {
	pre_check_type = document.getElementById("pre_check_type")
	pre_check_type_value = pre_check_type.options[pre_check_type.selectedIndex].value;
	console.log(pre_check_type_value)
	const pre_check_entry_standard = "pre-check-entry-standard";
	const pre_check_entry_opposed = "pre-check-entry-opposed";

	if (pre_check_type_value == 'skill') {
		entry_hide(pre_check_entry_opposed);
		entry_show(pre_check_entry_standard);
	} else if (pre_check_type_value == 'opposed') {
		entry_hide(pre_check_entry_standard);
		entry_show(pre_check_entry_opposed);
	} else {
		entry_hide(pre_check_entry_opposed);
		entry_hide(pre_check_entry_standard);
	}
}

standard_enter = 0;

function pre_check_submit() {;
	
	let standard_circ_value = document.getElementById('pre_check_circ').value;
	let standard_when_field = document.getElementById('pre_check_when');
	let standard_skill_field = document.getElementById('pre_check_skill');
	let standard_when_value =  standard_when_field.options[standard_when_field.selectedIndex].value; 
	let standard_skill_value =  standard_skill_field.options[standard_skill_field.selectedIndex].value; 

	let opposed_circ_value = document.getElementById('pre_check_opposed_circ').value;
	let opposed_when_field = document.getElementById('pre_check_opposed_when');
	let opposed_skill_field = document.getElementById('pre_check_opposed_skill');
	let opposed_field = document.getElementById('pre_check_opposed');
	let opposed_when_value =  opposed_when_field.options[opposed_when_field.selectedIndex].value; 
	let opposed_skill_value =  opposed_skill_field.options[opposed_skill_field.selectedIndex].value;
	let opposed_value =  opposed_field.options[opposed_field.selectedIndex].value; 

	const pre_check_type = document.getElementById("pre_check_type")
	const pre_check_type_value = pre_check_type.options[pre_check_type.selectedIndex].value;

	let when;
	let check;
	let opposed_check;
	let description;

	if (pre_check_type_value == 'skill') {
		when = standard_when_value;
		check = standard_skill_value;
		opposed_check = '';
		description = standard_circ_value;
	} else if (pre_check_type_value == 'opposed') {
		when = opposed_when_value;
		check = opposed_skill_value;
		opposed_check = opposed_value;
		description = opposed_circ_value;
	}

	const bonus_id = document.getElementById('bonus_id').value;
	const error_line = 'pre-check-err-line';
	const error_table = 'pre-check-err';
	
	if ((pre_check_type_value != '') && ((pre_check_type_value == 'skill' && standard_skill_value != '' && standard_circ_value != '' && standard_when_value != '') || 
		(pre_check_type_value == 'opposed' && opposed_skill_value != '' && opposed_circ_value != '' && opposed_when_value != '' && opposed_value != ''))) {

		response = fetch('/skill/pre_check/create', {
			method: 'POST',
			body: JSON.stringify({
				'bonus_id': bonus_id,
				'check_type': pre_check_type_value,
				'when': when,
				'check': check,
				'opposed_check': opposed_check,
				'description': description,
			}),
			headers: {
			  'Content-Type': 'application/json',
			}
		})
		.then(response => response.json())
		.then(jsonResponse => {
			console.log(jsonResponse)
			if (jsonResponse.success) {

				let table_id;
				let table_data;
				let del;

				if (pre_check_type_value == 'opposed') {
					table_id = 'pre-check-table-opposed';
					table_data = [{'class': 'pre-check-table-opposed-when', 'value': jsonResponse.when},
									{'class': 'pre-check-table-opposed-skill', 'value': jsonResponse.check},
									{'class': 'pre-check-table-opposedby', 'value': jsonResponse.oppose_check},
									{'class': 'pre-check-table-opposed-circ', 'value': jsonResponse.description}];
					del = {'class': 'pre-check-table-opposed-delete', 'button': 'pre-check-opposed-xbox', 'value': jsonResponse.id};
				} else if (pre_check_type_value == 'skill') {
					table_id = 'pre-check-table-standard';
					table_data = [{'class': 'pre-check-table-when', 'value': jsonResponse.when},
									{'class': 'pre-check-table-skill', 'value': jsonResponse.check},
									{'class': 'pre-check-table-circ', 'value': jsonResponse.description}];
					del = {'class': 'pre-check-table-delete', 'button': 'pre-check-standard-xbox', 'value': jsonResponse.id};
				}

				const table = document.getElementById(table_id);

				table.style.display = "grid";
				table.style.padding = "1%";
				table.style.maxHeight = table.scrollHeight + "px";
				table.style.padding = "1%";
				
				let data;
				let rows = [];
				let divs = [];

				for (data of table_data) {
					let new_div = document.createElement('div');
					new_div.className = data.class;
					new_div.innerHTML = data.value;
					divs.push(new_div);
					rows.push(new_div.scrollHeight);
				};

				console.log(divs);
				
				const del_div = document.createElement('div');
				del_div.className = del.class;
				const deleteBtn = document.createElement('button');
				deleteBtn.className = del.button;
				deleteBtn.setAttribute('data-id', jsonResponse.id);
				del_div.appendChild(deleteBtn);
				
				let div;
				for (div of divs) {
					table.appendChild(div);
				};
				table.appendChild(del_div);
				for (div of divs) {
					div.style.maxHeight = div.scrollHeight + 'px';				
				};
				del_div.style.maxHeight = del_div.scrollHeight + 'px';

				let row_height = 0;

				for (i = 0; i < rows.length; i++) {
					if (rows[i] > row_height) {
						row_height = rows[i]
					}
				};

				table.style.maxHeight = table.scrollHeight + row_height + 15 + "px";

				pre_check_standard_delete();
				pre_check_opposed_delete();

				clear_errors(error_line, error_table)

			} else {

				back_error(error_line, error_table)
			}
		})

	} else {

		if (pre_check_type_value == 'skill') {
			pre_check_standard_errors()
		} else if (pre_check_type_value == 'opposed') {
			pre_check_opposed_errors()
		}
	}		
};

function pre_check_standard_errors() {
	errors_delete = document.getElementsByClassName('pre-check-err-line');
	
	for (i = 0; i < errors_delete.length; i++) {
		errors_delete[i].style.display = "none";
	}
	errors = document.getElementById('pre-check-err')

	errors.style.display = "grid";
	errors.style.padding = "1%";

	let errors_height = errors.scrollHeight + 20;

	if (standard_skill_value == '') {
		const error = document.createElement('div');
		error.className = 'pre-check-err-line'
		error.innerHTML = ' You must choose a skill value';

		errors.appendChild(error);

		error.style.maxHeight = error.scrollHeight + "px";
		errors_height = errors_height + error.scrollHeight; 
	}

	if (standard_circ_value == '') {
		const error = document.createElement('div');
		error.className = 'pre-check-err-line'
		error.innerHTML = ' You must enter a circumstance';

		errors.appendChild(error);

		error.style.maxHeight = error.scrollHeight + "px";
		errors_height = errors_height + error.scrollHeight; 
	}

	if (standard_when_value == '') {
		const error = document.createElement('div');
		error.className = 'pre-check-err-line'
		error.innerHTML = ' You must specify when this requirement occurs';

		errors.appendChild(error);

		error.style.maxHeight = error.scrollHeight + "px";
		errors_height = errors_height + error.scrollHeight; 
	}

	if (pre_check_type_value == '') {
		const error = document.createElement('div');
		error.className = 'pre-check-err-line'
		error.innerHTML = ' You must choose a check type';

		errors.appendChild(error);

		error.style.maxHeight = error.scrollHeight + "px";
		errors_height = errors_height + error.scrollHeight; 
	}

	errors.style.maxHeight = errors_height + "px";
	errors.style.padding = "1%";

}


pre_check_standard_delete = function() {
	const deletes = document.querySelectorAll('.pre-check-standard-xbox');
	const skills = document.getElementsByClassName('pre-check-table-skill');
	const circs = document.getElementsByClassName('pre-check-table-circ');
	const whens = document.getElementsByClassName('pre-check-table-when');
	const deletesDiv = document.getElementsByClassName('pre-check-table-delete');
	for (let i = 0; i < deletes.length; i++) {
		const btn = deletes[i];
		btn.onclick = function(e) {
			console.log('click')

			const delId = e.target.dataset['id'];
			fetch('/skill/pre_check/delete/' + delId, {
				method: 'DELETE'
			})
			.then(function() {
				skills[i].style.maxHeight = "0px";
				skills[i].style.padding = "0px";
				skills[i].style.marginBottom = "0px";
				circs[i].style.maxHeight = "0px";
				circs[i].style.padding = "0px";
				circs[i].style.marginBottom = "0px";
				whens[i].style.maxHeight = "0px";
				whens[i].style.padding = "0px";
				whens[i].style.marginBottom = "0px";
				deletesDiv[i].style.maxHeight = "0px";
				deletesDiv[i].style.padding = "0px";
				deletesDiv[i].style.marginBottom = "0px";
			})
		}
	}
};

pre_check_standard_delete();

opposed_enter = 0;

function pre_check_opposed_submit() {
	
	let opposed_circ_value = document.getElementById('pre_check_opposed_circ').value;
	let opposed_when_field = document.getElementById('pre_check_opposed_when');
	let opposed_skill_field = document.getElementById('pre_check_opposed_skill');
	let opposed_field = document.getElementById('pre_check_opposed');
	let opposed_when_value =  opposed_when_field.options[opposed_when_field.selectedIndex].value; 
	let opposed_skill_value =  opposed_skill_field.options[opposed_skill_field.selectedIndex].value;
	let opposed_value =  opposed_field.options[opposed_field.selectedIndex].value; 

	pre_check_type = document.getElementById("pre_check_type")
	pre_check_type_value = pre_check_type.options[pre_check_type.selectedIndex].value;

	const bonus_id = document.getElementById('bonus_id').value;

	console.log(opposed_circ_value);
	console.log(opposed_when_value);
	console.log(opposed_skill_value);
	console.log(opposed_value);
	
	if (opposed_skill_value != '' && opposed_circ_value != '' && opposed_when_value != '' && opposed_value != '' && pre_check_type_value != '') {

		response = fetch('/skill/pre_check/create', {
			method: 'POST',
			body: JSON.stringify({
				'bonus_id': bonus_id,
				'check_type': pre_check_type_value,
				'when': opposed_when_value,
				'check': opposed_skill_value,
				'opposed_check': opposed_value,
				'description': opposed_circ_value,
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
				skill.className = 'pre-check-table-opposed-skill'
				skill.innerHTML = jsonResponse.check;

				const when = document.createElement('div');
				when.className = 'pre-check-table-opposed-when'
				when.innerHTML = jsonResponse.when;
		
				const opposed = document.createElement('div');
				opposed.className = 'pre-check-table-opposedby'
				opposed.innerHTML = jsonResponse.oppose_check;

				const circ = document.createElement('div');
				circ.className = 'pre-check-table-opposed-circ'
				circ.innerHTML = jsonResponse.description;
	
				const opposedDelete = document.createElement('div');
				opposedDelete.className = 'pre-check-table-opposed-delete'
				const deleteBtn = document.createElement('button');
				deleteBtn.className = 'pre-check-opposed-xbox';
				deleteBtn.setAttribute('data-id', jsonResponse.id);
				opposedDelete.appendChild(deleteBtn);

				const opposed_table = document.getElementById('pre-check-table-opposed');

				opposed_table.style.display = "grid";
				opposed_table.style.padding = "1%";
				opposed_table.style.maxHeight = opposed_table.scrollHeight + "px";
				opposed_table.style.padding = "1%";

				opposed_table.appendChild(when);
				opposed_table.appendChild(skill);
				opposed_table.appendChild(opposed);
				opposed_table.appendChild(circ);
				opposed_table.appendChild(opposedDelete);

				rows = [when.scrollHeight, skill.scrollHeight, opposed.scrollHeight, circ.scrollHeight];
				let row_height = 0;

				for (i = 0; i < rows.length; i++) {
					if (rows[i] > row_height) {
						row_height = rows[i]
					}
				}
		
				skill.style.maxHeight = skill.scrollHeight + "px";
				when.style.maxHeight = when.scrollHeight + "px";
				circ.style.maxHeight = circ.scrollHeight + "px";
				opposed.style.maxHeight = opposed.scrollHeight + "px";
				opposedDelete.style.maxHeight = opposedDelete.scrollHeight + "px";
				opposed_table.style.maxHeight = opposed_table.scrollHeight + row_height + 15 + "px";

				pre_check_opposed_delete()

				errors_delete = document.getElementsByClassName('pre-check-err-line');

				if (typeof errors_delete[0] === "undefined") {
					console.log('no errors defined')
				} else {
					for (i = 0; i < errors_delete.length; i++) {
						errors_delete[i].style.maxHeight = "0px";
						errors_delete[i].style.padding = "0px";
						errors_delete[i].style.marginBottom = "0px";
					}

					errors = document.getElementById('pre-check-err')

					errors.style.display = "none";
					errors.style.padding = "0px";
					errors.style.maxHeight = "0px";
				}
			} else {
				const errors = document.getElementById('pre-check-err');

				errors.style.display = "grid";
				errors.style.padding = "1%";

				const error = document.createElement('div');
				error.className = 'pre-check-err-line';
				error.innerHTML = jsonResponse.error;
	
				errors.appendChild(error);
	
				error.style.maxHeight = error.scrollHeight + "px";
	
				errors.style.maxHeight = error.scrollHeight + errors.scrollHeight + 15 + "px";
				errors.style.padding = "1%";
			}
		})
	} else {

	}
};

function pre_check_opposed_errors() {
	errors_delete = document.getElementsByClassName('pre-check-err-line');

	for (i = 0; i < errors_delete.length; i++) {
		errors_delete[i].style.display = "none";
	}
	errors = document.getElementById('pre-check-err')

	errors.style.display = "grid";
	errors.style.padding = "1%";

	let errors_height = errors.scrollHeight + 20;

	if (opposed_skill_value == '') {
		const error = document.createElement('div');
		error.className = 'pre-check-err-line'
		error.innerHTML = ' You must choose a skill valure';

		errors.appendChild(error);

		error.style.maxHeight = error.scrollHeight + "px";
		errors_height = errors_height + error.scrollHeight; 
	}

	if (opposed_circ_value != '') {
		const error = document.createElement('div');
		error.className = 'pre-check-err-line'
		error.innerHTML = ' You must enter a circumstance';

		errors.appendChild(error);

		error.style.maxHeight = error.scrollHeight + "px";
		errors_height = errors_height + error.scrollHeight; 
	}

	if (opposed_when_value == '') {
		const error = document.createElement('div');
		error.className = 'pre-check-err-line'
		error.innerHTML = ' You must specify when this requirement occurs';

		errors.appendChild(error);

		error.style.maxHeight = error.scrollHeight + "px";
		errors_height = errors_height + error.scrollHeight; 
	}

	if (opposed_value == '') {
		const error = document.createElement('div');
		error.className = 'pre-check-err-line'
		error.innerHTML = ' You must specify the opposed value';

		errors.appendChild(error);

		error.style.maxHeight = error.scrollHeight + "px";
		errors_height = errors_height + error.scrollHeight; 
	}

	if (pre_check_type_value == '') {
		const error = document.createElement('div');
		error.className = 'pre-check-err-line'
		error.innerHTML = ' You must CHOOSE A CHECK TYPE';

		errors.appendChild(error);

		error.style.maxHeight = error.scrollHeight + "px";
		errors_height = errors_height + error.scrollHeight; 
	}

	errors.style.maxHeight = errors_height + "px";
	errors.style.padding = "1%";
}

pre_check_opposed_delete = function() {
	const deletes = document.querySelectorAll('.pre-check-opposed-xbox');
	const skills = document.getElementsByClassName('pre-check-table-opposed-skill');
	const circs = document.getElementsByClassName('pre-check-table-opposed-circ');
	const whens = document.getElementsByClassName('pre-check-table-opposed-when');
	const opposeds = document.getElementsByClassName('pre-check-table-opposedby');
	const deletesDiv = document.getElementsByClassName('pre-check-table-opposed-delete');
	for (let i = 0; i < deletes.length; i++) {
		const btn = deletes[i];
		btn.onclick = function(e) {
			console.log('click')

			const delId = e.target.dataset['id'];
			fetch('/skill/pre_check/delete/' + delId, {
				method: 'DELETE'
			})
			.then(function() {
				skills[i].style.maxHeight = "0px";
				skills[i].style.padding = "0px";
				skills[i].style.marginBottom = "0px";
				circs[i].style.maxHeight = "0px";
				circs[i].style.padding = "0px";
				circs[i].style.marginBottom = "0px";
				whens[i].style.maxHeight = "0px";
				whens[i].style.padding = "0px";
				whens[i].style.marginBottom = "0px";
				opposeds[i].style.maxHeight = "0px";
				opposeds[i].style.padding = "0px";
				opposeds[i].style.marginBottom = "0px";
				deletesDiv[i].style.maxHeight = "0px";
				deletesDiv[i].style.padding = "0px";
				deletesDiv[i].style.marginBottom = "0px";
				})
		}
	}
};

pre_check_opposed_delete();