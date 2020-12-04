function dc_set() {
	const dc_set_field = document.getElementById('dc_set');
	let dc_set = dc_set_field.options[dc_set_field.selectedIndex].value;
	const check = document.getElementById("alt_check_check");

	const dc_table = document.getElementById('dc-levels');

	if (dc_set == 'table') {
		dc_table.style.display = 'grid';
		setTimeout(function(){dc_table.style.opacity = '100%'}, 10);
	} else if (dc_set != 'table' && check.checked == false) {
		dc_table.style.opacity = '0%';
		setTimeout(function(){dc_table.style.display = 'none';}, 400)
	}

}


function dc_mea_click() {
	const mea_grid = 'dc-measure-field';
	const mea_check = 'dc_mea_check';

	check_drop(mea_check, mea_grid);
}

function dc_dam_click() {
	const dam_grid = 'dc-damage-field';
	const dam_check = 'dc_dam_check';

	check_drop(dam_check, dam_grid);
}

function dc_key_click() {
	const key_grid = 'dc-keyword-field';
	const key_check = 'dc_key_check';
	
	check_drop(key_check, key_grid);
}

function dc_con_click() {
	const con_grid = 'dc-condition-field';
	const con_check = 'dc_con_check';
	
	check_drop(con_check, con_grid);
}

function dc_act_click() {
	const act_grid = 'dc-action-field';
	const act_check = 'dc_act_check';
		
	check_drop(act_check, act_grid)
}

function dc_def_click() {
	const def_grid = 'dc-defense-field';
	const def_check = 'dc_def_check';
	
	check_drop(def_check, def_grid);
}

function dc_measure_type() {
	const select = 'dc_mea_type';
	const dc_measure_value = 'dc-measure-value';
	const dc_measure_math = 'dc-measure-math';

	value_type_maxheight(select, dc_measure_math, dc_measure_value);
}

let dc_enter = 0;

let dc_col = "auto";
let key_col = "1%";
let des_col = "auto";
let mea_col = "1%";
let dam_col = "1%";
let def_col = "1%";
let act_col = "1%";
let con_col = "1%";
let del_col = "auto";
let dc_grid = dc_col + ' ' + key_col + ' ' + des_col + ' ' + mea_col + ' ' + dam_col + ' ' + def_col + ' ' + act_col + ' ' + con_col + ' ' + del_col; 

function dc_submit() {

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

	const mea_check_check = document.getElementById('dc_mea_check');
	const dam_check_check = document.getElementById('dc_dam_check');
	const key_check_check = document.getElementById('dc_key_check');
	const def_check_check = document.getElementById('dc_def_check');
	const con_check_check = document.getElementById('dc_con_check');
	const act_check_check = document.getElementById('dc_act_check');

	const mea_check = mea_check_check.checked;
	const dam_check = dam_check_check.checked;
	const key_check = key_check_check.checked;
	const def_check = def_check_check.checked;
	const con_check = con_check_check.checked;
	const act_check = act_check_check.checked;

	const mea_type_field = document.getElementById('dc_mea_type');
	let mea_type_value = mea_type_field.options[mea_type_field.selectedIndex].value;

	const mea_val_value = document.getElementById('dc_mea_val').value;

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
	
	const key_value = document.getElementById('dc_key').value;
	
	const def_field = document.getElementById('dc_def');
	let def_value = def_field.options[def_field.selectedIndex].value;
	
	const con1_field = document.getElementById('dc_con1');
	let con1_value = con1_field.options[con1_field.selectedIndex].value;
	
	const con2_field = document.getElementById('dc_con2');
	let con2_value = con2_field.options[con2_field.selectedIndex].value;
		
	const act_field = document.getElementById('dc_act');
	let act_value = act_field.options[act_field.selectedIndex].value;

	const bonus_id = document.getElementById('bonus_id').value;
	const error_line = 'dc-err-line';
	const error_table = 'dc-err';
	
	const mea_check = mea_check_check.checked;
	const dam_check = dam_check_check.checked;
	const key_check = key_check_check.checked;
	const def_check = def_check_check.checked;
	const con_check = con_check_check.checked;
	const act_check = act_check_check.checked;
	if ((des_value != '') && ((type_value == 'value' && class_value != '') || (type_value == 'math' && math_val_value != '' && math_value != '' && math_rank_value != '')) &&  
			((mea_check == true && mea_type_value == 'math' && mea_math_val_value != '' && mea_math_value != '' && mea_math_rnk_value != '') || 
			(mea_check == true && mea_type_value == 'value' && mea_val_value != '' && mea_unt_value != '') || (mea_check == false)) && 
			((dam_check == true && dam_value != '') || (dam_check == false)) && ((key_check == true && key_value != '') || (key_check == false)) && 
			((def_check == true && def_value != '') || (def_check == false)) && ((act_check == true && act_value != '') || (act_check == false)) && 
			((con_check == true && con1_value != '' && con2_value != '') || (con_check == false)) ) {


		response = fetch('/skill/dc/create', {
			method: 'POST',
			body: JSON.stringify({
				'bonus_id': bonus_id,
				'measure_check': mea_check,
				'damage_check': dam_check,
				'keyword_check': key_check,
				'defense_check': def_check,
				'condition_check': con_check,
				'action_check': act_check,
				'type': type_value,
				'val': class_value,
				'math_val': math_val_value,
				'math': math_value,
				'math_rank': math_rank_value,
				'measure_type': mea_type_value,
				'measure_val': mea_val_value,
				'measure_val_unit': mea_unt_value,
				'measure_math_val': mea_math_val_value,
				'measure_math': mea_math_value,
				'measure_rank': mea_math_rnk_value,
				'damage': dam_value,
				'keyword': key_value,
				'condition_one': con1_value,
				'condition_two': con2_value,
				'defense': def_value,
				'action': act_value,
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

				const dc = document.createElement('div');
				dc.className = 'dc-table-dc';
				if (type_value == 'value') {
					dc.innerHTML = jsonResponse.val;
					dc_col = "4%";
				} else if (type_value == 'math') {
					dc.innerHTML = jsonResponse.math_val + ' ' + jsonResponse.math + ' ' + jsonResponse.math_rank;
					dc_col = "15%";
				}
				
				const des = document.createElement('div');
				des.className = 'dc-table-des';
				des.innerHTML = jsonResponse.description;

				console.log(key_value);
				console.log(con_check.checked);

				const key = document.createElement('div');
				key.className = 'dc-table-key';

				if (key_value != '') {	
					key.innerHTML = jsonResponse.keyword;
					key_col = "auto";
				} else {
					key.innerHTML = '';
				}

				const mea = document.createElement('div');
				mea.className = 'dc-table-mea';
				
				if (mea_type_value == 'math') {
					mea.innerHTML = jsonResponse.measure_math_val + jsonResponse.measure_math + jsonResponse.measure_rank;
					mea_col = "auto";
				} else if (mea_type_value == 'value') {
					mea.innerHTML = jsonResponse.measure_val + ' ' + jsonResponse.measure_val_unit;
					mea_col = "auto";
				} else {
					mea.innerHTML = '';
				}

				const dam = document.createElement('div');
				dam.className = 'dc-table-dam';
				
				if (dam_value != '') {
					dam.innerHTML = jsonResponse.damage;
					dam_col = "auto";
				} else {
					dam.innerHTML = '';
				}

				const def = document.createElement('div');
				def.className = 'dc-table-def';
				
				if (def_value != '') {
					def.innerHTML = jsonResponse.defense;
					def_col = "auto";
				} else {
					def.innerHTML = '';
				}

				const act = document.createElement('div');
				act.className = 'dc-table-act';
				
				if (act_value != '') {
					act.innerHTML = jsonResponse.action;
					act_col = "auto";
				} else {
					act.innerHTML = '';
				}

				const con = document.createElement('div');
				con.className = 'dc-table-con';
				
				if (con1_value != '' && con2_value != '') {
					con.innerHTML = jsonResponse.condition_one + ' to ' + jsonResponse.condition_two;
					con_col = "auto";
				} else {
					con.innerHTML = '';
				}

				const dcDelete = document.createElement('div');
				dcDelete.className = 'dc-table-delete';
				const deleteBtn = document.createElement('button');
				deleteBtn.className = 'dc-xbox';
				deleteBtn.setAttribute('data-id', jsonResponse.id);
				dcDelete.appendChild(deleteBtn);

				let dc_grid = dc_col + ' ' + key_col + ' ' + des_col + ' ' + mea_col + ' ' + dam_col + ' ' + def_col + ' ' + act_col + ' ' + con_col + ' ' + del_col; 
					
				const key_title = document.getElementById('dc-table-title-key');
				const mea_title = document.getElementById('dc-table-title-mea');
				const dam_title = document.getElementById('dc-table-title-dam');
				const def_title = document.getElementById('dc-table-title-def');
				const act_title = document.getElementById('dc-table-title-act');
				const con_title = document.getElementById('dc-table-title-con');

				const table = document.getElementById('dc-table-container');

				table.style.display = "grid";
				table.style.padding = "1%";
				table.style.maxHeight = table.scrollHeight + "px";
				table.style.padding = "1%";
				table.style.gridTemplateColumns = dc_grid;

				table.appendChild(dc);
				table.appendChild(key);
				table.appendChild(des);
				table.appendChild(mea);
				table.appendChild(dam);
				table.appendChild(def);
				table.appendChild(act);
				table.appendChild(con);
				table.appendChild(dcDelete);

				let rows = [dc.scrollHeight, key.scrollHeight, des.scrollHeight, mea.scrollHeight, dam.scrollHeight, def.scrollHeight, act.scrollHeight, con.scrollHeight];
				let row_height = 0;

				for (i = 0; i < rows.length; i++) {
					if (rows[i] > row_height) {
						row_height = rows[i]
					}
				}

				if (key_check.checked == true) {
					key_title.style.maxWidth = key_title.scrollWidth + "px";
				} 

				if (mea_check.checked == true) {
					mea_title.style.maxWidth = mea_title.scrollWidth + "px";
				}

				if (dam_check.checked == true) {
					dam_title.style.maxWidth = dam_title.scrollWidth + "px";
				}

				if (def_check.checked == true) {
					def_title.style.maxWidth = def_title.scrollWidth + "px";
				}

				if (act_check.checked == true) {
					act_title.style.maxWidth = act_title.scrollWidth + "px";
				}
				if (con_check.checked == true) {
					con_title.style.maxWidth = act_title.scrollWidth + "px";
				}
				
				dc.style.maxHeight = dc.scrollHeight + "px";
				key.style.maxHeight = key.scrollHeight + "px";
				des.style.maxHeight = des.scrollHeight + "px";
				mea.style.maxHeight = mea.scrollHeight + "px";
				dam.style.maxHeight = dam.scrollHeight + "px";
				def.style.maxHeight = def.scrollHeight + "px";
				act.style.maxHeight = act.scrollHeight + "px";
				con.style.maxHeight = con.scrollHeight + "px";
				dcDelete.style.maxHeight = dcDelete.scrollHeight + "px";
				table.style.maxHeight = table.scrollHeight + row_height + 15 + "px";

				dc_delete();
				
				clear_errors(error_line, error_table);

			} else {

				console.log(jsonResponse)
				back_errors(error_line, error_table);
				
			}
		})

	} else {
		errors = document.getElementById('dc-err')

		errors.style.display = "grid";
		errors.style.padding = "1%";

		errors_delete = document.getElementsByClassName('dc-err-line');

		for (i = 0; i < errors_delete.length; i++) {
			errors_delete[i].style.display = "none";
		}

		let errors_height = errors.scrollHeight + 20;

		if (des_value == '') { 
			const error = document.createElement('div');
			error.className = 'dc-err-line'
			error.innerHTML = ' You enter a description';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (type_value == 'value' && class_value == '') { 
			const error = document.createElement('div');
			error.className = 'dc-err-line'
			error.innerHTML = ' You enter a dc value';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (type_value == 'math' && (math_val_value == '' || math_value == '' || math_rank_value == '')) { 
			const error = document.createElement('div');
			error.className = 'dc-err-line'
			error.innerHTML = ' You enter all dc math fields';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (mea_type_value == 'math' && (mea_math_val_value == '' || mea_math_value == '' || mea_math_rnk_value == '')) { 
			const error = document.createElement('div');
			error.className = 'dc-err-line'
			error.innerHTML = ' You enter all dc math fields or uncheck the measurement box';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (mea_type_value == 'value' && (mea_val_value == '' || mea_unt_value == '')) { 
			const error = document.createElement('div');
			error.className = 'dc-err-line'
			error.innerHTML = ' You enter all dc math fields';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (key_check.checked == true && key_value == '') { 
			const error = document.createElement('div');
			error.className = 'dc-err-line'
			error.innerHTML = ' You enter a keyword or uncheck the keyword box';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (dam_check.checked == true && dam_value == '') { 
			const error = document.createElement('div');
			error.className = 'dc-err-line'
			error.innerHTML = ' You enter a damage value or uncheck the damage box';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (def_check.checked == true && def_value == '') { 
			const error = document.createElement('div');
			error.className = 'dc-err-line'
			error.innerHTML = ' You choose a defense or uncheck the defense box';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (act_check.checked == true && act_value == '') { 
			const error = document.createElement('div');
			error.className = 'dc-err-line'
			error.innerHTML = ' You choose an action type or uncheck the action box';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		if (con_check.checked == true && (con1_value == '' || con2_value == '')) { 
			const error = document.createElement('div');
			error.className = 'dc-err-line'
			error.innerHTML = ' You choose both conditions or uncheck the condition box';

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";
			errors_height = errors_height + error.scrollHeight; 
		}

		errors.style.maxHeight = errors_height + "px";
		errors.style.padding = "1%";
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

			const delId = e.target.dataset['id'];
			fetch('/skill/dc/delete/' + delId, {
				method: 'DELETE'
			})
			.then(function() {

				dcs[i].style.maxHeight = "0px";
				dcs[i].style.padding = "0px";
				dcs[i].style.marginBottom = "0px";
				keys[i].style.maxHeight = "0px";
				keys[i].style.padding = "0px";
				keys[i].style.marginBottom = "0px";
				keys[i].innerHTML = '';
				dess[i].style.maxHeight = "0px";
				dess[i].style.padding = "0px";
				dess[i].style.marginBottom = "0px";
				meas[i].style.maxHeight = "0px";
				meas[i].style.padding = "0px";
				meas[i].style.marginBottom = "0px";
				meas[i].innerHTML = '';
				dams[i].style.maxHeight = "0px";
				dams[i].style.padding = "0px";
				dams[i].style.marginBottom = "0px";
				dams[i].innerHTML = '';
				acts[i].style.maxHeight = "0px";
				acts[i].style.padding = "0px";
				acts[i].style.marginBottom = "0px";
				acts[i].innerHTML = '';
				defs[i].style.maxHeight = "0px";
				defs[i].style.padding = "0px";
				defs[i].style.marginBottom = "0px";
				defs[i].innerHTML = '';
				cons[i].style.maxHeight = "0px";
				cons[i].style.padding = "0px";
				cons[i].style.marginBottom = "0px";
				cons[i].innerHTML = '';
				deletesDiv[i].style.maxHeight = "0px";
				deletesDiv[i].style.padding = "0px";
				deletesDiv[i].style.marginBottom = "0px";

				setTimeout(function(){
					dcs[i].style.display = 'none';
					keys[i].style.display = 'none';
					dess[i].style.display = 'none';
					meas[i].style.display = 'none';
					dams[i].style.display = 'none';
					acts[i].style.display = 'none';
					defs[i].style.display = 'none';
					cons[i].style.display = 'none';
					deletesDiv[i].style.display = 'none';
				}, 400);

				for (let int = 0; int < keys.length; int++) {
					if (keys[int].innerHTML != ''){
						key_title.style.maxWidth = key_title.scrollWidth + "px";
						key_col = "auto";
						break;
					} else {
						key_title.style.maxWidth = "0px";
						key_col = "1%";
					}
				}

				for (let int = 0; int < meas.length; int++) {
					if (meas[int].innerHTML != ''){
						mea_title.style.maxWidth = mea_title.scrollWidth + "px";
						mea_col = "auto";
						break;
					} else {
						mea_title.style.maxWidth = "0px";
						mea_col = "1%";
					}
				}
		
				for (let int = 0; int < dams.length; int++) {
					if (dams[int].innerHTML != ''){
						dam_title.style.maxWidth = dam_title.scrollWidth + "px";
						dam_col = "auto";
						break;
					} else {
						dam_title.style.maxWidth = "0px";
						dam_col = "1%";
					}
				}

				for (let int = 0; int < defs.length; int++) {
					if (defs[int].innerHTML != ''){
						def_title.style.maxWidth = def_title.scrollWidth + "px";
						def_col = "auto";
						break;
					} else {
						def_title.style.maxWidth = "0px";
						def_col = "1%";
					}
				}
			
				for (let int = 0; int < acts.length; int++) {
					if (acts[int].innerHTML != ''){
						act_title.style.maxWidth = act_title.scrollWidth + "px";
						act_col = "auto";
						break;
					} else {
						act_title.style.maxWidth = "0px";
						act_col = "1%";
					}
				}
		
				for (let int = 0; int < cons.length; int++) {
					if (cons[int].innerHTML != ''){
						con_title.style.maxWidth = con_title.scrollWidth + "px";
						con_col = "auto";
						break;
					} else {
						con_title.style.maxWidth = "0px";
						con_col = "1%";
					}
				}

				const table = document.getElementById('dc-table-container');

				let dc_grid = dc_col + ' ' + key_col + ' ' + des_col + ' ' + mea_col + ' ' + dam_col + ' ' + def_col + ' ' + act_col + ' ' + con_col + ' ' + del_col; 
				table.style.gridTemplateColumns = dc_grid;
			})
		}
	}
}

dc_delete();
