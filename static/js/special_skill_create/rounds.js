function rounds_check() {
	const rounds_check = document.getElementById("rounds_check");
	const rounds_entry = document.getElementById("rounds-entry");
	const title = document.getElementById("rounds-title");
	
	if (rounds_check.checked == true) {
		rounds_entry.style.display = "grid";
		rounds_entry.style.padding = "1%";
		rounds_entry.style.maxHeight = rounds_entry.scrollHeight + "px";
		rounds_entry.style.padding = "1%";
		title.style.color = "#af0101";
		title.style.fontSize = "207%";
		setTimeout(function(){title.style.fontSize = "200%"}, 75);
	} else {
		rounds_entry.style.maxHeight = "0px";
		rounds_entry.style.padding = "0px";
		title.style.color = "#245681";
	}
}





rounds_enter = 0;

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
	
	if (rank_value != '' && mod_value != '' && rnd_value != '') {

		const dc = document.createElement('div');
		dc.className = 'rounds-table-dc'
		dc.innerHTML = dc_value;

		const deg = document.createElement('div');
		deg.className = 'rounds-table-degree'
		deg.innerHTML = deg_value;

		const rank = document.createElement('div');
		rank.className = 'rounds-table-rank'
		rank.innerHTML = rank_value;

		const mod = document.createElement('div');
		mod.className = 'rounds-table-mod'
		mod.innerHTML = mod_value;
	
		const rnd = document.createElement('div');
		rnd.className = 'rounds-table-rounds'
		rnd.innerHTML = rnd_value;
	
		const rndDelete = document.createElement('div');
		rndDelete.className = 'rounds-table-delete'
		const deleteBtn = document.createElement('button');
		deleteBtn.className = 'rounds-xbox';
		deleteBtn.innerHTML = '&cross;';
		deleteBtn.setAttribute('data-id', rounds_enter);
		rndDelete.appendChild(deleteBtn);

		other_enter = other_enter + 1;
	
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

		errors_delete = document.getElementsByClassName('rounds-err-line');

		if (typeof errors_delete[0] === "undefined") {
			console.log('no errors defined')
		} else {
			for (i = 0; i < errors_delete.length; i++) {
				errors_delete[i].style.maxHeight = "0px";
				errors_delete[i].style.padding = "0px";
				errors_delete[i].style.marginBottom = "0px";
			}

			errors = document.getElementById('rounds-err')

			errors.style.display = "none";
			errors.style.padding = "0px";
			errors.style.maxHeight = "0px";
		}

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
	const deletes = document.querySelectorAll('.rounds-xbox');
	const dcs = document.getElementsByClassName('rounds-table-dc');
	const degs = document.getElementsByClassName('rounds-table-degree');
	const ranks = document.getElementsByClassName('rounds-table-rank');
	const modss = document.getElementsByClassName('rounds-table-mod');
	const rnds = document.getElementsByClassName('rounds-table-rounds');
	const deletesDivs = document.getElementsByClassName('rounds-table-delete');
	for (let i = 0; i < deletes.length; i++) {
		const btn = deletes[i];
		btn.onclick = function(e) {
			console.log('click')
			dcs[i].style.maxHeight = "0px";
			dcs[i].style.padding = "0px";
			dcs[i].style.marginBottom = "0px";
			degs[i].style.maxHeight = "0px";
			degs[i].style.padding = "0px";
			degs[i].style.marginBottom = "0px";
			ranks[i].style.maxHeight = "0px";
			ranks[i].style.padding = "0px";
			ranks[i].style.marginBottom = "0px";
			modss[i].style.maxHeight = "0px";
			modss[i].style.padding = "0px";
			modss[i].style.marginBottom = "0px";
			rnds[i].style.maxHeight = "0px";
			rnds[i].style.padding = "0px";
			rnds[i].style.marginBottom = "0px";
			deletesDivs[i].style.maxHeight = "0px";
			deletesDivs[i].style.padding = "0px";
			deletesDivs[i].style.marginBottom = "0px";
		}
	}
};

rounds_delete();