	
function descriptor_new(value, div) {
	
	const des_title_row1 = document.getElementById('descriptor-field-title');
	const des_field = document.getElementById('descriptor-field');

	if (value == 'new') {
		div.style.opacity = '100%';
		des_title_row1.style.opacity = '0%'
		des_field.style.opacity = '0%'
	} else {
		div.style.opacity = '0%';
	}
}

function get_medium_subtypes() {

	const title = document.getElementById('descriptor-medium-subtype-title')
	const des_title = document.getElementById('descriptor-medium-subtype-des-title')

	const medium_type_field  = document.getElementById('descriptor_medium_type');
	const medium_type = medium_type_field.options[medium_type_field.selectedIndex].value;

	const update = document.getElementById('descriptor_medium_subtype');
	const update_medium  = document.getElementById('descriptor_medium');

	update.style.backgroundColor = 'lightblue';
	setTimeout(function(){update.style.backgroundColor = "white"}, 200)
	update_medium.style.backgroundColor = 'lightblue';
	setTimeout(function(){update_medium.style.backgroundColor = "white"}, 200)

	response = fetch('/power/medium/subtype/select', {
		method: 'POST',
		body: JSON.stringify({
			'medium_type': medium_type
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			update.innerText = null;
			update_medium.innerText = null;

			title.innerText = jsonResponse.title;
			title.style.opacity = '100%';

			des_title.innerText = jsonResponse.des_title;

			const options = jsonResponse.options;
			let option;

			for (option of options)  {
				let o = document.createElement("option")
				o.value = option.id;
				o.text = option.name;
				update.add(o);
			}

			const options_medium = jsonResponse.options_medium
			let option_medium;

			for (option_medium of options_medium) {
				o = document.createElement('option')
				o.value = option_medium.id;
				o.text = option_medium.name;
				update_medium.add(o);
			}

		} else {
			console.log(jsonResponse.options);
		}
	})	
}

function get_medium() {

	const medium_subtype_field = document.getElementById('descriptor_medium_subtype');
	const medium_subtype = medium_subtype_field.options[medium_subtype_field.selectedIndex].value;
	
	const update  = document.getElementById('descriptor_medium');

	update.style.backgroundColor = 'lightblue';
	setTimeout(function(){update.style.backgroundColor = "white"}, 200)

	response = fetch('/power/medium/select', {
		method: 'POST',
		body: JSON.stringify({
			'medium_subtype': medium_subtype
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			const options = jsonResponse.options;
			let option;

			update.innerText = null;

			for (option of options)  {
				let o = document.createElement("option")
				o.value = option.id;
				o.text = option.name;
				update.add(o);
			}

		} else {
			console.log(jsonResponse.options);
		}
	})	
}

function get_descriptors(origin, source, medium_type, medium_subtype, medium, update) {

	update.style.backgroundColor = 'lightblue';
	setTimeout(function(){update.style.backgroundColor = "white"}, 200)

	response = fetch('/power/descriptor/select', {
		method: 'POST',
		body: JSON.stringify({
			'origin': origin,
			'source': source,
			'medium_type': medium_type,
			'medium_subtype': medium_subtype,
			'medium': medium
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			const select = document.getElementById('descriptor_field');
			let old_options = select.options;
			
			for (i = old_options.length - 1; i > -1; i--) {
				if (old_options[i].value == 'new' || old_options[i].value == 'all' || old_options[i].value == '') {
					console.log('keep');
				} else {
					old_options[i].remove();
				}
			}

			let options = jsonResponse.options;
			let option;

			for (option of options)  {
				console.log(option)
				let o = document.createElement("option")
				o.value = option.id;
				o.text = option.name;
				update.add(o);
			}

		} else {
			console.log(jsonResponse.options);
		}
	})	
}

function descriptor_des(value, div) {
	const row3 = document.getElementById('descriptor-row3') 
	if (value == 'new') {
		div.style.display = 'grid';
		div.style.maxHeight = div.scrollHeight + 'px';
		row3.style.display = 'grid';
		row3.style.maxHeight = div.scrollHeight + row3.scrollHeight + 'px';
	} else {
		div.style.maxHeight = '0px';
		setTimeout(function(){div.style.display = 'none'}, 400);
	}
}

function new_entry_show(row2, row3) {
	row2.style.display = 'grid';
	row2.style.maxHeight = row2.scrollHeight + 'px';
	row3.style.display = 'grid';
	row3.style.maxHeight = row3.scrollHeight + 'px';
}

function new_entry_hide(row2, row3) {
	row2.style.maxHeight = '0px';
	setTimeout(function(){row2.style.display = 'none'}, 400);
	row3.style.maxHeight = '0px';
	setTimeout(function(){row3.style.display = 'none'}, 400);
}

function field_show(value, title, field) {
	if (value != '' && value != 'new' && value != 'all') {
		title.style.opacity = '100%';
		field.style.opacity = '100%';
	} else {
		title.style.opacity = '0%';
		field.style.opacity = '0%';
	}
}
function descriptor() {
	const origin_field  = document.getElementById('descriptor_origin');
	const origin = origin_field.options[origin_field.selectedIndex].value;

	const source_field  = document.getElementById('descriptor_source');
	const source = source_field.options[source_field.selectedIndex].value;

	const medium_type_field  = document.getElementById('descriptor_medium_type');
	const medium_type = medium_type_field.options[medium_type_field.selectedIndex].value;
	
	const medium_subtype_field = document.getElementById('descriptor_medium_subtype');
	const medium_subtype = medium_subtype_field.options[medium_subtype_field.selectedIndex].value;

	const medium_field  = document.getElementById('descriptor_medium');
	const medium = medium_field.options[medium_field.selectedIndex].value;

	const descriptor_field  = document.getElementById('descriptor_field');
	const descriptor = descriptor_field.options[descriptor_field.selectedIndex].value;

	const sub_title_row1 = document.getElementById('descriptor-medium-subtype-title')
	const med_title_row1 = document.getElementById('descriptor-medium-title');
	const des_title_row1 = document.getElementById('descriptor-field-title');
	const sub_row1 = document.getElementById('descriptor-medium-subtype');
	const med_row1 = document.getElementById('descriptor-medium');
	const des_field = document.getElementById('descriptor-field');

	const ori_text = document.getElementById('descriptor-origin-field');
	const sou_text = document.getElementById('descriptor-source-field');
	const sub_text = document.getElementById('descriptor-medium-subtype-field');
	const med_text = document.getElementById('descriptor-medium-field');
	const des_text = document.getElementById('descriptor-descriptor-new');

	const ori_des = document.getElementById('descriptor-origin-des');
	const sou_des = document.getElementById('descriptor-source-des');
	const sub_des = document.getElementById('descriptor-medium-subtype-des');
	const med_des = document.getElementById('descriptor-medium-des');
	const des_des = document.getElementById('descriptor-descriptor-result');

	const row2 = document.getElementById('descriptor-row2');
	const row3 = document.getElementById('descriptor-row3');

	if (origin == 'new' || source == 'new' || medium_subtype ==  'new' || medium == 'new' || descriptor == 'new') {
		new_entry_show(row2, row3)
	}

	if (origin != 'new' && source != 'new' && medium_subtype !=  'new' && medium != 'new' && descriptor != 'new') {
		new_entry_hide(row2, row3)
	}

	descriptor_new(origin, ori_text);
	descriptor_des(origin, ori_des);
	descriptor_new(source, sou_text);
	descriptor_des(source, sou_des);
	descriptor_new(medium_subtype, sub_text)
	descriptor_des(medium_subtype, sub_des)
	descriptor_new(medium, med_text);
	descriptor_des(medium, med_des);

	field_show(medium_type, sub_title_row1, sub_row1)
	field_show(medium_subtype, med_title_row1, med_row1)
	
	if ((origin != 'all' && origin != '') || (source != 'all' && source != '') || (medium_type != 'all' && medium_type != '') || 
		(medium_subtype != 'all' && medium_subtype != '') || (medium != 'all' && medium != '')) {
		des_title_row1.style.opacity = '100%';
		des_field.style.opacity = '100%';
	} else {
		des_title_row1.style.opacity = '0%';
		des_field.style.opacity = '0%';
	}

	get_descriptors(origin, source, medium_type, medium_subtype, medium, descriptor_field)
}

function descriptor_field() {

	const origin_field  = document.getElementById('descriptor_origin');
	const origin = origin_field.options[origin_field.selectedIndex].value;

	const source_field  = document.getElementById('descriptor_source');
	const source = source_field.options[source_field.selectedIndex].value;
	
	const medium_subtype_field = document.getElementById('descriptor_medium_subtype');
	const medium_subtype = medium_subtype_field.options[medium_subtype_field.selectedIndex].value;

	const medium_field  = document.getElementById('descriptor_medium');
	const medium = medium_field.options[medium_field.selectedIndex].valu

	const descriptor_field  = document.getElementById('descriptor_field');
	const descriptor = descriptor_field.options[descriptor_field.selectedIndex].value;
	const des_text = document.getElementById('descriptor-descriptor-new');
	const des_des = document.getElementById('descriptor-descriptor-result');
	const row2 = document.getElementById('descriptor-row2');
	const row3 = document.getElementById('descriptor-row3');
	
	console.log(descriptor)

	if (origin == 'new' || source == 'new' || medium_subtype ==  'new' || medium == 'new' || descriptor == 'new') {
		new_entry_show(row2, row3)
	} else if (origin != 'new' && source != 'new' && medium_subtype !=  'new' && medium != 'new' && descriptor != 'new') {
		new_entry_hide(row2, row3)
	}

	descriptor_new(descriptor, des_text)
	descriptor_des(descriptor, des_des)
}

let des_counts = {'rows': 0, 'des_rows': 0, 'cha_count': 3, 'cha_rows': 0, 'rows_effect': 0, 'des_rows_effect': 0, 'cha_count_effect': 3, 'cha_rows_effect': 0}


function descriptor_submit() {

	const error_line = 'descriptor-err-line';
	const error_div = 'descriptor-err';

	const origin_name = document.getElementById('descriptor_origin_name').value;
	const source_name = document.getElementById('descriptor_source_name').value;
	const medium_subtype_name = document.getElementById('descriptor_medium_subtype_name').value;
	const medium_name = document.getElementById('descriptor_medium_name').value;
	const descriptor_name = document.getElementById('descriptor_name').value;

	const origin_des = document.getElementById('descriptor_origin_des').value;
	const source_des = document.getElementById('descriptor_source_des').value;
	const medium_subtype_des = document.getElementById('descriptor_medium_subtype_des').value;
	const medium_des = document.getElementById('descriptor_medium_des').value;
	const descriptor_result = document.getElementById('descriptor_result').value;

	const origin_field  = document.getElementById('descriptor_origin');
	const origin = origin_field.options[origin_field.selectedIndex].value;

	const source_field  = document.getElementById('descriptor_source');
	const source = source_field.options[source_field.selectedIndex].value;

	const medium_type_field  = document.getElementById('descriptor_medium_type');
	const medium_type = medium_type_field.options[medium_type_field.selectedIndex].value;
	
	const medium_subtype_field = document.getElementById('descriptor_medium_subtype');
	const medium_subtype = medium_subtype_field.options[medium_subtype_field.selectedIndex].value;

	const medium_field  = document.getElementById('descriptor_medium');
	const medium = medium_field.options[medium_field.selectedIndex].value;

	const descriptor_field  = document.getElementById('descriptor_field');
	const descriptor = descriptor_field.options[descriptor_field.selectedIndex].value;

	const descriptor_type_field = document.getElementById('descriptor_descriptor_type');
	const descriptor_type = descriptor_type_field.options[descriptor_type_field.selectedIndex].value;
	
	const power_id = document.getElementById('power_id').value;

	if (((origin == 'new' && origin_name != '' && origin_des != '') || (origin != 'new' )) || ((source == 'new' && source_name != '' && source_des != '') || (source != 'new')) || 
			((medium_subtype == 'new' && medium_subtype_name != '' && medium_subtype_des != '') || (medium_subtype != 'new')) || ((medium == 'new' && medium_name != '' && medium_des != '') || (medium != 'new')) ||
			((descriptor == 'new' && descriptor_name != '' && descriptor_result != '') || (descriptor != '')) ) {

			response = fetch('/descriptor/create', {
				method: 'POST',
				body: JSON.stringify({
					'origin': origin,
					'origin_name': origin_name,
					'origin_des': origin_des,
					'source': source,
					'source_name': source_name,
					'source_des': source_des,
					'medium_type': medium_type,
					'medium_subtype': medium_subtype,
					'medium_subtype_name': medium_subtype_name,
					'medium_subtype_des': medium_subtype_des,
					'medium': medium,
					'medium_name': medium_name,
					'medium_des': medium_des,
					'descriptor': descriptor,
					'descriptor_name': descriptor_name,
					'descriptor_result': descriptor_result,
					'descriptor_type': descriptor_type,
					'power_id': power_id
				}),
				headers: {
				'Content-Type': 'application/json',
				}
			})
			.then(response => response.json())
			.then(jsonResponse => {
				console.log(jsonResponse)
				if (jsonResponse.success) {

					const type = jsonResponse.type;
					console.log(type)

					const selects = document.getElementsByClassName('descriptor-sml')
					let select;

					for (select of selects)  {
						let option = document.createElement("option")
						option.value = jsonResponse.id;
						option.text = jsonResponse.name;
						select.add(option);
					}

					if (jsonResponse.add_select) {
						const new_options = jsonResponse.selects;
						let new_option;

						for (new_option of new_options) {
							let new_select = document.getElementById(new_option.select)
							let o = document.createElement("option");
							o.value = new_option.id;
							o.text = new_option.name;
							new_select.add(o);
							new_select.style.backgroundColor = 'lightblue';
							setTimeout(function(){new_select.style.backgroundColor = "white"}, 200)
						}
					};

					let table_div;
					let place_div;
					let btn_div;
					let btn_del;
					let title_div;

					console.log(des_counts);

					if (type == 'power') {
						table_div = 'descriptors-div';
						title_div = 'descriptor-table-title';
						if (jsonResponse.descriptor) {
							place_div = 'descriptors';
							btn_div = 'des-btn descriptor-btn';
							btn_del = 'des-del descriptor-btn-del';	
							des_counts.des_rows = des_counts.des_rows + 1
						} else {
							place_div = 'descriptor-table';
							btn_div = 'cha-btn descriptor-btn';
							btn_del = 'des-del cha-descriptor-btn-del';
							des_counts.cha_count = des_counts.cha_count + 1
							if (des_counts.cha_count == 4) {
								des_counts.cha_rows = des_counts.cha_rows + 1;
								des_counts.cha_count = 0;
							}
						}
					} else if (type == 'effect') {
						table_div = 'descriptors-interact-div';
						title_div = 'descriptor-interact-table-title';
						if (jsonResponse.descriptor) {
							place_div = 'descriptors-interact';
							btn_div = 'des-btn effect-btn';
							btn_del = 'des-del effect-btn-del';
							des_counts.des_rows_effect = des_counts.des_rows_effect + 1
						} else {
							place_div = 'descriptor-interact-table';
							btn_div = 'cha-btn effect-btn';
							btn_del = 'des-del cha-effect-btn-del';
							des_counts.cha_count_effect = des_counts.cha_count_effect + 1
							if (des_counts.cha_count_effect == 4) {
								des_counts.cha_rows_effect = des_counts.cha_rows_effect + 1;
								des_counts.cha_count_effect = 0;
							}}
					}

					console.log(des_counts);

					const div = document.getElementById(table_div);
					const table = document.getElementById(place_div);
					const title = document.getElementById(title_div)

					const btn = document.createElement('div');
					btn.className = btn_div;

					const txt = document.createElement('div');
					txt.className = 'des-txt';
					txt.innerHTML = jsonResponse.name;
				
					const del = document.createElement('div');
					del.className = 'descriptor-del'
					const deleteBtn = document.createElement('button');
					deleteBtn.className = btn_del;
					deleteBtn.setAttribute('data-id', jsonResponse.id);
					del.appendChild(deleteBtn);

					btn.appendChild(txt);
					btn.appendChild(del);

					div.style.display = "grid";
					div.style.padding = "1%";
					div.style.maxHeight = div.scrollHeight + title.scrollHeight + "px";
					div.style.padding = "1%";

					table.appendChild(btn);
					setTimeout(function(){btn.style.opacity = '100%'}, 10);

					if ((des_counts.des_rows > des_counts.rows) || (des_counts.cha_rows > des_counts.rows)) {
						div.style.maxHeight = div.scrollHeight + btn.scrollHeight + 'px';
						des_counts.rows = des_counts.rows + 1;
					} 
					
					if ((des_counts.des_rows_effect > des_counts.rows_effect) || (des_counts.cha_rows_effect > des_counts.rows_effect)) {
						div.style.maxHeight = div.scrollHeight + btn.scrollHeight + 'px';
						des_counts.rows_effect = des_counts.rows_effect + 1;
					}
					
					descriptor_delete()

					clear_errors(error_line, error_div)

				} else {

					const all_errors = jsonResponse.error;

					json_errors(error_line, error_div, all_errors);

					if (jsonResponse.add_select) {
						const new_options = jsonResponse.selects;
						let new_option;

						for (new_option of new_options) {
							let new_select = document.getElementById(new_option.select)
							let o = document.createElement("option");
							o.value = new_option.id;
							o.text = new_option.name;
							new_select.add(o);
							new_select.style.backgroundColor = 'lightblue';
							setTimeout(function(){new_select.style.backgroundColor = "white"}, 200)
						}
					};

				}
			})

		} else {

			clear_error_lines(error_line);

			const errors = document.getElementById(error_div)

			errors.style.display = "grid";
			errors.style.padding = "1%";

			let errors_height = errors.scrollHeight + 20;

			if (des == '') {
				let description = '';
				new_error(description, error_line, errors, errors_height)
			}

			errors.style.maxHeight = errors_height + "px";
			errors.style.padding = "1%";
		}
}

descriptor_delete = function() {

	const descriptors_to_delete = [{'delete_btn': 'cha-descriptor-del', 'button': 'cha-btn descriptor-btn', 'div': 'descriptors-div'},
									{'delete_btn': 'descriptor-btn-del', 'button': 'des-btn descriptor-btn', 'div': 'descriptors-div'},
									{'delete_btn': 'cha-effect-btn-del', 'button': 'cha-btn effect-btn', 'div': 'descriptors-interact-div'},
									{'delete_btn': 'effect-btn-del', 'button': 'des-btn effect-btn', 'div': 'descriptors-interact-div'}]

	descriptor_delete_function(descriptors_to_delete)

};

descriptor_delete();

function descriptor_delete_function(descriptors_to_delete) {

	let to_delete;

	for (to_delete in descriptors_to_delete) {
		const delete_btn = to_delete.delete_btn;
		const div_btn = to_delete.button;
		const container = to_delete.div;
	
		const deletes = document.getElementsByClassName(delete_btn);
		const div = document.getElementsByClassName(div_btn);
		const table_min = document.getElementById(container);
		
		for (let i = 0; i < deletes.length; i++) {
			const btn = deletes[i];
			btn.onclick = function(e) {
				console.log('click')
	
				const delId = e.target.dataset['id'];
				fetch('/power/powerdes/delete/' + delId, {
					method: 'DELETE'
				})
				.then(function() {
	
					remove_descriptor(delId)
	
					div.style.opacity = '0%';
					setTimeout(function(){div.style.display = 'none'}, 400)
	
					if (div_btn == 'cha-btn descriptor-btn') {
						des_counts.cha_count = des_counts.cha_count - 1
						if (des_counts.cha_count < 0) {
							des_counts.cha_rows = des_counts.cha_rows - 1
							des_counts.cha_count = 3
						}
					} else if (div_btn == 'des-btn descriptor-btn') {
						des_counts.des_rows = des_counts.des_rows - 1
					} else if (div_btn == 'cha-btn effect-btn') {
						des_counts.cha_count_effect = des_counts.cha_count_effect - 1
						if (des_counts.cha_count_effect < 0) {
							des_counts.cha_rows_effect = des_counts.cha_rows_effect - 1
							des_counts.cha_count_effect = 3
						}
					} else if (div_btn == 'des-btn effect-btn') {
						des_counts.des_rows_effect = des_counts.des_rows_effect - 1
					}
					
					if ((des_counts.cha_rows < des_counts.rows) && (des_counts.des_rows < des_counts.rows)) {
						table_min.style.maxHeight = table_min.scrollHeight - div.scrollHeight + 'px';
					}

					if ((des_counts.cha_rows_effect < des_counts.rows_effect) && (des_counts.des_rows_effect < des_counts.rows_effect)) {
						table_min.style.maxHeight = table_min.scrollHeight - div.scrollHeight + 'px';
					}
				})
			}
		}
	}
}

function remove_descriptor(id) {
	const selects = document.getElementsByClassName('descriptor-sml');
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
}