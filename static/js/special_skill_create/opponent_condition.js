function opp_cond_check() {
	const opp_cond_check = document.getElementById("opp_cond_check");
	const opp_cond_entry = document.getElementById("opp-cond-entry");
	
	if (opp_cond_check.checked == true) {
		opp_cond_entry.style.display = "grid";
		opp_cond_entry.style.padding = "1%";
		opp_cond_entry.style.maxHeight = opp_cond_entry.scrollHeight + "px";
		opp_cond_entry.style.padding = "1%";
	} else {
		opp_cond_entry.style.maxHeight = "0px";
		opp_cond_entry.style.padding = "0px";
	}
}

opp_cond_enter = 0;

function opp_cond_submit() {
	const table = document.getElementById('opp-cond-table');

	table.style.display = "grid";
	table.style.padding = "1%";
	table.style.maxHeight = table.scrollHeight + "px";
	table.style.padding = "1%";
	
	let des_value = document.getElementById('opp_cond_desc').value;
	let deg_field = document.getElementById('opp_cond_degree');
	let deg_value = deg_field.options[deg_field.selectedIndex].value; 
	let con_field = document.getElementById('opp_cond_cond');
	let con_value = con_field.options[con_field.selectedIndex].value; 
	let rnd_field = document.getElementById('opp_cond_rounds');
	let rnd_value = rnd_field.options[rnd_field.selectedIndex].value; 

	console.log
	
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
	
		table.appendChild(deg);
		table.appendChild(con);
		table.appendChild(rnd);
		table.appendChild(des)
		table.appendChild(ocDelete);

		
		deg.style.maxHeight = deg.scrollHeight + "px";
		con.style.maxHeight = con.scrollHeight + "px";
		rnd.style.maxHeight = rnd.scrollHeight + "px";
		des.style.maxHeight = des.scrollHeight + "px";
		ocDelete.style.maxHeight = ocDelete.scrollHeight + "px";
		table.style.maxHeight = table.scrollHeight + 20 + "px";

		opp_cond_delete()
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