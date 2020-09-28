function char_check() {
	const char_check = document.getElementById("char_check");
	const char_base_form = document.getElementById("char-base-form");
	
	if (char_check.checked == true) {
		char_base_form.style.opacity = "100%";
	} else {
		char_base_form.style.opacity = "0%";
	}
}

function char_base() {
	const char_type = document.getElementById("char_type");
	const char_target = document.getElementById("char_target");
	let chartype = circ_skill.options[char_type.selectedIndex].value;
	let chartarget =  char_target.options[char_target.selectedIndex].value;
	console.log(chartype);
	console.log(chartarget);
	const char_entry = document.getElementById("char-entry");

	if (chartype != '' && chartarget != '') {
		char_entry.style.display = "grid";
		char_entry.style.padding = "1%";
		char_entry.style.maxHeight = char_entry.scrollHeight + "px";
		char_entry.style.padding = "1%";
	} else {
		char_entry.style.maxHeight = "0px";
		char_entry.style.padding = "0px";
	}
}
char_enter = 0;

function char_submit() {
	const table = document.getElementById('char-table');
	const tar_field = document.getElementById("char_target");
	const chk_field = document.getElementById("char_type");
	let chk_value = chk_field.options[chk_field.selectedIndex].value;
	let tar_value =  tar_field.options[tar_field.selectedIndex].value;

	table.style.display = "grid";
	table.style.padding = "1%";
	table.style.maxHeight = table.scrollHeight + "px";
	table.style.padding = "1%";
	
	let deg_field = document.getElementById('char_val');
	let chk_field = document.getElementById('char_rank');

	let des_value = document.getElementById('char_value').value;

	let deg_value = deg_field.options[deg_field.selectedIndex].value;
	let rnk_value = rnk_field.options[rnk_field.selectedIndex].value;
	let chk_value = chk_field.options[chk_field.selectedIndex].value;
 
	
	if (deg_value != '' && tar_value != '' && chk_value != '' && rnk_value != '' && des_value != '') {
		const deg = document.createElement('div');
		deg.className = 'char-table-deg'
		deg.innerHTML = deg_value;

		const tar = document.createElement('div');
		tar.className = 'char-table-tar';
		tar.innerHTML = tar_value;

		const chk = document.createElement('div');
		chk.className = 'char-table-chk';
		chk.innerHTML = chk_value;

		const rnk = document.createElement('div');
		rnk.className = 'char-table-rnk';
		rnk.innerHTML = rnk_value;

		const des = document.createElement('div');
		des.className = 'char-table-des';
		des.innerHTML = des_value;

		const charDelete = document.createElement('div');
		charDelete.className = 'char-table-delete'
		const deleteBtn = document.createElement('button');
		deleteBtn.className = 'char-xbox';
		deleteBtn.innerHTML = '&cross;';
		deleteBtn.setAttribute('data-id', char_enter);
		charDelete.appendChild(deleteBtn);

		char_enter = char_enter + 1;
	
		table.appendChild(deg);
		table.appendChild(tar);
		table.appendChild(chk);
		table.appendChild(rnk);
		table.appendChild(des)
		table.appendChild(charDelete);

		
		mod.style.maxHeight = mod.scrollHeight + "px";
		rnd.style.maxHeight = rnd.scrollHeight + "px";
		circ.style.maxHeight = circ.scrollHeight + "px";
		charDelete.style.maxHeight = charDelete.scrollHeight + "px";
		table.style.maxHeight = table.scrollHeight + 20 + "px";

		char_delete()
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
		}
	}
};

char_delete();