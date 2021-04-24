

function get_medium_subtypes() {
	const select = 'descriptor_medium_type';
	const fill = {'subtypes': 'descriptor_medium_subtype',
					'mediums': 'descriptor_medium'};
	const sub = 'power_create';
	const titles = {'title': 'descriptor-medium-subtype-title',
					'description': 'descriptor-medium-subtype-des-title'};

	id_select(select, fill, medium_subtype_select, sub, false, titles, true);
}

function get_medium() {
	const select = 'descriptor_medium_subtype';
	const fill = 'descriptor_medium';
	const sub = 'power_create';

	id_select(select, fill, medium_select, sub);
}

function descriptor() {
	const origin  = 'descriptor_origin';
	const source  = 'descriptor_source';
	const medium_type  = 'descriptor_medium_type';
	const medium_subtype = 'descriptor_medium_subtype';
	const medium  = 'descriptor_medium';
	const descriptor = 'descriptor_field';

	const sub_title_row1 = 'descriptor-medium-subtype-title'
	const med_title_row1 = 'descriptor-medium-title';
	const sub_row1 = 'descriptor-medium-subtype';
	const med_row1 = 'descriptor-medium';
	const des_title_row1 = 'descriptor-field-title';
	const des_field = 'descriptor-field';

	const ori_text = 'descriptor-origin-field';
	const sou_text = 'descriptor-source-field';
	const sub_text = 'descriptor-medium-subtype-field';
	const med_text = 'descriptor-medium-field';
	const des_text = 'descriptor-descriptor-new';

	const ori_des = 'descriptor-origin-des';
	const sou_des = 'descriptor-source-des';
	const sub_des = 'descriptor-medium-subtype-des';
	const med_des = 'descriptor-medium-des';
	const des_des = 'descriptor-descriptor-result';

	const row2 = 'descriptor-row2';
	const row3 = 'descriptor-row3';
	const damage = 'descriptor-damage-row';


	descriptor_new(origin, ori_text, des_title_row1, des_field);
	descriptor_des(origin, ori_des, row3);
	descriptor_new(source, sou_text, des_title_row1, des_field);
	descriptor_des(source, sou_des, row3);
	descriptor_new(medium_subtype, sub_text, des_title_row1, des_field)
	descriptor_des(medium_subtype, sub_des, row3)
	descriptor_new(medium, med_text, des_title_row1, des_field);
	descriptor_des(medium, med_des, row3);

	field_show(medium_type, sub_title_row1, sub_row1)
	field_show(medium_subtype, med_title_row1, med_row1)

	descriptor_create_fields(origin, source, medium_subtype, medium, descriptor, row2, row3, damage)
	show_descriptor_field(origin, source, medium_type, medium_subtype, medium, des_field, des_title_row1);

	get_descriptors(origin, source, medium_type, medium_subtype, medium, descriptor)
}

function descriptor_field() {

	const origin  = 'descriptor_origin';
	const source  = 'descriptor_source';
	const medium_subtype = 'descriptor_medium_subtype';
	const medium = 'descriptor_medium';

	const descriptor  = 'descriptor_field';
	const des_text = 'descriptor-descriptor-new';
	const des_des = 'descriptor-descriptor-result';
	const row2 = 'descriptor-row2';
	const row3 = 'descriptor-row3';
	const damage = 'descriptor-damage-row';
	const des_title_row1 = 'descriptor-field-title';
	const des_field = 'descriptor-field';
	
	console.log(descriptor)

	descriptor_create_fields(origin, source, medium_subtype, medium, descriptor, row2, row3, damage)

	descriptor_new(descriptor, des_text, des_title_row1, des_field);
	descriptor_des(descriptor, des_des, row3)
}

let des_counts = {'rows': 0, 'des_rows': 0, 'cha_count': 3, 'cha_rows': 0, 'rows_effect': 0, 'des_rows_effect': 0, 'cha_count_effect': 3, 'cha_rows_effect': 0, 'des_total': 0, 'eff_total': 0}


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

	const damage_check = document.getElementById('descriptor_damage');
	const damage = damage_check.checked;
	
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
					'damage': damage,
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
							des_counts.des_total = des_counts.des_total + 1
						} else {
							place_div = 'descriptor-table';
							btn_div = 'cha-btn cha-descriptor-btn';
							btn_del = 'des-del cha-descriptor-btn-del';
							des_counts.cha_count = des_counts.cha_count + 1
							des_counts.des_total = des_counts.des_total + 1
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
							btn_div = 'des-btn des-effect-btn';
							btn_del = 'des-del effect-btn-del';
							des_counts.des_rows_effect = des_counts.des_rows_effect + 1
							des_counts.eff_total = des_counts.eff_total + 1
						} else {
							place_div = 'descriptor-interact-table';
							btn_div = 'cha-btn cha-effect-btn';
							btn_del = 'des-del cha-effect-btn-del';
							des_counts.cha_count_effect = des_counts.cha_count_effect + 1
							des_counts.eff_total = des_counts.eff_total + 1
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

	const descriptors_to_delete = [{'delete_btn': 'cha-descriptor-btn-del', 'button': 'cha-descriptor-btn', 'div': 'descriptors-div'},
									{'delete_btn': 'descriptor-btn-del', 'button': 'descriptor-btn', 'div': 'descriptors-div'},
									{'delete_btn': 'cha-effect-btn-del', 'button': 'cha-effect-btn', 'div': 'descriptors-interact-div'},
									{'delete_btn': 'effect-btn-del', 'button': 'des-effect-btn', 'div': 'descriptors-interact-div'}]

	descriptor_delete_function(descriptors_to_delete)

};

descriptor_delete();

function descriptor_delete_function(descriptors_to_delete) {

	let to_delete;

	for (to_delete of descriptors_to_delete) {
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
				.then(response => response.json())
				.then(jsonResponse => {
	
					let delId = jsonResponse.id

					console.log('delete ' + delId)
					remove_descriptor(delId)
	
					div[i].style.opacity = '0%';
					setTimeout(function(){div[i].style.display = 'none'}, 400)
	
					if (div_btn == 'cha-descriptor-btn') {
						des_counts.cha_count = des_counts.cha_count - 1;
						des_counts.des_total = des_counts.des_total - 1;
						if (des_counts.cha_count < 0) {
							des_counts.cha_rows = des_counts.cha_rows - 1;
							des_counts.cha_count = 3;
						}
					} else if (div_btn == 'descriptor-btn') {
						des_counts.des_rows = des_counts.des_rows - 1;
						des_counts.des_total = des_counts.des_total - 1;
					} else if (div_btn == 'cha-effect-btn') {
						des_counts.cha_count_effect = des_counts.cha_count_effect - 1;
						des_counts.eff_total = des_counts.eff_total - 1;
						if (des_counts.cha_count_effect < 0) {
							des_counts.cha_rows_effect = des_counts.cha_rows_effect - 1;
							des_counts.cha_count_effect = 3;
						}
					} else if (div_btn == 'des-effect-btn') {
						des_counts.des_rows_effect = des_counts.des_rows_effect - 1
						des_counts.eff_total = des_counts.eff_total - 1
					}

					console.log(des_counts);
					
					if ((des_counts.cha_rows < des_counts.rows) && (des_counts.des_rows < des_counts.rows)) {
						table_min.style.maxHeight = table_min.scrollHeight - div.scrollHeight + 'px';
					}

					if ((des_counts.cha_rows_effect < des_counts.rows_effect) && (des_counts.des_rows_effect < des_counts.rows_effect)) {
						table_min.style.maxHeight = table_min.scrollHeight - div.scrollHeight + 'px';
					}

					if (des_counts.des_total == 0) {
						const descriptor_div = document.getElementById('descriptors-div');
						descriptor_div.style.maxHeight = '0px';
						setTimeout(function(){descriptor_div.style.display = 'none'}, 400)
					}

					if (des_counts.eff_total == 0) {
						const descriptor_div = document.getElementById('descriptors-interact-div');
						descriptor_div.style.maxHeight = '0px';
						setTimeout(function(){descriptor_div.style.display = 'none'}, 400)
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
			if (option.value == id) {
				console.log(option.value);
				option.remove();
			}
		}
	}
}

function minimize_descriptor_div(chas, dess) {
	let empty = true
	let cha;
	let des;

	for (cha of chas) {
		if (cha.style.display = 'grid') {
			empty = false;
		} 
	}
	for (des of dess) {
		if (cha.style.display = 'grid') {
			empty = false;
		} 
	}
	if (empty) {
		table_min.style.maxHeight = '0px';
		setTimeout(function(){table_min.style.display = 'none'}, 400);
	}
}