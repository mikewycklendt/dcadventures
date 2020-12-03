function char_check() {
	const char_check = "char_check";
	const char_base_form = "char-base-form";
	const title = "char-title";
	const entry = 'char-entry';
	
	check_title(char_check, title, char_base_form, entry);
}

function char_base() {
	const char_type = "char_type";
	const char_target = "char_target";
	const char_entry = "char-entry";

	base_two(char_type, char_target, char_entry);
}
char_enter = 0;

function char_submit() {
	const tar_field = document.getElementById("char_target");
	const chk_field = document.getElementById("char_type");
	let chk_value = chk_field.options[chk_field.selectedIndex].value;
	let tar_value =  tar_field.options[tar_field.selectedIndex].value;
	
	let deg_field = document.getElementById('char_value');
	let rnk_field = document.getElementById('char_rank');

	let des_value = document.getElementById('char_desc').value;

	let deg_value = deg_field.options[deg_field.selectedIndex].value;
	let rnk_value = rnk_field.options[rnk_field.selectedIndex].value;

	const bonus_id = document.getElementById('bonus_id').value;
	
	if (deg_value != '' && tar_value != '' && chk_value != '' && rnk_value != '' && des_value != '') {

		response = fetch('/skill/char_check/create', {
			method: 'POST',
			body: JSON.stringify({
				'bonus_id': bonus_id,
				'check_id': chk_value,
				'target': tar_value,
				'degree': deg_value,
				'rank': rnk_value,
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

				const deg = document.createElement('div');
				deg.className = 'char-table-deg'
				deg.innerHTML = jsonResponse.degree;

				const tar = document.createElement('div');
				tar.className = 'char-table-tar';
				tar.innerHTML = jsonResponse.target;

				const chk = document.createElement('div');
				chk.className = 'char-table-chk';
				chk.innerHTML = jsonResponse.check_id;

				const rnk = document.createElement('div');
				rnk.className = 'char-table-rnk';
				rnk.innerHTML = jsonResponse.rank;

				const des = document.createElement('div');
				des.className = 'char-table-des';
				des.innerHTML = jsonResponse.description;

				const charDelete = document.createElement('div');
				charDelete.className = 'char-table-delete'
				const deleteBtn = document.createElement('button');
				deleteBtn.className = 'char-xbox';
				deleteBtn.setAttribute('data-id', jsonResponse.id);
				charDelete.appendChild(deleteBtn);

				const table = document.getElementById('char-table');
			
				table.style.display = "grid";
				table.style.padding = "1%";
				table.style.maxHeight = table.scrollHeight + "px";
				table.style.padding = "1%";
			
				table.appendChild(deg);
				table.appendChild(tar);
				table.appendChild(chk);
				table.appendChild(rnk);
				table.appendChild(des)
				table.appendChild(charDelete);

				rows = [deg.scrollHeight, des.scrollHeight, tar.scrollHeight, chk.scrollHeight, rnk.scrollHeight];
				let row_height = 0;

				for (i = 0; i < rows.length; i++) {
					if (rows[i] > row_height) {
						row_height = rows[i]
					}
				}

				deg.style.maxHeight = deg.scrollHeight + "px";
				tar.style.maxHeight = tar.scrollHeight + "px";
				chk.style.maxHeight = chk.scrollHeight + "px";
				rnk.style.maxHeight = rnk.scrollHeight + "px";
				des.style.maxHeight = des.scrollHeight + "px";
				charDelete.style.maxHeight = charDelete.scrollHeight + "px";
				table.style.maxHeight = table.scrollHeight + row_height + 15 + "px";

				char_delete()
			
				errors_delete = document.getElementsByClassName('char-err-line');

				if (typeof errors_delete[0] === "undefined") {
					console.log('no errors defined')
				} else {
					for (i = 0; i < errors_delete.length; i++) {
						errors_delete[i].style.maxHeight = "0px";
						errors_delete[i].style.padding = "0px";
						errors_delete[i].style.marginBottom = "0px";
					}

					errors = document.getElementById('char-err')

					errors.style.display = "none";
					errors.style.padding = "0px";
					errors.style.maxHeight = "0px";
				}

			} else {
				const errors = document.getElementById('char-err');

				errors.style.display = "grid";
				errors.style.padding = "1%";

				const error = document.createElement('div');
				error.className = 'char-err-line';
				error.innerHTML = jsonResponse.error;
	
				errors.appendChild(error);
	
				error.style.maxHeight = error.scrollHeight + "px";
	
				errors.style.maxHeight = error.scrollHeight + errors.scrollHeight + 15 + "px";
				errors.style.padding = "1%";
			}
		})


	} else {

		errors_delete = document.getElementsByClassName('char-err-line');

		for (i = 0; i < errors_delete.length; i++) {
			errors_delete[i].style.display = "none";
		}
		errors = document.getElementById('char-err')

		errors.style.display = "grid";
		errors.style.padding = "1%";
		
		let errors_height = errors.scrollHeight + 20;

		if (deg_value == '') {
			const error = document.createElement('div');
			error.className = 'char-err-line'
			error.innerHTML = ' You must specify the required degree of success';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (tar_value == '') {
			const error = document.createElement('div');
			error.className = 'char-err-line'
			error.innerHTML = ' You must choose a target';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (chk_value == '') {
			const error = document.createElement('div');
			error.className = 'char-err-line'
			error.innerHTML = ' You must choose a check type';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (rnk_value == '') {
			const error = document.createElement('div');
			error.className = 'char-err-line'
			error.innerHTML = ' You must choose the rank type for the check';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (des_value != '') {
			const error = document.createElement('div');
			error.className = 'char-err-line'
			error.innerHTML = ' You must enter a description';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		errors.style.maxHeight = errors_height + "px";
		errors.style.padding = "1%";
	}
};

char_delete = function() {
	const deletes = document.querySelectorAll('.char-xbox');
	const degs = document.querySelectorAll('.char-table-deg');
	const chks = document.querySelectorAll('.char-table-chk');
	const rnks = document.querySelectorAll('.char-table-rnk');
	const dess = document.querySelectorAll('.char-table-des');
	const tars = document.querySelectorAll('.char-table-tar');
	const deletesDiv = document.querySelectorAll('.char-table-delete');
	for (let i = 0; i < deletes.length; i++) {
		const btn = deletes[i];
		btn.onclick = function(e) {
			console.log('click')

			const delId = e.target.dataset['id'];
			fetch('/skill/char_check/delete/' + delId, {
				method: 'DELETE'
			})
			.then(function() {

				degs[i].style.maxHeight = "0px";
				degs[i].style.padding = "0px";
				degs[i].style.marginBottom = "0px";
				chks[i].style.maxHeight = "0px";
				chks[i].style.padding = "0px";
				chks[i].style.marginBottom = "0px";
				rnks[i].style.maxHeight = "0px";
				rnks[i].style.padding = "0px";
				rnks[i].style.marginBottom = "0px";
				dess[i].style.maxHeight = "0px";
				dess[i].style.padding = "0px";
				dess[i].style.marginBottom = "0px";
				tars[i].style.maxHeight = "0px";
				tars[i].style.padding = "0px";
				tars[i].style.marginBottom = "0px";
				deletesDiv[i].style.maxHeight = "0px";
				deletesDiv[i].style.padding = "0px";
				deletesDiv[i].style.marginBottom = "0px";
			})
		}
	}
};

char_delete();