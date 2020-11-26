function resist_effect_check() {
	const resist_effect_check = document.getElementById("resist_effect_check");
	const resist_effect_entry = document.getElementById("resist-effect-entry");
	const title = document.getElementById("resist-effect-title");
	
	if (resist_effect_check.checked == true) {
		resist_effect_entry.style.display = "grid";
		resist_effect_entry.style.padding = "1%";
		resist_effect_entry.style.maxHeight = resist_effect_entry.scrollHeight + "px";
		resist_effect_entry.style.padding = "1%";
		title.style.color = "#af0101";
		title.style.fontSize = "207%";
		setTimeout(function(){title.style.fontSize = "200%"}, 75);
	} else {
		resist_effect_entry.style.maxHeight = "0px";
		resist_effect_entry.style.padding = "0px";
		title.style.color = "#245681";
	}
}





resist_enter = 0;

function resist_submit() {
	
	let ex_value = document.getElementById('resist_effect_examples').value;
	let eff_field = document.getElementById('resist_effect');
	let eff_value = eff_field.options[eff_field.selectedIndex].value; 

	console.log

	const bonus_id = document.getElementById('bonus_id').value;
	
	if (eff_value != '' && ex_value != '') {

		response = fetch('/skill/resist/create', {
			method: 'POST',
			body: JSON.stringify({
				'bonus_id': bonus_id,
				'effect': eff_value,
				'description': ex_value
			}),
			headers: {
			  'Content-Type': 'application/json',
			}
		})
		.then(response => response.json())
		.then(jsonResponse => {
			console.log(jsonResponse)
			if (jsonResponse.success) {

				const eff = document.createElement('div');
				eff.className = 'resist-effect-table-eff'
				eff.innerHTML = jsonResponse.effect;

				const ex = document.createElement('div');
				ex.className = 'resist-effect-table-ex'
				ex.innerHTML = jsonResponse.description;
	
				const resistDelete = document.createElement('div');
				resistDelete.className = 'resist-effect-table-delete'
				const deleteBtn = document.createElement('button');
				deleteBtn.className = 'resist-effect-xbox';
				deleteBtn.setAttribute('data-id', jsonResponse.id);
				resistDelete.appendChild(deleteBtn);

				const table = document.getElementById('resist-effect-table');

				table.style.display = "grid";
				table.style.padding = "1%";
				table.style.maxHeight = table.scrollHeight + "px";
				table.style.padding = "1%";

				table.appendChild(eff);
				table.appendChild(ex);
				table.appendChild(resistDelete);

				rows = [eff.scrollHeight, ex.scrollHeight];
				let row_height = 0;

				for (i = 0; i < rows.length; i++) {
					if (rows[i] > row_height) {
						row_height = rows[i]
					}
				}

				ex.style.maxHeight = ex.scrollHeight + "px";
				eff.style.maxHeight = eff.scrollHeight + "px";
				resistDelete.style.maxHeight = resistDelete.scrollHeight + "px";
				table.style.maxHeight = table.scrollHeight + row_height + 15 + "px";

				resist_delete()
	
				errors_delete = document.getElementsByClassName('resist-effect-err-line');

				if (typeof errors_delete[0] === "undefined") {
					console.log('no errors defined')
				} else {
					for (i = 0; i < errors_delete.length; i++) {
						errors_delete[i].style.maxHeight = "0px";
						errors_delete[i].style.padding = "0px";
						errors_delete[i].style.marginBottom = "0px";
					}

					errors = document.getElementById('resist-effect-err')

					errors.style.display = "none";
					errors.style.padding = "0px";
					errors.style.maxHeight = "0px";
				}

			} else {
				const errors = document.getElementById('resist-effect-err');

				errors.style.display = "grid";
				errors.style.padding = "1%";

				const error = document.createElement('div');
				error.className = 'resist-effect-err-line';
				error.innerHTML = jsonResponse.error;

				errors.appendChild(error);

				error.style.maxHeight = error.scrollHeight + "px";

				errors.style.maxHeight = error.scrollHeight + errors.scrollHeight + 15 + "px";
				errors.style.padding = "1%";
			}
		})

	} else {

		errors_delete = document.getElementsByClassName('resist-effect-err-line');

		for (i = 0; i < errors_delete.length; i++) {
			errors_delete[i].style.display = "none";
		}
		errors = document.getElementById('resist-effect-err')

		errors.style.display = "grid";
		errors.style.padding = "1%";

		let errors_height = errors.scrollHeight + 20;

		if (eff_value == '') {
			const error = document.createElement('div');
			error.className = 'resist-effect-err-line'
			error.innerHTML = ' You must specify the effect';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (ex_value == '') {
			const error = document.createElement('div');
			error.className = 'resist-effect-err-line'
			error.innerHTML = ' You must provide examples';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		errors.style.maxHeight = errors_height + "px";
		errors.style.padding = "1%";
	}
};

resist_delete = function() {
	const deletes = document.querySelectorAll('.resist-effect-xbox');
	const effs = document.getElementsByClassName('resist-effect-table-eff');
	const exs = document.getElementsByClassName('resist-effect-table-ex');
	const deletesDiv = document.getElementsByClassName('resist-effect-table-delete');
	for (let i = 0; i < deletes.length; i++) {
		const btn = deletes[i];
		btn.onclick = function(e) {
			console.log('click')

			const delId = e.target.dataset['id'];
			fetch('/skill/resist/delete/' + delId, {
				method: 'DELETE'
			})
			.then(function() {
				effs[i].style.maxHeight = "0px";
				effs[i].style.padding = "0px";
				effs[i].style.marginBottom = "0px";
				exs[i].style.maxHeight = "0px";
				exs[i].style.padding = "0px";
				exs[i].style.marginBottom = "0px";
				deletesDiv[i].style.maxHeight = "0px";
				deletesDiv[i].style.padding = "0px";
				deletesDiv[i].style.marginBottom = "0px";
				})
		}
	}
};

resist_delete();