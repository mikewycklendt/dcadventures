function opp_cond_check() {
	const opp_cond_check = "opp_cond_check";
	const opp_cond_entry = "opp-cond-entry";
	const title = "opp-cond-title";
	
	entry_check(opp_cond_check, opp_cond_entry, title);
}

opp_cond_enter = 0;

function opp_cond_submit() {
	
	let des_value = document.getElementById('opp_cond_desc').value;
	let deg_field = document.getElementById('opp_cond_degree');
	let deg_value = deg_field.options[deg_field.selectedIndex].value; 
	let con_field = document.getElementById('opp_cond_cond');
	let con_value = con_field.options[con_field.selectedIndex].value; 
	let rnd_field = document.getElementById('opp_cond_rounds');
	let rnd_value = rnd_field.options[rnd_field.selectedIndex].value; 

	const bonus_id = document.getElementById('bonus_id').value;
	const error_line = 'opp-cond-err-line';
	const error_table = 'opp-cond-err';
	
	if (des_value != '' && deg_value != '' && con_value != '' && rnd_value != '') {

		response = fetch('/skill/opp_condition/create', {
			method: 'POST',
			body: JSON.stringify({
				'bonus_id': bonus_id,
				'degree': deg_value,
				'condition': con_value,
				'rounds': rnd_value,
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
				deg.className = 'opp-cond-table-deg'
				deg.innerHTML = jsonResponse.degree;

				const con = document.createElement('div');
				con.className = 'opp-cond-table-con'
				con.innerHTML = jsonResponse.condition;

				const rnd = document.createElement('div');
				rnd.className = 'opp-cond-table-rnd'
				rnd.innerHTML = jsonResponse.rounds;

				const des = document.createElement('div');
				des.className = 'opp-cond-table-des'
				des.innerHTML = jsonResponse.description;
			
				const ocDelete = document.createElement('div');
				ocDelete.className = 'opp-cond-table-delete'
				const deleteBtn = document.createElement('button');
				deleteBtn.className = 'opp-cond-xbox';
				deleteBtn.setAttribute('data-id', jsonResponse.id);
				ocDelete.appendChild(deleteBtn);

				const table = document.getElementById('opp-cond-table');

				table.style.display = "grid";
				table.style.padding = "1%";
				table.style.maxHeight = table.scrollHeight + "px";
				table.style.padding = "1%";

				table.appendChild(deg);
				table.appendChild(con);
				table.appendChild(rnd);
				table.appendChild(des)
				table.appendChild(ocDelete);

				rows = [deg.scrollHeight, con.scrollHeight, rnd.scrollHeight, des.scrollHeight];
				let row_height = 0;

				for (i = 0; i < rows.length; i++) {
					if (rows[i] > row_height) {
						row_height = rows[i]
					}
				}
				
				deg.style.maxHeight = deg.scrollHeight + "px";
				con.style.maxHeight = con.scrollHeight + "px";
				rnd.style.maxHeight = rnd.scrollHeight + "px";
				des.style.maxHeight = des.scrollHeight + "px";
				ocDelete.style.maxHeight = ocDelete.scrollHeight + "px";
				table.style.maxHeight = table.scrollHeight + row_height + 15 + "px";

				opp_cond_delete()
			
				clear_errors(error_line, error_table);

			} else {
				back_error(error_line, error_table);
			}
		})

	} else {

		errors_delete = document.getElementsByClassName('opp-cond-err-line');

		for (i = 0; i < errors_delete.length; i++) {
			errors_delete[i].style.display = "none";
		}
		errors = document.getElementById('opp-cond-err')

		errors.style.display = "grid";
		errors.style.padding = "1%";

		let errors_height = errors.scrollHeight + 20;

		if (des_value == '') {
			const error = document.createElement('div');
			error.className = 'opp-cond-err-line'
			error.innerHTML = ' You must enter a description';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (deg_value == '') {
			const error = document.createElement('div');
			error.className = 'opp-cond-err-line'
			error.innerHTML = ' You must enter a required degree of success';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (con_value == '') {
			const error = document.createElement('div');
			error.className = 'opp-cond-err-line'
			error.innerHTML = ' You must enter a condition';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (rnd_value == '') {
			const error = document.createElement('div');
			error.className = 'opp-cond-err-line'
			error.innerHTML = ' You must specify how long the condition lasts';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		errors.style.maxHeight = errors_height + "px";
		errors.style.padding = "1%";
	}
};

opp_cond_delete = function() {
	const deletes = '.opp-cond-xbox';
	const divs = ['opp-cond-table-deg', 'opp-cond-table-con', 'opp-cond-table-rnd', 'opp-cond-table-des', 'opp-cond-table-delete'];
	const route = '/skill/opp_condition/delete/';

	delete_function(deletes, divs, route);
};

opp_cond_delete();