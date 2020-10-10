function opp_cond_check() {
	const opp_cond_check = document.getElementById("opp_cond_check");
	const opp_cond_entry = document.getElementById("opp-cond-entry");
	const title = document.getElementById("opp-cond-title");
	
	if (opp_cond_check.checked == true) {
		opp_cond_entry.style.display = "grid";
		opp_cond_entry.style.padding = "1%";
		opp_cond_entry.style.maxHeight = opp_cond_entry.scrollHeight + "px";
		opp_cond_entry.style.padding = "1%";
		title.style.color = "#af0101";
		title.style.fontSize = "207%";
		setTimeout(function(){title.style.fontSize = "200%"}, 75);
	} else {
		opp_cond_entry.style.maxHeight = "0px";
		opp_cond_entry.style.padding = "0px";
		title.style.color = "#245681";
	}
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
	
	if (des_value != '' && deg_value != '' && con_value != '' && rnd_value != '') {

		const deg = document.createElement('div');
		deg.className = 'opp-cond-table-deg'
		deg.innerHTML = deg_value;

		const con = document.createElement('div');
		con.className = 'opp-cond-table-con'
		con.innerHTML = con_value;

		const rnd = document.createElement('div');
		rnd.className = 'opp-cond-table-rnd'
		rnd.innerHTML = rnd_value;

		const des = document.createElement('div');
		des.className = 'opp-cond-table-des'
		des.innerHTML = des_value;
	
		const ocDelete = document.createElement('div');
		ocDelete.className = 'opp-cond-table-delete'
		const deleteBtn = document.createElement('button');
		deleteBtn.className = 'opp-cond-xbox';
		deleteBtn.innerHTML = '&cross;';
		deleteBtn.setAttribute('data-id', opp_cond_enter);
		ocDelete.appendChild(deleteBtn);

		opp_cond_enter = opp_cond_enter + 1;
	
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
	
		errors_delete = document.getElementsByClassName('opp-cond-err-line');

		if (typeof errors_delete[0] === "undefined") {
			console.log('no errors defined')
		} else {
			for (i = 0; i < errors_delete.length; i++) {
				errors_delete[i].style.maxHeight = "0px";
				errors_delete[i].style.padding = "0px";
				errors_delete[i].style.marginBottom = "0px";
			}

			errors = document.getElementById('opp-cond-err')

			errors.style.display = "none";
			errors.style.padding = "0px";
			errors.style.maxHeight = "0px";
		}

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
	const deletes = document.querySelectorAll('.opp-cond-xbox');
	const degs = document.getElementsByClassName('opp-cond-table-deg');
	const cons = document.getElementsByClassName('opp-cond-table-con');
	const rnds = document.getElementsByClassName('opp-cond-table-rnd');
	const dess = document.getElementsByClassName('opp-cond-table-des');
	const deletesDiv = document.getElementsByClassName('opp-cond-table-delete');
	for (let i = 0; i < deletes.length; i++) {
		const btn = deletes[i];
		btn.onclick = function(e) {
			console.log('click')
			degs[i].style.maxHeight = "0px";
			degs[i].style.padding = "0px";
			degs[i].style.marginBottom = "0px";
			cons[i].style.maxHeight = "0px";
			cons[i].style.padding = "0px";
			cons[i].style.marginBottom = "0px";
			rnds[i].style.maxHeight = "0px";
			rnds[i].style.padding = "0px";
			rnds[i].style.marginBottom = "0px";
			dess[i].style.maxHeight = "0px";
			dess[i].style.padding = "0px";
			dess[i].style.marginBottom = "0px";
			deletesDiv[i].style.maxHeight = "0px";
			deletesDiv[i].style.padding = "0px";
			deletesDiv[i].style.marginBottom = "0px";
		}
	}
};

opp_cond_delete();