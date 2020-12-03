function alt_check_entry() {
	const check = "alt_check_check";
	const entry = "alt-check-entry";
	const title = "alt-check-title";
	
	entry_check(check, entry, title)
}

function check_type() {
	const check_field = document.getElementById('check');
	let check_value = check_field.options[check_field.selectedIndex].value;

	alt_check = document.getElementById('alt-check');

	if (check_value != 1) {
		alt_check.style.display = 'grid';
	}
}

alt_check_enter = 0;

function alt_check_submit() {
	
	let des_value = document.getElementById('alt_check_desc').value;
	let dc_field = document.getElementById('alt_check_dc');
	let dc_value = dc_field.options[dc_field.selectedIndex].value; 

	const bonus_id = document.getElementById('bonus_id').value;

	if (dc_value != '' && des_value != '') {

		const dc = document.createElement('div');
		dc.className = 'alt-check-table-dc'
		dc.innerHTML = dc_value;

		const des = document.createElement('div');
		des.className = 'alt-check-table-des'
		des.innerHTML = des_value;
	
		const altDelete = document.createElement('div');
		altDelete.className = 'alt-check-table-delete'
		const deleteBtn = document.createElement('button');
		deleteBtn.className = 'alt-check-xbox';
		deleteBtn.setAttribute('data-id', alt_check_enter);
		altDelete.appendChild(deleteBtn);

		alt_check_enter = alt_check_enter + 1;
	
		const table = document.getElementById('alt-check-table');

		table.style.display = "grid";
		table.style.padding = "1%";
		table.style.maxHeight = table.scrollHeight + "px";
		table.style.padding = "1%";

		table.appendChild(dc);
		table.appendChild(des);
		table.appendChild(altDelete);

		rows = [dc.scrollHeight, des.scrollHeight];
		let row_height = 0;

		for (i = 0; i < rows.length; i++) {
			if (rows[i] > row_height) {
				row_height = rows[i]
			}
		}

		dc.style.maxHeight = dc.scrollHeight + "px";
		des.style.maxHeight = des.scrollHeight + "px";
		altDelete.style.maxHeight = altDelete.scrollHeight + "px";
		table.style.maxHeight = table.scrollHeight + row_height + 15 + "px";

		alt_check_delete()

		errors_delete = document.getElementsByClassName('alt-check-err-line');

		if (typeof errors_delete[0] === "undefined") {
			console.log('no errors defined')
		} else {
			for (i = 0; i < errors_delete.length; i++) {
				errors_delete[i].style.maxHeight = "0px";
				errors_delete[i].style.padding = "0px";
				errors_delete[i].style.marginBottom = "0px";
			}

			errors = document.getElementById('alt-check-err')

			errors.style.display = "none";
			errors.style.padding = "0px";
			errors.style.maxHeight = "0px";
		}

	} else {

		errors_delete = document.getElementsByClassName('alt-check-err-line');

		for (i = 0; i < errors_delete.length; i++) {
			errors_delete[i].style.display = "none";
		}
		const errors = document.getElementById('alt-check-err')

		errors.style.display = "grid";
		errors.style.padding = "1%";

		console.log(dc_value)

		let errors_height = errors.scrollHeight + 20;

		if (dc_value == '') {
			const error = document.createElement('div');
			error.className = 'alt-check-err-line'
			error.innerHTML = ' You must enter a difficulty class';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (des_value == '') {
			const error = document.createElement('div');
			error.className = 'alt-check-err-line'
			error.innerHTML = ' You must enter a difficulty class';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		errors.style.maxHeight = errors_height + "px";
		errors.style.padding = "1%";
	}
};

alt_check_delete = function() {
	const deletes = document.querySelectorAll('.alt-check-xbox');
	const dcs = document.getElementsByClassName('alt-check-table-dc');
	const dess = document.getElementsByClassName('alt-check-table-des');
	const deletesDiv = document.getElementsByClassName('alt-check-table-delete');
	for (let i = 0; i < deletes.length; i++) {
		const btn = deletes[i];
		btn.onclick = function(e) {
			console.log('click')
			dcs[i].style.maxHeight = "0px";
			dcs[i].style.padding = "0px";
			dcs[i].style.marginBottom = "0px";
			dess[i].style.maxHeight = "0px";
			dess[i].style.padding = "0px";
			dess[i].style.marginBottom = "0px";
			deletesDiv[i].style.maxHeight = "0px";
			deletesDiv[i].style.padding = "0px";
			deletesDiv[i].style.marginBottom = "0px";
		}
	}
};

alt_check_delete();