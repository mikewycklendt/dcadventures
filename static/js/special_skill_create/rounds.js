function rounds_check() {
	const rounds_check = "rounds_check";
	const rounds_entry = "rounds-entry";
	const title = "rounds-title";
	
	entry_check(rounds_check, rounds_entry, title);
}

function rounds_submit() {
	
	let dc_field = document.getElementById('rounds_dc');
	let dc_value =  dc_field.options[dc_field.selectedIndex].value;
	let deg_field = document.getElementById('rounds_degree');
	let deg_value =  deg_field.options[dc_field.selectedIndex].value;
	let rank_field = document.getElementById('rounds_rank');
	let rank_value =  rank_field.options[rank_field.selectedIndex].value;
	let mod_field = document.getElementById('rounds_mod');
	let mod_value =  mod_field.options[mod_field.selectedIndex].value;
	let rnd_field = document.getElementById('rounds_rounds');
	let rnd_value =  rnd_field.options[rnd_field.selectedIndex].value; 

	const bonus_id = document.getElementById('bonus_id').value;
	const error_line = 'rounds-err-line';
	const error_table = 'rounds-err';
	
	if (rank_value != '' && mod_value != '' && rnd_value != '') {

		response = fetch('/skill/rounds/create', {
			method: 'POST',
			body: JSON.stringify({
				'bonus_id': bonus_id,
				'dc': dc_value,
				'degree': deg_value,
				'rank': rank_value,
				'mod': mod_value,
				'rounds': rnd_value
			}),
			headers: {
			  'Content-Type': 'application/json',
			}
		})
		.then(response => response.json())
		.then(jsonResponse => {
			console.log(jsonResponse)
			if (jsonResponse.success) {

				const dc = document.createElement('div');
				dc.className = 'rounds-table-dc'
				dc.innerHTML = jsonResponse.dc;

				const deg = document.createElement('div');
				deg.className = 'rounds-table-degree'
				deg.innerHTML = jsonResponse.degree;

				const rank = document.createElement('div');
				rank.className = 'rounds-table-rank'
				rank.innerHTML = jsonResponse.rank;

				const mod = document.createElement('div');
				mod.className = 'rounds-table-mod'
				mod.innerHTML = jsonResponse.mod;
	
				const rnd = document.createElement('div');
				rnd.className = 'rounds-table-rounds'
				rnd.innerHTML = jsonResponse.rounds;
	
				const rndDelete = document.createElement('div');
				rndDelete.className = 'rounds-table-delete'
				const deleteBtn = document.createElement('button');
				deleteBtn.className = 'rounds-xbox';
				deleteBtn.setAttribute('data-id', jsonResponse.id );
				rndDelete.appendChild(deleteBtn);

				const table = document.getElementById('rounds-table');

				table.style.display = "grid";
				table.style.padding = "1%";
				table.style.maxHeight = table.scrollHeight + "px";
				table.style.padding = "1%";
		
				table.appendChild(dc);
				table.appendChild(deg);
				table.appendChild(rank);
				table.appendChild(mod);
				table.appendChild(rnd);
				table.appendChild(rndDelete);

				rows = [dc.scrollHeight, deg.scrollHeight, rank.scrollHeight, mod.scrollHeight, rnd.scrollHeight];
				let row_height = 0;

				for (i = 0; i < rows.length; i++) {
					if (rows[i] > row_height) {
						row_height = rows[i]
					}
				}

				dc.style.maxHeight = dc.scrollHeight + "px";
				deg.style.maxHeight = deg.scrollHeight + "px";
				rank.style.maxHeight = rank.scrollHeight + "px";
				mod.style.maxHeight = mod.scrollHeight + "px";
				rnd.style.maxHeight = rnd.scrollHeight + "px";
				rndDelete.style.maxHeight = rndDelete.scrollHeight + "px";
				table.style.maxHeight = table.scrollHeight + row_height + 15 + "px";

				rounds_delete()

				clear_errors(error_line, error_table);
			} else {
				back_error(error_line, error_table);
			}
		})

	} else {

		errors_delete = document.getElementsByClassName('rounds-err-line');

		for (i = 0; i < errors_delete.length; i++) {
			errors_delete[i].style.display = "none";
		}
		errors = document.getElementById('rounds-err')

		errors.style.display = "grid";
		errors.style.padding = "1%";

		let errors_height = errors.scrollHeight + 20;

		if (rank_value == '') {
			const error = document.createElement('div');
			error.className = 'rounds-err-line'
			error.innerHTML = ' You must choose a rank';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (mod_value == '') {
			const error = document.createElement('div');
			error.className = 'rounds-err-line'
			error.innerHTML = ' You must specify the modifier';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (rnd_value == '') {
			const error = document.createElement('div');
			error.className = 'rounds-err-line'
			error.innerHTML = ' You must specify how many rounds this lasts';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		errors.style.maxHeight = errors_height + "px";
		errors.style.padding = "1%";
	}
};

rounds_delete = function() {
	const deletes = '.rounds-xbox';
	const divs = ['rounds-table-dc', 'rounds-table-degree', 'rounds-table-rank', 'rounds-table-mod', 'rounds-table-rounds', 'rounds-table-delete'];
	const route = '/skill/rounds/delete/';
	
	delete_function(deletes, divs, route);
};

rounds_delete();