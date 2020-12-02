function extras_submit() {
	
	let des = document.getElementById('extra_des').value;
	let name = document.getElementById('extra_name').value;
	let cost_field = document.getElementById('extra_cost');
	let cost = cost_field.options[cost_field.selectedIndex].value;
	let rank_field = document.getElementById('extra_rank');
	let rank = rank_field.options[rank_field.selectedIndex].value;
	let inherit_field = document.getElementById('extra_inherit');
	let inherit = inherit_field.options[inherit_field.selectedIndex].value;

	const power_id = document.getElementById('power_id').value;
	
	if (des != '' && name != '' &&  cost != '' && rank != '') {

		response = fetch('/power/extra/create', {
			method: 'POST',
			body: JSON.stringify({
				'power_id': power_id,
				'name': name,
				'cost': cost,
				'ranks': rank,
				'des': des,
				'inherit': inherit
			}),
			headers: {
			  'Content-Type': 'application/json',
			}
		})
		.then(response => response.json())
		.then(jsonResponse => {
			console.log(jsonResponse)
			if (jsonResponse.success) {

				const selects = document.getElementsByClassName('extra-select')
				let select;

				for (select of selects)  {
					let option = document.createElement("option")
					option.value = jsonResponse.id;
					option.text = jsonResponse.name;
					select.add(option);
				}

				const selects_sml = document.getElementsByClassName('extra-sml')
				let select_sml;

				for (select_sml of selects_sml)  {
					let option = document.createElement("option")
					option.value = jsonResponse.id;
					option.text = jsonResponse.name;
					select_sml.add(option);
				}

				const nam = document.createElement('div');
				nam.className = 'extras-table-nam'
				nam.innerHTML = jsonResponse.name;

				const pnt = document.createElement('div');
				pnt.className = 'extras-table-pnt'
				pnt.innerHTML = jsonResponse.cost;

				const rnk = document.createElement('div');
				rnk.className = 'extras-table-rnk'
				rnk.innerHTML = jsonResponse.ranks;				

				const des = document.createElement('div');
				des.className = 'extras-table-des'
				des.innerHTML = jsonResponse.des;

				const inh = document.createElement('div');
				inh.className = 'extras-table-inh'
				inh.innerHTML = jsonResponse.des;
			
				const exDelete = document.createElement('div');
				exDelete.className = 'extras-table-del'
				const deleteBtn = document.createElement('button');
				deleteBtn.className = 'extras-xbox';
				deleteBtn.innerHTML = '&cross;';
				deleteBtn.setAttribute('data-id', jsonResponse.id);
				exDelete.appendChild(deleteBtn);

				const table = document.getElementById('extras-table');

				table.style.display = "grid";
				table.style.padding = "1%";
				table.style.maxHeight = table.scrollHeight + "px";
				table.style.padding = "1%";

				table.appendChild(nam);
				table.appendChild(pnt);
				table.appendChild(rnk);
				table.appendChild(des)
				table.appendChild(inh)
				table.appendChild(exDelete);

				rows = [nam.scrollHeight, pnt.scrollHeight, rnk.scrollHeight, des.scrollHeight, inh.scrollHeight];
				let row_height = 0;

				for (i = 0; i < rows.length; i++) {
					if (rows[i] > row_height) {
						row_height = rows[i]
					}
				}
				
				nam.style.maxHeight = nam.scrollHeight + "px";
				pnt.style.maxHeight = pnt.scrollHeight + "px";
				rnk.style.maxHeight = rnk.scrollHeight + "px";
				des.style.maxHeight = des.scrollHeight + "px";
				exDelete.style.maxHeight = exDelete.scrollHeight + "px";
				table.style.maxHeight = table.scrollHeight + row_height + 15 + "px";

				extras_delete()
			
				const errors_delete = document.getElementsByClassName('extras-err-line');

				if (typeof errors_delete[0] === "undefined") {
					console.log('no errors defined')
				} else {
					for (i = 0; i < errors_delete.length; i++) {
						errors_delete[i].style.maxHeight = "0px";
						errors_delete[i].style.padding = "0px";
						errors_delete[i].style.marginBottom = "0px";
					}

					const errors = document.getElementById('extras-err')

					errors.style.display = "none";
					errors.style.padding = "0px";
					errors.style.maxHeight = "0px";
				}

			} else {
				const errors = document.getElementById('extras-err');

				errors.style.display = "grid";
				errors.style.padding = "1%";

				const error = document.createElement('div');
				error.className = 'extras-err-line';
				error.innerHTML = jsonResponse.error;

				errors.appendChild(error);

				error.style.maxHeight = error.scrollHeight + "px";

				errors.style.maxHeight = error.scrollHeight + errors.scrollHeight + 15 + "px";
				errors.style.padding = "1%";
			}
		})

	} else {

		const errors_delete = document.getElementsByClassName('extras-err-line');

		for (i = 0; i < errors_delete.length; i++) {
			errors_delete[i].style.display = "none";
		}
		const errors = document.getElementById('extras-err')

		errors.style.display = "grid";
		errors.style.padding = "1%";

		let errors_height = errors.scrollHeight + 20;

		if (des == '') {
			const error = document.createElement('div');
			error.className = 'extras-err-line'
			error.innerHTML = ' You must enter a description';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (name == '') {
			const error = document.createElement('div');
			error.className = 'extras-err-line'
			error.innerHTML = ' You must enter a name for the subskill';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (rank == '') {
			const error = document.createElement('div');
			error.className = 'extras-err-line'
			error.innerHTML = ' You must set thhe number of ranks for the specified points';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (cost == '') {
			const error = document.createElement('div');
			error.className = 'extras-err-line'
			error.innerHTML = ' You must specify how many points this extra costs';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		errors.style.maxHeight = errors_height + "px";
		errors.style.padding = "1%";
	}
};

extras_delete = function() {
	const deletes = document.querySelectorAll('.extras-xbox');
	const nams = document.getElementsByClassName('extras-table-nam');
	const rnks = document.getElementsByClassName('extras-table-rnk');
	const pnts = document.getElementsByClassName('extras-table-pnt');
	const dess = document.getElementsByClassName('extras-table-des');
	const inhs = document.getElementsByClassName('extras-table-inh');
	const deletesDiv = document.getElementsByClassName('extras-table-del');
	for (let i = 0; i < deletes.length; i++) {
		const btn = deletes[i];
		btn.onclick = function(e) {
			console.log('click')

			const delId = e.target.dataset['id'];
			fetch('/power/extra/delete/' + delId, {
				method: 'DELETE'
			})
			.then(function() {

				const selects = document.getElementsByClassName('extra-select');
				let select;

				for (select of selects) {
					options = select.options;
					let option;

					for (option of options) {
						if (option.value == delId) {
							console.log(option.value);
							option.remove();
						}
					}
				}

				nams[i].style.maxHeight = "0px";
				nams[i].style.padding = "0px";
				nams[i].style.marginBottom = "0px";
				rnks[i].style.maxHeight = "0px";
				rnks[i].style.padding = "0px";
				rnks[i].style.marginBottom = "0px";
				pnts[i].style.maxHeight = "0px";
				pnts[i].style.padding = "0px";
				pnts[i].style.marginBottom = "0px";
				dess[i].style.maxHeight = "0px";
				dess[i].style.padding = "0px";
				dess[i].style.marginBottom = "0px";
				inhs[i].style.maxHeight = "0px";
				inhs[i].style.padding = "0px";
				inhs[i].style.marginBottom = "0px";
				deletesDiv[i].style.maxHeight = "0px";
				deletesDiv[i].style.padding = "0px";
				deletesDiv[i].style.marginBottom = "0px";
			})
		}
	}
};

extras_delete();