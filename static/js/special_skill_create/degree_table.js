function degree_check() {
	const degree_check = "degree_check";
	const degree_base_form = "degree-base-form";
	const title = "degree-title";
	const entry = 'degree-entry';

	check_title_small(degree_check, title, degree_base_form, entry);
}

function degree_base() {
	const degree_type = "degree_type";
	const degree_target = "degree_target";
	const degree_entry = "degree-entry";

	base_text(degree_target, degree_type, degree_entry);
}

degree_type_check = true;

function degree_submit() {
	
	const type = document.getElementById('degree-type');

	let key_value = document.getElementById('degree_keyword').value;
	let desc_value = document.getElementById('degree_desc').value;
	let val_field = document.getElementById('degree_value');
	let val_value =  val_field.options[val_field.selectedIndex].value; 

	const degree_type = document.getElementById("degree_type");
	const degree_target = document.getElementById("degree_target");
	degrees_target =  degree_target.options[degree_target.selectedIndex].value;
	degrees_type = degree_type.value;

	type.style.opacity = "0%"

	const bonus_id = document.getElementById('bonus_id').value;

	if (degrees_type != '' && degrees_target != '' && key_value != '' && desc_value != '' && val_value != '') {

		response = fetch('/skill/degree_key/create', {
			method: 'POST',
			body: JSON.stringify({
				'bonus_id': bonus_id,
				'degree_type_check': degree_type_check,
				'target': degrees_target,
				'degree': val_value,
				'keyword': key_value,
				'description': desc_value,
				'type': degrees_type	
			}),
			headers: {
			  'Content-Type': 'application/json',
			}
		})
		.then(response => response.json())
		.then(jsonResponse => {
			console.log(jsonResponse)
			if (jsonResponse.success) {

				degree_type_check = false;

				table_type = document.getElementById('degree-table-type');
				table_type.innerHTML = jsonResponse.type;

				const val = document.createElement('div');
				val.className = 'degree-table-deg'
				val.innerHTML = jsonResponse.degree;
		
				const key = document.createElement('div');
				key.className = 'degree-table-key'
				key.innerHTML = jsonResponse.keyword;

				const desc = document.createElement('div');
				desc.className = 'degree-table-desc'
				desc.innerHTML = jsonResponse.description;

				const degDelete = document.createElement('div');
				degDelete.className = 'degree-table-delete'
				const deleteBtn = document.createElement('button');
				deleteBtn.className = 'degree-xbox';
				deleteBtn.setAttribute('data-id', jsonResponse.id);
				degDelete.appendChild(deleteBtn);
	
				const table = document.getElementById('degree-table');
	
				table.style.display = "grid";
				table.style.padding = "1%";
				table.style.maxHeight = table.scrollHeight + "px";
				table.style.padding = "1%";
	
				table.appendChild(val);
				table.appendChild(key);
				table.appendChild(desc);
				table.appendChild(degDelete);

				rows = [val.scrollHeight, desc.scrollHeight, key.scrollHeight];
				let row_height = 0;

				for (i = 0; i < rows.length; i++) {
					if (rows[i] > row_height) {
						row_height = rows[i]
					}
				}

		
				val.style.maxHeight = val.scrollHeight + "px";
				key.style.maxHeight = key.scrollHeight + "px";
				desc.style.maxHeight = desc.scrollHeight + "px";
				degDelete.style.maxHeight = degDelete.scrollHeight + "px";
				table.style.maxHeight = table.scrollHeight + row_height + 15 + "px";

				degree_delete()
	
				errors_delete = document.getElementsByClassName('degree-err-line');

				const errors = document.getElementById('degree-err');
				
				let errors_height = errors.scrollHeight + 20;

				if (typeof errors_delete[0] === "undefined") {
					console.log('no errors defined')
				} else {
					for (i = 0; i < errors_delete.length; i++) {
						errors_delete[i].style.maxHeight = "0px";
						errors_delete[i].style.padding = "0px";
						errors_delete[i].style.marginBottom = "0px";
					}

					errors = document.getElementById('degree-err')

					errors.style.display = "none";
					errors.style.padding = "0px";
					errors.style.maxHeight = "0px";
				}
	
			} else {
				const errors = document.getElementById('degree-err');

				errors.style.display = "grid";
				errors.style.padding = "1%";

				const error = document.createElement('div');
				error.className = 'degree-err-line';
				error.innerHTML = jsonResponse.error;

				errors.appendChild(error);

				error.style.maxHeight = error.scrollHeight + "px";

				errors.style.maxHeight = error.scrollHeight + errors.scrollHeight + 15 + "px";
				errors.style.padding = "1%";
			}
		})				

	} else {

		errors_delete = document.getElementsByClassName('degree-err-line');

		for (i = 0; i < errors_delete.length; i++) {
			errors_delete[i].style.display = "none";
		}
		errors = document.getElementById('degree-err')

		errors.style.display = "grid";
		errors.style.padding = "1%";

		let errors_height = errors.scrollHeight + 20;

		if (degrees_type == '') {
			const error = document.createElement('div');
			error.className = 'degree-err-line'
			error.innerHTML = ' You must enter a degree type';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (degrees_target == '') {
			const error = document.createElement('div');
			error.className = 'degree-err-line'
			error.innerHTML = ' You must enter a target';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (key_value == '') {
			const error = document.createElement('div');
			error.className = 'degree-err-line'
			error.innerHTML = ' You must enter a keyword';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (desc_value == '') {
			const error = document.createElement('div');
			error.className = 'degree-err-line'
			error.innerHTML = ' You must enter a description';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (val_value == '') {
			const error = document.createElement('div');
			error.className = 'degree-err-line'
			error.innerHTML = ' You must enter a degree value';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		errors.style.maxHeight = errors_height + "px";
		errors.style.padding = "1%";
	}
};

degree_delete = function() {
	const deletes = document.querySelectorAll('.degree-xbox');
	const vals = document.querySelectorAll('.degree-table-deg');
	const keys = document.querySelectorAll('.degree-table-key');
	const descs = document.querySelectorAll('.degree-table-desc');
	const deletesDiv = document.querySelectorAll('.degree-table-delete');
	for (let i = 0; i < deletes.length; i++) {
		const btn = deletes[i];
		btn.onclick = function(e) {
			console.log('click')

			const delId = e.target.dataset['id'];
			fetch('/skill/degree_key/delete/' + delId, {
				method: 'DELETE'
			})
			.then(function() {

				vals[i].style.maxHeight = "0px";
				vals[i].style.padding = "0px";
				vals[i].style.marginBottom = "0px";
				keys[i].style.maxHeight = "0px";
				keys[i].style.padding = "0px";
				keys[i].style.marginBottom = "0px";
				descs[i].style.maxHeight = "0px";
				descs[i].style.padding = "0px";
				descs[i].style.marginBottom = "0px";
				deletesDiv[i].style.maxHeight = "0px";
				deletesDiv[i].style.padding = "0px";
				deletesDiv[i].style.marginBottom = "0px";
			})
		}
	}
};

degree_delete();