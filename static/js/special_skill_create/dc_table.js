function dc_set() {
	const dc_set_field = document.getElementById('dc_set');
	let dc_set = dc_set_field.options[dc_set_field.selectedIndex].value;

	const dc_table = document.getElementById('dc-levels');

	if (dc_set == 'table') {
		dc_table.style.display = 'grid';
	}

}

function dc_dc_type() {
	const type_field = document.getElementById('dc_type');
	let type_value = type_field.options[type_field.selectedIndex].value;

	const dc_class = document.getElementById('dc-class');
	const dc_math = document.getElementById('dc-math');
	const dc_entry = document.getElementById('dc-entry');

	if (type_value == 'value') {
		dc_class.style.display = "grid";
		dc_math.style.display = "none";
		dc_class.style.padding = "1%";
		dc_class.style.maxHeight = dc_class.scrollHeight + "px";
		dc_entry.style.display = "grid";
		dc_entry.style.padding = "1%";
		dc_entry.style.maxHeight = dc_entry.scrollHeight + "px";
		dc_entry.style.padding = "1%";
	} else if (type_value == 'math') {
		dc_math.style.display = "grid";
		dc_math.style.padding = "1%";
		dc_math.style.maxHeight = dc_math.scrollHeight + "px";
		dc_class.style.display = "none";
		dc_entry.style.display = "grid";
		dc_entry.style.padding = "1%";
		dc_entry.style.maxHeight = dc_entry.scrollHeight + "px";
		dc_entry.style.padding = "1%";
	} else {
		dc_class.style.display = "none";
		dc_math.style.display = "none";
		dc_entry.style.maxHeight = "0px";
		dc_entry.style.padding = "0px";
	}
}

function dc_mea_click() {
	const mea_grid = document.getElementById('dc-measurement-field');
	const mea_check = document.getElementById('dc_mea_check');

	if (mea_check.checked == true) {
		mea_grid.style.display = "grid";
		mea_grid.style.padding = "1%";
		mea_grid.style.maxHeight = mea_grid.scrollHeight + "px";
		mea_grid.style.padding = "1%";
	}  else {
		mea_grid.style.maxHeight = "0px";
		mea_grid.style.padding = "0px";
	}
}

function dc_dam_click() {
	const dam_grid = document.getElementById('dc-damage-field');
	const dam_check = document.getElementById('dc_dam_check');

	if (dam_check.checked == true) {
		dam_grid.style.display = "grid";
		dam_grid.style.padding = "1%";
		dam_grid.style.maxHeight = dam_grid.scrollHeight + "px";
		dam_grid.style.padding = "1%";
	}  else {
		dam_grid.style.maxHeight = "0px";
		dam_grid.style.padding = "0px";
	}

}

function dc_key_click() {
	const key_grid = document.getElementById('dc-keyword-field');
	const key_check = document.getElementById('dc_key_check');

	if (key_check.checked == true) {
		key_grid.style.display = "grid";
		key_grid.style.padding = "1%";
		key_grid.style.maxHeight = key_grid.scrollHeight + "px";
		key_grid.style.padding = "1%";
	}  else {
		key_grid.style.maxHeight = "0px";
		key_grid.style.padding = "0px";
	}
}

function dc_con_click() {
	const con_grid = document.getElementById('dc-condition-field');
	const con_check = document.getElementById('dc_con_check');

	if (con_check.checked == true) {
		con_grid.style.display = "grid";
		con_grid.style.padding = "1%";
		con_grid.style.maxHeight = con_grid.scrollHeight + "px";
		con_grid.style.padding = "1%";
	}  else {
		con_grid.style.maxHeight = "0px";
		con_grid.style.padding = "0px";
	}
}

function dc_act_click() {
	const act_grid = document.getElementById('dc-action-field');
	const act_check = document.getElementById('dc_act_check');

	if (act_check.checked == true) {
		act_grid.style.display = "grid";
		act_grid.style.padding = "1%";
		act_grid.style.maxHeight = act_grid.scrollHeight + "px";
		act_grid.style.padding = "1%";
	}  else {
		act_grid.style.maxHeight = "0px";
		act_grid.style.padding = "0px";
	}
}

function dc_def_click() {
	const def_grid = document.getElementById('dc-defense-field');
	const def_check = document.getElementById('dc_def_check');

	if (def_check.checked == true) {
		def_grid.style.display = "grid";
		def_grid.style.padding = "1%";
		def_grid.style.maxHeight = def_grid.scrollHeight + "px";
		def_grid.style.padding = "1%";
	}  else {
		def_grid.style.maxHeight = "0px";
		def_grid.style.padding = "0px";
	}
}

function dc_measure_type() {
	const mea_type_field = document.getElementById('dc_mea_type');
	let mea_type_value = mea_type_field.options[mea_type_field.selectedIndex].value;

	const dc_measure_value = document.getElementById('dc-measure-value');
	const dc_measure_math = document.getElementById('dc-measure-math');

	if (mea_type_value == 'value') {
		dc_measure_value.style.display = "grid"
		dc_measure_math.style.display = "none";
		dc_measure_value.style.padding = "1%";
		dc_measure_value.style.maxHeight = dc_measure_value.scrollHeight + "px";
		dc_measure_value.style.padding = "1%";
	} else if (mea_type_value == 'math') {
		dc_measure_math.style.display = "grid"
		dc_measure_value.style.display = "none";
		dc_measure_math.style.padding = "1%";
		dc_measure_math.style.maxHeight = dc_measure_math.scrollHeight + "px";
		dc_measure_math.style.padding = "1%";
	} else {
		dc_measure_math.style.display = "none";
		dc_measure_value.style.display = "none";
	}
}

let dc_enter = 0;

function dc_submit() {

	const table = document.getElementById('dc-table-container');

	const type_field = document.getElementById('dc_type');
	let type_value = type_field.options[type_field.selectedIndex].value;

	const class_field = document.getElementById('dc_class');
	let class_value = class_field.options[class_field.selectedIndex].value;
	
	const math_val_field = document.getElementById('dc_math_value');
	let math_val_value = math_val_field.options[math_val_field.selectedIndex].value;
	const math_field = document.getElementById('dc_math');
	let math_value = math_field.options[math_field.selectedIndex].value;
	const math_rank_field = document.getElementById('dc_math_rank');
	let math_rank_value = math_rank_field.options[math_rank_field.selectedIndex].value;

	const des_value = document.getElementById('dc_des').value;

	const mea_check = document.getElementById('dc_mea_check');
	const dam_check = document.getElementById('dc_dam_check');
	const key_check = document.getElementById('dc_key_check');
	const def_check = document.getElementById('dc_def_check');
	const con_check = document.getElementById('dc_con_check');
	const act_check = document.getElementById('dc_act_check');

	const mea_type_field = document.getElementById('dc_mea_type');
	let mea_type_value = mea_type_field.options[mea_type_field.selectedIndex].value;

	const mea_val_field = document.getElementById('dc_mea_val');
	let mea_val_value = mea_val_field.options[mea_val_field.selectedIndex].value;
	const mea_unt_field = document.getElementById('dc_mea_unit');
	let mea_unt_value = mea_unt_field.options[mea_unt_field.selectedIndex].value;

	
	const mea_math_val_field = document.getElementById('dc_mea_math_val');
	let mea_math_val_value = mea_math_val_field.options[mea_math_val_field.selectedIndex].value;
	const mea_math_field = document.getElementById('dc_mea_math');
	let mea_math_value = mea_math_field.options[mea_math_field.selectedIndex].value;
	const mea_math_rnk_field = document.getElementById('dc_mea_math_rank');
	let mea_math_rnk_value = mea_math_rnk_field.options[mea_math_rnk_field.selectedIndex].value;
	
	const dam_field = document.getElementById('dc_dam');
	let dam_value = dam_field.options[dam_field.selectedIndex].value;
	
	const key_field = document.getElementById('dc_key');
	let key_value = key_field.options[key_field.selectedIndex].value;
	
	const def_field = document.getElementById('dc_def');
	let def_value = def_field.options[def_field.selectedIndex].value;
	
	const con1_field = document.getElementById('dc_con1');
	let con1_value = con1_field.options[con1_field.selectedIndex].value;
	
	const con2_field = document.getElementById('dc_con2');
	let con2_value = con2_field.options[con2_field.selectedIndex].value;
		
	const act_field = document.getElementById('dc_act');
	let act_value = act_field.options[act_field.selectedIndex].value;

	if ((des_value != '') && ((type_value == 'value' && class_value != '') || (type_value == 'math' && math_val_value != '' && math_value != '' && math_rank_value != '')) &&  
			((mea_check.checked == true && mea_type_value == 'math' && mea_math_val_value != '' && mea_math_value != '' && mea_math_rnk_value != '') || 
			(mea_check.checked == true && mea_type_value == 'value' && mea_val_value != '' && mea_unt_value != '') || (mea_check.checked == false)) && 
			((dam_check.checked == true && dam_value != '') || (dam_check.checked == false)) && ((key_check.checked == true && key_value != '') || (key_check.checked == false)) && 
			((def_check.checked == true && def_value != '') || (def_check.checked == false)) && ((act_check.checked == true && act_value != '') || (act_check.checked == false)) && 
			((con_check.checked == true && con1_value != '' && con2_value != '') || (con_check.checked == false)) ) {

		const dc = document.createElement('div');
		dc.className = 'dc-table-dc';
		if (type_value == 'value') {
			dc.innerHTML = class_value;
		} else if (type_value == 'math') {
			dc.innerHTML = math_val_value + ' ' + math_value + ' ' + math_rank_value;
		}
		
		const des = document.createElement('div');
		des.className = 'dc-table-des';
		des.innerHTML = des_value;

		const mea = document.createElement('div');
		mea.className = 'dc-table-mea'
		if (mea_type_value == 'value') {
			mea.innerHTML = mea_val_value + ' ' + mea_unt_value;
		} else if (mea_type_value == 'math') {
			mea.innerHTML = mea_math_val_value + ' ' + mea_math_value + ' ' + mea_math_rnk_value;
		} else { 
			mea.innerHTML = '';
		}

		const dam = document.createElement('div');
		dam.className = 'dc-table-dam';
		if (dam_check.checked == true) {
			dam.innerHTML = dam_value;
		} else {
			dam.innerHTML = ''
		}

		const key = document.createElement('div');
		key.className = 'dc-table-key';
		if (key_check.checked == true) {
			key.innerHTML = key_value;
		} else {
			key.innerHTML = ''
		}

		const def = document.createElement('div');
		def.className = 'dc-table-def';
		if (def_check.checked == true) {
			def.innerHTML = def_value;
		} else {
			def.innerHTML = ''
		}

		const act = document.createElement('div');
		act.className = 'dc-table-act';
		if (act_check.checked == true) {
			act.innerHTML = act_value;
		} else {
			act.innerHTML = ''
		}

		const con = document.createElement('div');
		con.className = 'dc-table-con';
		if (con_check.checked == true) {
			con.innerHTML = con_value;
		} else {
			con.innerHTML = ''
		}
	
		const dcDelete = document.createElement('div');
		dcDelete.className = 'dc-table-delete'
		const deleteBtn = document.createElement('button');
		deleteBtn.className = 'dc-xbox';
		deleteBtn.innerHTML = '&cross;';
		deleteBtn.setAttribute('data-id', dc_enter);
		dcDelete.appendChild(deleteBtn);

		dc_enter = dc_enter + 1;
			
		const key_title = document.getElementById('dc-table-title-key');
		const mea_title = document.getElementById('dc-table-title-mea');
		const dam_title = document.getElementById('dc-table-title-dam');
		const def_title = document.getElementById('dc-table-title-def');
		const act_title = document.getElementById('dc-table-title-act');
		const con_title = document.getElementById('dc-table-title-con');

		if (key_check.checked == true) {
			key_title.style.display = 'block';
		} 

		if (mea_check.checked == true) {
			mea_title.style.display = 'block';
		}

		if (dam_check.checked == true) {
			dam_title.style.display = 'block';
		}

		if (def_check.checked == true) {
			def_title.style.display = 'block';
		}

		if (act_check.checked == true) {
			act_title.style.display = 'block';
		}

		if (con_check.checked == true) {
			con_title.style.display = 'block';
		}

		table.style.display = "grid";
		table.style.padding = "1%";
		table.style.maxHeight = table.scrollHeight + "px";
		table.style.padding = "1%";

		table.appendChild(dc);
		table.appendChild(key);
		table.appendChild(des);
		table.appendChild(mea);
		table.appendChild(dam);
		table.appendChild(def);
		table.appendChild(act);
		table.appendChild(con);
		
		dc.style.maxHeight = dc.scrollHeight + "px";
		key.style.maxHeight = key.scrollHeight + "px";
		des.style.maxHeight = des.scrollHeight + "px";
		mea.style.maxHeight = mea.scrollHeight + "px";
		dam.style.maxHeight = dam.scrollHeight + "px";
		def.style.maxHeight = def.scrollHeight + "px";
		act.style.maxHeight = act.scrollHeight + "px";
		con.style.maxHeight = con.scrollHeight + "px";
		dcDelete.style.maxHeight = dcDelete.scrollHeight + "px";
		table.style.maxHeight = table.scrollHeight + des.scrollHeight + 15 + "px";

		dc_delete();
	}
}

function dc_delete() {
	const deletes = document.querySelectorAll('.dc-xbox');
	const dcs = document.getElementsByClassName('dc-table-dc');
	const keys = document.getElementsByClassName('dc-table-key');
	const dess = document.getElementsByClassName('dc-table-des');
	const meas = document.getElementsByClassName('dc-table-mea');
	const dams = document.getElementsByClassName('dc-table-dam');
	const defs = document.getElementsByClassName('dc-table-def');
	const acts = document.getElementsByClassName('dc-table-act');
	const cons = document.getElementsByClassName('dc-table-con');
	const deletesDiv = document.getElementsByClassName('dc-table-delete');

	const key_title = document.getElementById('dc-table-title-key');
	const mea_title = document.getElementById('dc-table-title-mea');
	const dam_title = document.getElementById('dc-table-title-dam');
	const def_title = document.getElementById('dc-table-title-def');
	const act_title = document.getElementById('dc-table-title-act');
	const con_title = document.getElementById('dc-table-title-con');

	for (let i = 0; i < deletes.length; i++) {
		const btn = deletes[i];
		btn.onclick = function(e) {
			console.log('click')

			dcs[i].style.maxHeight = "0px";
			dcs[i].style.padding = "0px";
			dcs[i].style.marginBottom = "0px";
			keys[i].style.maxHeight = "0px";
			keys[i].style.padding = "0px";
			keys[i].style.marginBottom = "0px";
			dess[i].style.maxHeight = "0px";
			dess[i].style.padding = "0px";
			dess[i].style.marginBottom = "0px";
			meas[i].style.maxHeight = "0px";
			meas[i].style.padding = "0px";
			meas[i].style.marginBottom = "0px";
			dams[i].style.maxHeight = "0px";
			dams[i].style.padding = "0px";
			dams[i].style.marginBottom = "0px";
			acts[i].style.maxHeight = "0px";
			acts[i].style.padding = "0px";
			acts[i].style.marginBottom = "0px";
			defs[i].style.maxHeight = "0px";
			defs[i].style.padding = "0px";
			defs[i].style.marginBottom = "0px";
			cons[i].style.maxHeight = "0px";
			cons[i].style.padding = "0px";
			cons[i].style.marginBottom = "0px";
			deletesDiv[i].style.maxHeight = "0px";
			deletesDiv[i].style.padding = "0px";
			deletesDiv[i].style.marginBottom = "0px";
		}
	}

	for (let i = 0; i < keys.length; i++) {
		if (keys[i].innerHTML != ''){
			key_title.style.display = 'block';
			break;
		} else {
			key_title.style.display = 'none';
		}
	}

	for (let i = 0; i < meas.length; i++) {
		if (meas[i].innerHTML != ''){
			mea_title.style.display = 'block';
			break;
		} else {
			mea_title.style.display = 'none';
		}
	}
	
	for (let i = 0; i < dams.length; i++) {
		if (dams[i].innerHTML != ''){
			dam_title.style.display = 'block';
			break;
		} else {
			dam_title.style.display = 'none';
		}
	}

	for (let i = 0; i < defs.length; i++) {
		if (defs[i].innerHTML != ''){
			def_title.style.display = 'block';
			break;
		} else {
			def_title.style.display = 'none';
		}
	}
		
	for (let i = 0; i < acts.length; i++) {
		if (acts[i].innerHTML != ''){
			act_title.style.display = 'block';
			break;
		} else {
			act_title.style.display = 'none';
		}
	}
	
	for (let i = 0; i < cons.length; i++) {
		if (cons[i].innerHTML != ''){
			con_title.style.display = 'block';
		} else {
			con_title.style.display = 'none';
		}
	}
	
}

dc_delete();